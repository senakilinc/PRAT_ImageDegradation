import cv2
import os
from augraphy import *

def ink_bleed(img, intensity_range=(0.4, 0.7)):
    """
    Adds subtle ink bleed to an image to simulate folded paper using augraphy library by python. This is a wrapper function for modularity purposes.

    """
    # Load input image and convert to float32

    inkbleed = InkBleed(intensity_range,
                    kernel_size=(5, 5),
                    severity=(0.2, 0.4)
                        )

    img_inkbleed = inkbleed(img)

    #os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    #cv2.imwrite(output_image_path, img_inkbleed)
    #print(f"Folding effect added and saved to: {output_image_path}")
    return img_inkbleed

