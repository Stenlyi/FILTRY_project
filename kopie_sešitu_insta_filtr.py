from PIL import Image
obrazek = Image.open("earth.jpg")
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        obrazek.putpixel((x,y), (r , b, r))
        if prumer > 150:
            obrazek.putpixel((x,y), (255, 255, 255))
        else:
            obrazek.putpixel((x,y), (100, 75, 25))
        y += 1
    x += 1
display(obrazek) #obrazek.show()
