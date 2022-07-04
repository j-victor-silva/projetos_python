import os


for root, dirs, files in os.walk('E:\\Downloads'):
    for file in files:
        print(dirs)
