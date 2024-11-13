from machine import Pin
import dht
import time


senzor = dht.DHT11(Pin(0))

while True:
    try:
        # Spuštění měření
        senzor.measure()

        # Čtení teploty a vlhkosti
        teplota = senzor.temperature()
        vlhkost = senzor.humidity()

        # Výstup na obrazovku
        print(f"Teplota: {teplota:.1f}°C  Vlhkost: {vlhkost:.1f}%")

    except OSError as e:
        # Ošetření chyb při čtení
        print(f"Chyba při čtení senzoru: {e}")

    # Počkejte 5 sekund před dalším měřením
    time.sleep(5)