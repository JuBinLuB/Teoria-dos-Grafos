from typing import Any, List, Tuple
from PIL import Image, ImageDraw
from colors import Color

def draw_path(path: List, image_paths: List[str], output_paths: List[str]) -> None:
  """
  Draw the specified path on the image and save the resulting image for each floor.

  Parameters:
  - path: List of coordinates representing the path to be drawn.
  - image_paths: List of file paths of the bitmap images.
  - output_paths: List of file paths to save the resulting images.
  - max_floors: The maximum number of floors in the building.

  Returns:
  - None
  """
  # Load the images and create drawing objects for each floor.
  original_images = [Image.open(image_path).convert("RGB") for image_path in image_paths]
  draws = [ImageDraw.Draw(image) for image in original_images]

  path_color = Color.BLUE

  # Draw the specified path on each floor's image.
  for x, y, z in path:
    pixel_color = original_images[z].getpixel((x, y))

    # Check if the pixel color is not a start or end color.
    if pixel_color not in [Color.RED, Color.GREEN]:
      draws[z].point((x, y), fill=path_color)

    # Save the resulting image with the drawn path.
    original_images[z].save(output_paths[z])
  