import os
import tkinter as tk

from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from graph import Graph
from draw_path import draw_path

class ImageViewer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.graph = Graph()
        self.master = master
        self.output_directory_path = "./images"
        self.max_floors = 0
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Create a frame to hold buttons.
        button_frame = tk.Frame(self)
        button_frame.pack(side=tk.TOP, pady=10)

        # Button to upload an image.
        self.upload_button = tk.Button(button_frame, text="Carregar Imagens", command=self.upload_images)
        self.upload_button.pack(side=tk.LEFT, padx=10)
        
        # Button to show the path on the image.
        self.show_path_button = tk.Button(button_frame, text="Exibir Caminho", command=self.show_path, state=tk.DISABLED)
        self.show_path_button.pack(side=tk.LEFT, padx=10)

        # Canvas to show image.
        self.canvas = tk.Canvas(self, bg="white", width=800, height=600)
        self.canvas.pack(side=tk.LEFT)

        # Zoom and move variables
        self.bind_all("<KeyPress>", self.on_key_press)
        self.bind_all("<KeyRelease>", self.on_key_release)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonPress-1>", self.on_drag_start)
        self.canvas.bind("<ButtonRelease-1>", self.on_drag_stop)

        self.scale = 1.0
        self.zooming = False
        self.start_x = 0
        self.start_y = 0

    def upload_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Bitmap files", "*.bmp")])
        if file_paths:
            self.image_paths = file_paths
            self.max_floors += len(file_paths)
            try:
                self.original_images = [Image.open(path) for path in self.image_paths]
                self.display_images()
            except Exception as e:
                messagebox.showerror("Erro", f"Não foi possível carregar as imagens:\n{str(e)}")

    def display_images(self):
        # Resize images to a common height
        common_height = min(image.size[1] for image in self.original_images)
        resized_images = [image.resize((int(image.width * common_height / image.height), common_height)) for image in self.original_images]

        # Create a composite image by stacking the images horizontally
        composite_width = sum(image.width for image in resized_images)
        composite_height = common_height
        composite_image = Image.new("RGB", (composite_width, composite_height), "white")

        offset = 0
        for image in resized_images:
            composite_image.paste(image, (offset, 0))
            offset += image.width

        self.image = composite_image.copy()
        self.tk_image = ImageTk.PhotoImage(self.image)
        image_width, image_height = self.image.size
        self.canvas.config(width=image_width, height=image_height, scrollregion=(0, 0, image_width, image_height))

        canvas_width = self.canvas.winfo_reqwidth()
        canvas_height = self.canvas.winfo_reqheight()
        x_position = (canvas_width - image_width) // 2
        y_position = (canvas_height - image_height) // 2

        self.image_id = self.canvas.create_image(x_position, y_position, anchor=tk.NW, image=self.tk_image)
        self.show_path_button.config(state=tk.NORMAL)

    def show_path(self):
        """
        Obtain the source and destination pixels from the graph, calculate the shortest path using BFS,
        and display the image with the drawn path.

        If a path is found, update the displayed image to show the path. Otherwise, show an error message.
        """
        # Obtain source and destination pixels from the graph based on the loaded image.
        source_pixel, destination_pixels = self.graph.build_graph(self.image_paths, self.max_floors)

        if not source_pixel or not destination_pixels:
            messagebox.showerror("Erro", f"Pixel de origem ou destino não foi encontrado.")
            return

        # Calculate the shortest path using the Dijkstra algorithm.
        path = self.graph.dijkstra(source_pixel, destination_pixels)

        if not path:
            messagebox.showerror("Erro", "Não há caminho possível.")
            return
        
        # Construct the output path for the drawn image.
        self.output_image_paths = [os.path.join(self.output_directory_path, f"possible_path_{os.path.basename(path)}")
            for path in self.image_paths
        ]
        
        # Draw the path on a new image.
        draw_path(path, self.image_paths, self.output_image_paths)

        # Display the composite image with drawn paths.
        self.original_images = [Image.open(image) for image in self.output_image_paths]
        self.display_images()

    def on_key_press(self, event):
        if event.keysym == "plus":
            self.zoom_in()
        elif event.keysym == "minus":
            self.zoom_out()

    def on_key_release(self, event):
        pass

    def on_drag_start(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        delta_x = event.x - self.start_x
        delta_y = event.y - self.start_y
        self.canvas.move(self.image_id, delta_x, delta_y)
        self.start_x = event.x
        self.start_y = event.y

    def on_drag_stop(self, event):
        pass
