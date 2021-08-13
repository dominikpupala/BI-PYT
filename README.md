# BI-PYT
Final project in python course

# Eizou - CLI image editor

Simple CLI image editor, that is controlled by sequence of argument flags. Eizou requires both input file and destination file, the sequence of argument flags can consist of following (in any order and count):

* `--rotate`           rotates the image by 90 degrees to the right
* `--mirror`           flips the image horizontaly
* `--inverse`          creates negative of the image
* `--bw`               creates grayscale of the image
* `--lighten` [0-100]  lightens the image
* `--darken` [0-100]   darkens the image
* `--sharpen`          sharpens the image
* `--blur`             blurs the image
* `--edges`            enhances edges of the image

**Usage**

To run Eizou in shell: `./eizou.py [SEQUENCE_OF_FLAGS] INPUT_FILE OUTPUT_FILE`.

## Example usage

* `./eizou.py --sharpen espionage.png espionage.png`
* `./eizou.py --rotate --rotate australian_meme.png normal_meme.png`
* `./eizou.py --darken 35 --blur my_ugly_selfie.png new_profile_pic.png`
* `./eizou.py --lighten 13 --bw female_instagram_influencer.png vintage_playboy_pic.png`
* `./eizou.py --rotate --mirror --inverse --bw --lighten 13 --darken 17 --sharpen --blur --edges normie_meme.jpg edgy_meme.png`
