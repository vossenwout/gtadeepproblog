import os
import shutil

src = "0.png"
for i in range(1,10):
    dst = str(i) + ".png"
    shutil.copyfile(src, dst)


