from services import encode, decode, is_arp
from services.renderer import render_pixelgrid


def do(path):
  if is_arp(path):
    pixel_grid = decode(path)
    render_pixelgrid(pixel_grid)
  else:
    image_data = encode(path)
    with open(path + ".arp", "w") as f:
      f.write(image_data)
