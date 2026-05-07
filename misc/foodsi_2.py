import os
import time
from PIL import Image
import pytesseract
import random

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kstyczynski\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# miejsca ceny
PRICE1 = (810, 890)
PRICE2 = (820, 1650)

# miejsca kliknięcia kart
CARD1 = (540, 900)
CARD2 = (540, 1400)

# miejsca gdzie pojawia się napis "NIEDOSTĘPNE"
STATUS1 = (260, 700)
STATUS2 = (260, 1460)


def refresh():
    os.system("adb shell input swipe 540 600 540 1200 300")


def screenshot():
    os.system("adb exec-out screencap -p > screen.png")


def screenshot2():
    os.system("adb exec-out screencap -p > screen2.png")


def read_price(x, y):
    img = Image.open("screen.png")

    crop = img.crop((x - 120, y - 50, x + 120, y + 50))

    text = pytesseract.image_to_string(crop)

    return text


def is_available(x, y):
    img = Image.open("screen.png")

    pixel = img.getpixel((x, y))
    r, g, b = pixel[:3]

    # jeśli piksel jest ciemny → jest napis "NIEDOSTĘPNE"
    if r < 100 and g < 100 and b < 100:
        return False

    return True


def play_alarm():
    os.system("start alarm.mp3")


def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")


counter = 0

while True:

    print("refresh")
    refresh()

    time.sleep(1)

    screenshot()

    p1 = read_price(*PRICE1)
    p2 = read_price(*PRICE2)

    if "34" in p1 and is_available(*STATUS1):
        print("34,99 na pozycji 1 → klik")
        tap(*CARD1)
        play_alarm()
        screenshot2()
        break

    # if "34" in p2 and is_available(*STATUS2):
    #     print("34,99 na pozycji 2 → klik")
    #     tap(*CARD2)
    #     play_alarm()
    #     screenshot2()
    #     break

    print("brak dobrej paczki")

    counter += 1
    print("próba:", counter)
    print("-------------------------------")
    x = random.randint(500, 700) / 100
    print("czekam " + str(x) + " sekund")
    time.sleep(x)
