import os
import shutil
import sys

sys.setrecursionlimit(1000000)

root_path = r'C:\Users\czlyj\Desktop\Assets.xcassets'

new_path = r"C:\Users\czlyj\Desktop\image"

fl = []


def dirlist(path, allfile):
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        elif filepath.endswith(r'@3x.png'):
            allfile.append(filepath)
            newpath = os.path.join(new_path, filename)
            shutil.copyfile(filepath, newpath)
    return allfile


dirlist(root_path, fl)

print('copy 完成...')
