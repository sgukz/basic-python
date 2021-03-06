#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from skimage import io
from PIL import ImageFont, ImageDraw, Image

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

row,col,dim = 515,515,3
img = np.zeros((row,col,dim), np.uint8)

text = u'โอฬาริก'
b,g,r,a = 0,255,0,0

fontpath = 'THSarabunNew BoldItalic.ttf'
font = ImageFont.truetype(fontpath, 100)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((120,120), text, font = font, fill = (b,g,r,a))
img = np.array(img_pil)

io.imshow(img)
io.show()

'''
=============================
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :


'''