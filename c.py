import os
from PIL import Image
sq_fit_size = 300
logo_file ="clin.png"
logoIm = Image.open(logo_file)
logoWidth, logoHeight = logoIm.size

p=input("Antre non dosye an: ")
if os.path.isdir(p):
    print("Ok")
else:
    print("No")
os.makedirs("withLogo", exist_ok = True)
for filename in os.listdir("C:\Users\Kalancia St Martin\Desktop\Projet_Watermarky"):
    print(filename)
    if not (filename.endswith(".png") or filename.endswith(".jpg")) or filename == logo_file:
        continue
    im = Image.open(filename)
    width, height = im.size

if width > sq_fit_size and height > sq_fit_size:
    if width > height:
        height = int((sq_fit_size / width) * height)
    width = sq_fit_size
else:
    width = int((sq_fit_size / height) * width)
    height = sq_fit_size

print("Resizing %s"% (filename))
im = im.resize((width, height))
im.paste(logoIm)
im.save(os.path.join("withLogo", filename))
