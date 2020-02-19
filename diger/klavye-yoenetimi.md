---
description: >-
  Python ile klavye ve mouse yönetimi (keyboard and mouse hooks), kısayol
  oluşturma, tuş basımı ve mouse tıklamaları
---

# ⌨️ Klavye Yönetimi

## 💞 Kısayol Ekleme

* 👮‍♂️ `suppress` deyimi ile hotkey tetiklendiğinde tuş basımlarını göndermezsin

```python
print('Press and release your desired shortcut: ')
shortcut = keyboard.read_hotkey()
print('Shortcut selected:', shortcut)


def on_triggered():
    print("Triggered!")


keyboard.add_hotkey(shortcut, on_triggered, suppress=True)

print("Press ESC to stop.")
keyboard.wait('esc')

```

## 🔴 Tekrarlama

* 👂 Klavye eylemlerini dinler
* 🔄 Dinleme işlemi bittiği zaman tüm eylemleri aynı sırayla tekrarlar

```python
import keyboard
import time

keyboard.start_recording()

time.sleep(10)

events = keyboard.stop_recording()
keyboard.replay(events)

```

## 👁️ Tuş Basımlarını Algılama

```python
import keyboard
import sys
sys.path.append('..')


def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
    # '\r' and end='' overwrites the previous line.
    # ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
    print('\r' + line + ' '*40, end='')


keyboard.hook(print_pressed_keys)
keyboard.wait()

```

## 📜 Tuş Basımlarını Raporlama

```python
import sys
sys.path.append('..')

# Also available as just `python -m keyboard`.
from keyboard import __main__

# {"event_type": "down", "name": "a", "scan_code": 30, "time": 1491442622.6348252}
# {"event_type": "down", "name": "s", "scan_code": 31, "time": 1491442622.664881}
# {"event_type": "down", "name": "d", "scan_code": 32, "time": 1491442622.7148278}
# {"event_type": "down", "name": "f", "scan_code": 33, "time": 1491442622.7544951}
# {"event_type": "up", "name": "a", "scan_code": 30, "time": 1491442622.7748237}
# {"event_type": "up", "name": "s", "scan_code": 31, "time": 1491442622.825077}
# {"event_type": "up", "name": "d", "scan_code": 32, "time": 1491442622.8644736}
# {"event_type": "up", "name": "f", "scan_code": 33, "time": 1491442622.9056144}

```

## ✍ Verilen Yazıyı Tekrarlama

```python
import fileinput
import keyboard
import sys
sys.path.append('../')

for line in fileinput.input():
    keyboard.write(line)
```

## 🔗 Faydalı Bağlantılar

{% embed url="https://github.com/boppreh/keyboard" %}

