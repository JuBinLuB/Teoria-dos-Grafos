from PIL import Image

def draw_path(path: list, image_name: str) -> None:
    """
    Draw the specified path on the image and save the resulting image.

    Parameters:
    - path: List of coordinates representing the path to be drawn.
    - image_name: The name of the image file to be read and modified.

    Returns:
    - None
    """
    image = Image.open(image_name).convert("RGB")
    pixels = image.load()
    for v in path:
      x, y = v
      pixels[x, y] = (0, 0, 255)
    # Save the resulting image with the drawn path.
    image.save("E:\Pandora's Box\Documents\Faculdade\Teoria dos Grafos\Trabalho Prático 01\Datasets\possible_path.bmp")
    