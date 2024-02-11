from PIL import Image # python3 -m pip install Pillow

import os

downloadsFolder = "/home/alejandro_lopez/Descargas"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(os.path.join(downloadsFolder, filename))
            picture.save(os.path.join(downloadsFolder + "compressed_"+filename), optimize=True, quality=60)