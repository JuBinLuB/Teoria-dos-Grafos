import tkinter
from interface import ImageViewer

def main():
    # Creating window.
    window = tkinter.Tk()

    window.title("Image Viewer App")
    app = ImageViewer(master=window)

    # Run the Tkinter event loop
    app.mainloop()

if __name__ == "__main__":
    main()
