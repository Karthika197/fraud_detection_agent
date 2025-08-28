# detector.py

import random

class ViolationDetector:
    def __init__(self, model=None):
        self.model = model  # placeholder for future model loading

    def run(self, images):
        flagged = []

        for idx, img in enumerate(images):
            # Simulate detection: randomly flag some images
            if random.random() > 0.6:
                flagged.append({
                    "image_id": idx,
                    "violation": "Unclean surface detected",
                    "confidence": round(random.uniform(0.7, 0.95), 2)
                })

        return flagged
