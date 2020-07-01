#!/usr/bin/env python3

import os
import sys
import argparse
import core as ez

# dictionary of functions (kinda scuffed but I don't want to use reflection)
functions = {
    "--rotate": ez.rotate,
    "--mirror": ez.mirror,
    "--inverse": ez.inverse,
    "--bw": ez.bw,
    "--lighten": ez.lighten,
    "--darken": ez.darken,
    "--sharpen": ez.sharpen,
    "--blur": ez.blur,
    "--edges": ez.edges
}

parser = argparse.ArgumentParser(
    description="Eizou - CLI image editor",
    epilog="Created by Dominik Pupala")

# positional arguments
parser.add_argument(
    "input_file", metavar="input-file", type=str,
    help="path to the input image")
parser.add_argument(
    "output_file", metavar="output-file", type=str,
    help="path to the output image")

# optional arguments
parser.add_argument(
    "--rotate", action="store_true",
    help="rotates the image by 90 degrees to the right")
parser.add_argument(
    "--mirror", action="store_true",
    help="flips the image horizontaly")
parser.add_argument(
    "--inverse", action="store_true",
    help="creates negative of the image")
parser.add_argument(
    "--bw", action="store_true",
    help="creates grayscale of the image")
parser.add_argument(
    "--lighten", type=int, choices=range(0, 101), metavar="[0-100]",
    help="lightens the image")
parser.add_argument(
    "--darken", type=int, choices=range(0, 101), metavar="[0-100]",
    help="darkens the image")
parser.add_argument(
    "--sharpen", action="store_true",
    help="sharpens the image")
parser.add_argument(
    "--blur", action="store_true",
    help="blurs the image")
parser.add_argument(
    "--edges", action="store_true",
    help="enhances edges of the image")

args = parser.parse_args()

# argparse filetype seems weird when using the same io files
if not os.access(args.input_file, os.R_OK):
    print("Cannot access input file!")
    exit()

image = ez.load_image(args.input_file)

if image.ndim not in [2, 3]:
    print("Invalid input file!")
    exit()

mode = "RGB" if image.ndim == 3 else "L"

# perhaps implementing custom Namespace object that stores
# count and order of the arguments would be a better choice
while sys.argv:
    item = sys.argv.pop(0)

    if item not in functions:
        continue

    mode = (
        mode
        if item != "--bw"
        else "L")
    image = (
        functions[item](image)
        if item != "--lighten" and item != "--darken"
        else functions[item](image, int(sys.argv.pop(0))))

ez.save_image(image, args.output_file, mode=mode)
