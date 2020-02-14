from PIL import Image
from services.logging import logger


def _read_image(path):
  img = Image.open(path)
  pixel_map = img.load()
  logger.info('the image read from path {} has following properties'.format(path))
  logger.info('size: {} x {}'.format(*img.size))
  logger.info('format: {}'.format(img.format))
  img.close()
  return img, pixel_map


def _get_top_256(pixel_map):
  return []


def encode(path):
  img, pixel_map = _read_image(path)
  print(_get_top_256(pixel_map))
  return ""
