import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here

    if not isinstance(image, list) or len(image) == 0:
        return -1

    gray_img = []

    for row in image:
        if not isinstance(row, list) or len(row) == 0:
            return -1
        row_buf = []
        for pixel in row:
            if not isinstance(pixel, list) or len(pixel) != 3:
                return -1
            gray_px = 0
            for i, channel in enumerate(pixel):
                if channel > 255 or channel < 0:
                    return -1
                lum = 0
                match i:
                    case 0: lum = .299
                    case 1: lum = .587
                    case 2: lum = .114
                gray_px += channel * lum
            row_buf.append(round(gray_px))
        gray_img.append(row_buf)

    return gray_img

    pass