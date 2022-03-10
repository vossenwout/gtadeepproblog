import os
import shutil

src = "60.png"
for i in range(80,100):
    dst = str(i) + ".png"
    shutil.copyfile(src, dst)


