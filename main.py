from PIL import Image

a = ['@', '#', '$', '%', '&', '?', '*', 'o', '/', '{', '[', '(', '|', '!', '^', '~', '-', '_', ':', ';', ',', '.',
     '`', '']
count = len(a)


def text(image_file):
    asd = ''
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            r, g, b = image_file.getpixel((w, h))
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            asd = asd + a[int(gray / (255 / (count - 1)))]
        asd = asd + '\r\n'
    return asd


Image_file = Image.open("test.jpg")
Image_file = Image_file.resize((int(Image_file.size[0] * 0.9), int(Image_file.size[1] * 0.35)))
# *print(text(Image_file))
tmp = open('test.txt', 'a')
tmp.write(text(Image_file))
tmp.close()
