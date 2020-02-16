from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from sklearn.metrics import pairwise_distances_argmin
from services.logging import logger
import numpy as np


def _read_image(path):
    img = Image.open(path)
    pixel_map = img.load()
    logger.info(
        'the image read from path {} has following properties'.format(path))
    logger.info('size: {} x {}'.format(*img.size))
    logger.info('format: {}'.format(img.format))
    img.close()
    return img, pixel_map


def _get_quantized_image(img, pixel_map):
    w, h, d = img.size[0], img.size[1], len(pixel_map[0, 0])
    image_array = np.array(
        [pixel_map[i, j] for j in range(h) for i in range(w)],
        dtype=np.float64) / 255
    image_array_sample = shuffle(
        image_array, random_state=0)[:(len(image_array) * 1) // 100]
    kmeans = KMeans(n_clusters=256, random_state=0).fit(image_array_sample)
    labels = kmeans.predict(image_array)
    centers = kmeans.cluster_centers_

    new_data = np.zeros((h, w, d))
    label_idx = 0
    for j in range(h):
        for i in range(w):
            new_data[j][i] = centers[labels[label_idx]]
            label_idx += 1

    return new_data


def encode(path):
    img, pixel_map = _read_image(path)
    new_pixel_data = _get_quantized_image(img, pixel_map)

    buffer = bytearray()
    buffer.append(97)
    print(buffer.hex())

    return ""
