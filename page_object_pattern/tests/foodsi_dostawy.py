import os
import time
from PIL import Image
import pytesseract
import random
import re

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\kstyczynski\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# miejsca ceny
PRICE1 = (820, 1140)
PRICE2 = (820, 1900)

# miejsca kliknięcia kart
CARD1 = (540, 1050)
CARD2 = (540, 1800)


def refresh():
    os.system("adb shell input swipe 540 400 540 1800 400")


def screenshot():
    os.system("adb exec-out screencap -p > screen.png")


def screenshot2():
    os.system("adb exec-out screencap -p > screen_2_dostawy.png")


def read_price(x, y):
    img = Image.open("screen.png")

    crop = img.crop((x - 120, y - 50, x + 120, y + 50))

    text = pytesseract.image_to_string(crop)

    return text


def parse_price(text):
    text = text.replace(",", ".")
    match = re.search(r"\d+(\.\d+)?", text)

    if match:
        return float(match.group())
    return None


def is_good_price(text):
    price = parse_price(text)

    if price is None:
        return False

    print("wykryta cena:", price)

    return price < 35


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

    if is_good_price(p1):
        print("cena < 35 na pozycji 1 → klik")
        tap(*CARD1)
        play_alarm()
        screenshot2()
        break

    if is_good_price(p2):
        print("cena < 35 na pozycji 2 → klik")
        tap(*CARD2)
        play_alarm()
        screenshot2()
        break

    print("brak dobrej paczki")

    counter += 1
    print("próba:", counter)


    x = random.randint(500, 700) / 100
    print("czekam " + str(x) + " sekund")
    print("-------------------------------")
    time.sleep(x)