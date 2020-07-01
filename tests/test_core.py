import os

import pytest
import numpy as np

from eizou.core import rotate, mirror, inverse, bw, lighten, darken, sharpen


def test_rotate():
    image = np.identity(5)
    target = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    assert np.array_equal(rotate(image), target)

    image = np.arange(45).reshape(3, 5, 3)
    target = [
        [
            [12, 13, 14],
            [27, 28, 29],
            [42, 43, 44]
        ],

        [
            [9, 10, 11],
            [24, 25, 26],
            [39, 40, 41]
        ],
        [
            [6, 7, 8],
            [21, 22, 23],
            [36, 37, 38]
        ],

        [
            [3, 4, 5],
            [18, 19, 20],
            [33, 34, 35]
        ],

        [
            [0, 1, 2],
            [15, 16, 17],
            [30, 31, 32]
        ]
    ]
    assert np.array_equal(rotate(image), target)


def test_mirror():
    image = np.identity(5)
    target = [
        [0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    assert np.array_equal(mirror(image), target)

    image = np.arange(45).reshape(3, 5, 3)
    target = [
        [
            [12, 13, 14],
            [9, 10, 11],
            [6, 7, 8],
            [3, 4, 5],
            [0, 1, 2]
        ],

        [
            [27, 28, 29],
            [24, 25, 26],
            [21, 22, 23],
            [18, 19, 20],
            [15, 16, 17]
        ],

        [
            [42, 43, 44],
            [39, 40, 41],
            [36, 37, 38],
            [33, 34, 35],
            [30, 31, 32]
        ]
    ]
    assert np.array_equal(mirror(image), target)


def test_inverse():
    image = np.identity(5)
    target = np.full((5, 5), 255) - np.identity(5)
    assert np.array_equal(inverse(image), target)

    image = np.arange(45).reshape(3, 5, 3)
    target = np.full((3, 5, 3), 255) - np.arange(45).reshape(3, 5, 3)
    assert np.array_equal(inverse(image), target)


def test_bw():
    image = np.identity(5)
    target = np.identity(5)
    assert np.array_equal(bw(image), target)

    image = np.arange(45).reshape(3, 5, 3)
    target = [
        [0, 3, 6, 9, 12],
        [15, 18, 21, 24, 27],
        [30, 33, 36, 39, 42]
    ]
    assert np.array_equal(bw(image), target)

    image = np.arange(45).reshape(3, 5, 3) * 5
    target = [
        [4, 19, 34, 49, 64],
        [79, 94, 109, 124, 139],
        [154, 169, 184, 199, 214]
    ]
    assert np.array_equal(bw(image), target)


def test_lighten():
    image = np.identity(5)
    target = np.identity(5)
    assert np.array_equal(lighten(image, 0), target)

    image = np.identity(5)
    target = np.full((5, 5), 255)
    assert np.array_equal(lighten(image, 100), target)

    image = np.identity(5)
    target = np.identity(5) + 127
    assert np.array_equal(lighten(image, 50), target)


def test_darken():
    image = np.identity(5) * 255
    target = np.identity(5) * 255
    assert np.array_equal(darken(image, 0), target)

    image = np.identity(5) * 255
    target = np.zeros((5, 5))
    assert np.array_equal(darken(image, 100), target)

    image = np.identity(5) * 255
    target = np.identity(5) * 127
    assert np.array_equal(darken(image, 50), target)
