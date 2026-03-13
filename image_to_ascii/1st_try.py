from PIL import Image

img = Image.open("image.jpg")

# resize
new_width = 120
aspect_ratio = img.height / img.width
new_height = int(new_width * aspect_ratio * 0.5)
img = img.resize((new_width, new_height))

pixels = img.load()
width, height = img.size

ascii_chars = "`.:-=+*0#G%@"

with open("ascii_photo.txt", "w") as f:
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            brightness = (r + g + b) // 3

            index = brightness // (255//len(ascii_chars))
            f.write(ascii_chars[index-1])
        f.write("\n")
