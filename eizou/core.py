import numpy as np

from PIL import Image

sharpening_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0],
])

blur_kernel = (1 / 256) * np.array([
    [1, 4, 6, 4, 1],
    [4, 16, 24, 16, 4],
    [6, 24, 36, 24, 6],
    [4, 16, 24, 16, 4],
    [1, 4, 6, 4, 1],
])

edge_kernel = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1],
])


def load_image(file_name: str) -> np.array:
    return np.asarray(Image.open(file_name), dtype=np.uint8)


def save_image(image, file_path: str, mode='RGB'):
    Image.fromarray(image, mode=mode).save(file_path)


def rotate(image: np.array) -> np.array:
    return np.rot90(image).astype(np.uint8)


def mirror(image: np.array) -> np.array:
    return np.fliplr(image).astype(np.uint8)


def inverse(image: np.array) -> np.array:
    return (255 - image).astype(np.uint8)


def bw(image: np.array) -> np.array:
    return ((np.average(image, weights=[0.299, 0.587, 0.114], axis=-1).astype(np.uint8))
        if image.ndim == 3
        else image.astype(np.uint8))


def lighten(image: np.array, scale: int) -> np.array:
    return (
        np.clip(image + (scale / 100) * (255 - image), 0, 255)
        .astype(np.uint8))


def darken(image: np.array, scale: int) -> np.array:
    return (
        np.clip(image - (scale / 100) * image, 0, 255)
        .astype(np.uint8))


def sharpen(image: np.array) -> np.array:
    return apply_filter(image, sharpening_kernel)


def blur(image: np.array) -> np.array:
    return apply_filter(image, blur_kernel)


def edges(image: np.array) -> np.array:
    return apply_filter(image, edge_kernel)


def apply_filter(image: np.array, kernel: np.array) -> np.array:
    return (
        apply_filter_rgb(image, kernel)
        if image.ndim == 3
        else apply_filter_grayscale(image, kernel))


def apply_filter_grayscale(image: np.array, kernel: np.array) -> np.array:
    h, w = image.shape[: 2]
    k = kernel.shape[0]
    o = (k - 1) // 2

    # zero padding
    temp = np.zeros([h + o * 2, w + o * 2])
    temp[o:h + o, o:w + o] = image

    # output array
    output = np.zeros((w, h))

    for j in range(h):
        for i in range(w):
            output[j, i] = (temp[j:j + k, i:i + k] * kernel).sum()

    return np.clip(output, 0, 255).astype(np.uint8)


def apply_filter_rgb(image: np.array, kernel: np.array) -> np.array:
    h, w = image.shape[: 2]
    k = kernel.shape[0]
    o = (k - 1) // 2

    # zero padding
    temp = np.zeros((h + o * 2, w + o * 2, 3))
    temp[o:h+o, o:w+o, 0:3] = image

    # output array
    output = np.zeros((w, h, 3))

    for c in range(3):
        for j in range(h):
            for i in range(w):
                output[j, i, c] = (temp[j:j + k, i:i + k, c] * kernel).sum()

    return np.clip(output, 0, 255).astype(np.uint8)
