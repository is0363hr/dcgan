
# -*- coding: utf-8 -*-
import os
import glob
from PIL import Image

files = glob.glob('crop/*.jpg')
a = 0
for f in files:
    a = a+1
    img = Image.open(f)
    img_resize = img.resize((96, 96))  # 画像のサイズの指定
    ftitle, fext = os.path.splitext(f)
    img_resize.save('train_data/idole/' + str(a) + '_(96)' + fext)
