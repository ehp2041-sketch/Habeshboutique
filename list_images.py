import os

# ስእልታት ዘለዉዎ ቦታ
path = "assets/"
image_list = [f for f in os.listdir(path) if f.endswith(('.jpg', '.png', '.jpeg'))]

print("እዞም ስማት ኮፒ ጌርካ ኣብቲ ጃቫስክሪፕት (images array) ኣእትዎም፦")
print(image_list)
