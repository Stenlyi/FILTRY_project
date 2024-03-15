from PIL import Image
name=input("Zadej své jméno:")
def greeting_name(name):
    print(f"Ahoj {name}")

print("Evidentně si chcete změnit filtr svého obrázku, pojďme do toho:")
print("Nejdříve si vyberte obrázek, u kterého chcete změnit filtr.")
print("Potom si vyberete filtr, který chcete na svůj obrázek dát.")

nazev_obrazku = input("Jméno obrázku (.png/.jpg): ")
vyber_filtru = input("Filtr: (Černobílý/Mono/Negativní/Sepia/Random): ")

obrazek = Image.open(nazev_obrazku)

sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        if vyber_filtru.lower() == "černobílý":
            if prumer > 150:
                obrazek.putpixel((x,y), (255, 255, 255))  
            else:
                obrazek.putpixel((x,y), (0, 0, 0))  

        elif vyber_filtru.lower() == "mono":
            if prumer > 150:
                obrazek.putpixel((x,y), (255, 255, 255))
            else:
                obrazek.putpixel((x,y), (0, 0, 0))
        elif vyber_filtru.lower() == "negativní":
            if prumer > 150:
                obrazek.putpixel((x,y), (255-r, 255-g, 255-b))
            else:
                obrazek.putpixel((x,y), (0, 0, 0))  
        elif vyber_filtru.lower() == "random":
            
            pass
        else:
            print("Neznámý filtr. Použijte 'Černobílý', 'Mono', 'Negativní', 'Sepia', 'Zářivý' nebo 'Random'.")
            obrazek = None
            break
        y += 1
    x += 1

if obrazek:
    obrazek.show()
