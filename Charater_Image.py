from PIL import Image, ImageDraw
import time
start_time = time.time()

im = Image.open('1.jpg') # Can be many different formats.
pix = im.load()
x, y = im.size

downsample_ratio = 3
character_img = Image.new('RGBA', (int(10*(x/downsample_ratio+1)), int(10*(y/downsample_ratio+1))))
d = ImageDraw.Draw(character_img)
for i in range(0, x, downsample_ratio):
    for j in range(0, y, downsample_ratio):
        r , g, b = pix[i,j]
        average_val = (r + b + g)/3.0
        chr_mapping = int((26*average_val/255) + 63)
        d.text((int(10*i/downsample_ratio), int(10*j/downsample_ratio)), chr(chr_mapping), fill=(r,g,b, int(average_val)))
character_img.save('text 0.4.png')
print("--- %s seconds ---" % (time.time() - start_time))

