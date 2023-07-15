# Image-Processing

This project is just for educational, not supporting hacking!
Image processing with "python-imagesearch"

You can browse this library here: https://pypi.org/project/python-imagesearch/

The game url: https://gamesge.com/en/whack-a-mole/


# Image-Processing

This project is just for educational, not supporting hacking!
Image processing with "python-imagesearch"

You can browse this library here: https://pypi.org/project/python-imagesearch/

The game url: https://gamesge.com/en/whack-a-mole/

----

# Quick tutorial

* Import:
from python_imagesearch.imagesearch import imagesearch, imagesearcharea

- Imagesearch usage:
`imagesearch("<Image>")`

Example: `imagesearch("image.png")`

* imagesearcharea usage:
`imagesearcharea("<Image>", <x1 coordinate>, <y1 coordinate>, <x2 coordinate>, <y2 coordinate>)`

Example : `imagesearcharea("image.png", 100, 200, 1900, 1000)`

* Check is image in screen:

```
the_image = imagesearch("image.png")
if the_image[0] != -1:
    print("yes")
```

In this code `the_image[0]` mean is x coordinate of `the_image` if we type `the_image[1]` this mean is y coordinate of `the_image`.

```
print("X coordinate:", the_image[0])
print("Y coordinate:", the_image[1])
```

If image in screen x or y coordinates must be at least `0`. If image is not in screen x and y coordinates must be `-1`. So if x or y coordinate of image is not `-1`, image in screen!
