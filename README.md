# Remove Background, Center, And Resize

This is a python script which removes the backgrounds from images,
centers the image, and then resizes the image to a square. I made this
to automate [Juliet Siegel's](https://www.tiktok.com/@julietsiegel)
workflow when making filters in
[EffectHouse](https://effecthouse.tiktok.com/).


## Usage

```
./filter.py <desired-resolution> <input-folder> <output-folder>
```

## Output Quality.

When formatting ~700 images during the creation of one of Juliet's
outfit filters, this tool succesfully converted about 600/700 with an
acceptable quality. It struggled on images where:
- the subject contained similar colors to the background
- the subject is very thin or stringy (for example, if the subject of
  the image is a necklace or wristband).
This script was cobbled together in a few hours using off-the-shelf libraries. No ML tool is perfect.
