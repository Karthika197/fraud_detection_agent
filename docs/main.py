# main.py

# basic imports
import os
from agents.image_collector import ImageCollector
from agents.detector import ViolationDetector
from agents.notifier import AlertNotifier

# create folders if they don't exist
def init_dirs():
    for folder in ["logs", "data/raw_images", "data/violations"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

# main pipeline
def main():
    print("Starting pipeline...")

    # image collection
    collector = ImageCollector(source="cctv_feed_or_api")
    images = collector.get_images()

    # violation detection
    detector = ViolationDetector(model="models/violation_model.pt")
    flagged = detector.run(images)

    # alerting
    notifier = AlertNotifier(role="health_officer")
    notifier.push(flagged)

    print("Done.")

if __name__ == "__main__":
    init_dirs()
    main()
