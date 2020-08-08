#!/usr/bin/env python3

import os
from PIL import Image

size = (128,128)

for image in os.listdir("."):
  if not image.endswith(".py") and not image.endswith(".DS_Store"):
    img= Image.open(image).convert("RGB")
    img.rotate(270)
    img.thumbnail(size)
    new_name=os.path.basename(image)
    img.save("/opt/icons/{}".format(new_name),"jpeg")
    img.close()
   else:
    continue
