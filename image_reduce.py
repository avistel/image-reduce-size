from PIL import Image

im = Image.open('1500-1204.jpg')
im.save('1500-1204-slim.jpg', optimize=True, quality=25)