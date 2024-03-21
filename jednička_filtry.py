from PIL import Image
import random

def greeting_name(name):
    print(f"Ahoj {name}")

name = input("Zadej své jméno: ")
greeting_name(name)

print("Evidentně si chcete změnit filtr svého obrázku, pojďme do toho:")
print("Nejdříve si vyberte obrázek, u kterého chcete změnit filtr.")
print("Potom si vyberete filtr, který chcete na svůj obrázek dát.")

nazev_obrazku = input("Jméno obrázku (.png/.jpg): ")

while True:
    vyber_filtru = input("Filtr: (Černobílý/Zelený/Žlutý/Červený/Negativní/Random): ")

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

            elif vyber_filtru.lower() == "zelený":
                obrazek.putpixel((x,y), (0, 255, 0))
                
            elif vyber_filtru.lower() == "žlutý":
                obrazek.putpixel((x,y), (255, 255, 0))
                
            elif vyber_filtru.lower() == "červený":
                obrazek.putpixel((x,y), (255, 0, 0))

            elif vyber_filtru.lower() == "negativní":
                obrazek.putpixel((x,y), (255-r, 255-g, 255-b))
                
            elif vyber_filtru.lower() == "random":
                vyber_filtru = random.choice(["černobílý", "zelený", "žlutý", "červený", "negativní"])
                
            y += 1
        x += 1

    obrazek.show()
    print(f"{name}, zde je váš obrázek.")
    break 
else:
    print("Neznámý filtr. Použijte 'Černobílý', 'Zelený', 'Žlutý', 'Červený', 'Negativní' nebo 'Random'.")  
    continue
