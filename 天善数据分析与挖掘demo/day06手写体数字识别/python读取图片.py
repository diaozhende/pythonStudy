from PIL import Image
image = Image.open("C:/Users/diaozhende/Desktop/three.jpg")
fh = open("C:/Users/diaozhende/Desktop/three.txt", "a")
im_rotate = image.rotate(90)
im = im_rotate.transpose(Image.FLIP_TOP_BOTTOM)
width = im.size[0]
height = im.size[1]
print("width:"+str(width))
print("height:"+str(height))
for i in range(0, width):
    for j in range(0, height):
        cl = im.getpixel((i, j))
        clall = cl[0] + cl[1] + cl[2]
        if (clall == 0):
            # 黑色
            fh.write("1")
        else:
            fh.write("0")
    fh.write("\n")
fh.close()
