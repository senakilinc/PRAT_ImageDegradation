import cv2
import os
from augraphy import *

def add_folding(input_image_path, output_image_path):
    """
    Adds subtle folding marks and creases to an image to simulate folded paper using augraphy library by python. This is a wrapper function for modularity purposes.
    Result is very artifical and not good, this is just for experiment purposes.
    """
    # Load input image and convert to float32
    img = cv2.imread(input_image_path)

    folding = Folding(fold_count=5,
                  fold_noise=0.0,
                  fold_angle_range = (-360,360),
                  gradient_width=(0.1, 0.2),
                  gradient_height=(0.01, 0.1),
                  backdrop_color = (0,0,0),
                  )

    img_folded= folding(img)

    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)
    cv2.imwrite(output_image_path, img_folded)
    print(f"Folding effect added and saved to: {output_image_path}")

