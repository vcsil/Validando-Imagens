# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:21:33 2021

@author: vinic
"""

import os
from PIL import Image
folder_path = ''
extensions = []
erros = []
for fldr in os.listdir(folder_path):
    sub_folder_path = os.path.join(folder_path, fldr)
    for filee in os.listdir(sub_folder_path):
        file_path = os.path.join(sub_folder_path, filee)
        print('** Path: {}  **'.format(file_path), end="\r", flush=True)
        #im = Image.open(file_path)
        try:
            im = Image.open(file_path)
        except:
            erros.append(file_path)
        rgb_im = im.convert('RGB')
        if filee.split('.')[1] not in extensions:
            extensions.append(filee.split('.')[1])
