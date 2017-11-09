import os

base_path = os.path.join(os.getcwd(), 'image')
for image in os.listdir(base_path):
    if image.endswith('.gif'):
        os.remove(os.path.join(base_path, image))
