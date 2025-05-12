
from PIL import Image
import os

def dummy_caption(image_path):
    return "portrait, high detail, person"

def tag_dataset_images(dataset_folder):
    tags = {}
    for file in os.listdir(dataset_folder):
        if file.lower().endswith(('.jpg', '.png')):
            tags[file] = dummy_caption(os.path.join(dataset_folder, file))
    return tags
