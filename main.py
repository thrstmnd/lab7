from PIL import Image, ImageFilter
def zadacha1():
    a = "dog.jpg"
    with Image.open(a) as jpg:
        jpg.load()
    jpg.show()
    w, h = jpg.size
    format = jpg.format
    zvet = jpg.mode
    print(w, h, format, zvet)

def zadacha2():
    a = 'dog.jpg'
    with Image.open(a) as jpg:
        jpg.load()
    neww=jpg.width //3
    newh=jpg.height //3
    newjpg = jpg.resize(neww, newh)
    newjpg.save('dog2.jpg')

def zadacha3():
    for i in range(1, 6):
        i = str(i)
        jpg = Image.open(i + '.jpg')
        jpg = jpg.filter(ImageFilter.SHARPEN)
        jpg.save("C:\Users\user\PycharmProjects\lab7\image" + i + ".jpg")

def zadacha4():
    jpg = Image.open('1.jpg')
    png = Image.open('water.png')
    jpg.paste(png, (300,230))
    jpg.save('zadacha4.jpg')