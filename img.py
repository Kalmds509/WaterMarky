from msilib.schema import Directory
import os
from PIL import Image
sq_fit_size = 300
chemin2="C:\\Users\\Kalancia St Martin\\Pictures\\clin.png"
logo=Image.open(chemin2)
# l,h=img.size

l2=logo.resize((100,100))
directory="C:\\Users\\Kalancia St Martin\\Desktop\imaj"
for dir, dirs, files in os.walk(directory):
    for i in files:
        l=Image.open(i)
        l.paste(l2)
        
        

