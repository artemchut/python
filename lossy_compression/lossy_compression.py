from PIL import Image

image = Image.open("image.jpg")
pixels = image.load()
width, height = image.size

length = 2 # 2x pixels and 2y pixels are being connected together into 1

new_image = Image.new("RGB", (width // length, height // length))
new_pixels = new_image.load()

new_x = 0
new_y = 0
for y in range(0, height-1, length):
    for x in range(0, width-1, length):
        r = g = b = 0
        # reading every 2x pixels and every 2 pixels (colours)
        r = pixels[x,y][0] + pixels[x+1,y][0] + pixels[x,y+1][0] + pixels[x+1,y+1][0]
        g = pixels[x,y][1] + pixels[x+1,y][1] + pixels[x,y+1][1] + pixels[x+1,y+1][1]
        b = pixels[x,y][2] + pixels[x+1,y][2] + pixels[x,y+1][2] + pixels[x+1,y+1][2]

        # finding the average of these 4 pixels
        avg = (r // (length*length), g // (length*length), b // (length*length))
        new_pixels[new_x, new_y] = avg
        new_x += 1
    new_x = 0
    new_y += 1

new_image.save("new_image.jpg")