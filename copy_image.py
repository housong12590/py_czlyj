import os
import shutil

root_dir = r'G:\code\android\cocos2dgame\app\src\main\assets\cocos2d-html5'
desc_dir = r'C:\Users\Administrator\Desktop\images'

img = ['.png', '.jpg', '.jpeg', '.gif']

for fpathe, dirs, fs in os.walk(root_dir):
    for f in fs:
        abs_path = os.path.join(fpathe, f)
        if os.path.isfile(abs_path) and os.path.splitext(abs_path)[1] in img:
            shutil.copy(abs_path, os.path.join(desc_dir, f))
            print(abs_path)
