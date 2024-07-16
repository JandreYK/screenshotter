from PIL import ImageGrab
import os
import threading
from pynput import mouse
import time

# Pytania użytkownika na początku
ready_to_run = input("Czy jesteś gotowy, aby uruchomić skrypt printscreenowania? (Y/N): ")
if ready_to_run.lower() != 'y':
    exit()

output_folder = input("Wskaż folder, w którym będą zapisywane screeny: ")
screenshot_name_prefix = input("Jak nazwać tę grupę screenów? ")

# Sprawdź, czy folder istnieje, jeśli nie, to utwórz go
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# Funkcja do wykonania "print screen" i zapisu obrazu do pliku JPG
def take_screenshot_and_save():
    screenshot = ImageGrab.grab()  # Wykonaj "print screen"
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = os.path.join(output_folder, f"{screenshot_name_prefix}_{timestamp}.jpg")

    try:
        screenshot.save(filename, "JPEG")
        print(f"Zapisano screenshot jako {filename}")
    except Exception as e:
        print(f"Błąd podczas zapisu screenshotu: {e}")


# Funkcja do monitorowania lewego kliknięcia myszy
def on_click(x, y, button, pressed):
    if button == mouse.Button.left and pressed:
        take_screenshot_and_save()


# Uruchom wątek monitorowania myszy
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# Czekaj na zakończenie, można wpisać "END" w konsoli, aby zakończyć
end_input = input("Wpisz 'END' w konsoli, aby zakończyć skrypt: ")
if end_input.lower() == 'end':
    mouse_listener.stop()
