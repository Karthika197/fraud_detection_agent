# image_collector.py

import os
import random
import cv2

class ImageCollector:
    def __init__(self, source=None):
        self.source = source

    def get_images(self):
        # Simulate image collection from a folder
        image_folder = "data/raw_images"
        image_list = []

        for filename in os.listdir(image_folder):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                path = os.path.join(image_folder, filename)
                img = cv2.imread(path)
                if img is not None:
                    image_list.append(img)

        # If no images found, simulate with random noise
        if not image_list:
            print("No images found. Generating synthetic ones...")
            for _ in range(5):
                img = (255 * random.random()) * np.ones((256, 256, 3), dtype=np.uint8)
                image_list.append(img)

        return image_list
