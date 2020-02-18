---
description: >-
  Python ile klavye ve mouse yönetimi (keyboard and mouse hooks), kısayol
  oluşturma, tuş basımı ve mouse tıklamaları
---

# ⌨️ Input Yönetimi

## 👀 Hızlı Bakış

* 🤖 Bilgisayarı işlemlerini otomatikleştirmeyi sağlar
* ✴️ Windows için `pynput` paketi kullanılır

## ⌨️ Klavye Yönetimi

* 👂 Dinleme işlemleri için `Listener` objesi kullanılır
* 👨‍💼 Yönetme işlemleri için `Controller` objesi kullanılır

```python
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Keyboard ~ pynput](https://pynput.readthedocs.io/en/latest/keyboard.html) alanına bakabilirsin.
{% endhint %}

## 💞 Hotkey Tanımlama

* ➕ Listener objesine `hotkey`'i tetikleyen metot eklenmesi gerekir
* 👮‍♂️ Hotkey'in tetiklenmesi `key` için `canonical` metodu ile kullanılmalıdır
* ❌ Eğer `canonical` olarak kullanılmazsa tuş kombinasyonlarını algılamaz

```python
from pynput import keyboard

def on_activate():
    print('Global hotkey activated!')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Keyboard ~ pynput](https://pynput.readthedocs.io/en/latest/keyboard.html) alanına bakabilirsin.
{% endhint %}

## 🖱 Mouse Yönetimi

* 👂 Dinleme işlemleri için `Listener` objesi kullanılır
* 👨‍💼 Yönetme işlemleri için `Controller` objesi kullanılır

```python
from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

# Set pointer position
mouse.position = (10, 20)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
mouse.move(5, -5)

# Press and release
mouse.press(Button.left)
mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on Mac OSX
mouse.click(Button.left, 2)

# Scroll two steps down
mouse.scroll(0, 2)
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Mouse ~ pynput](https://pynput.readthedocs.io/en/latest/mouse.html) alanına bakabilirsin.
{% endhint %}

## 🔗 Faydalı Bağlantılar

* [📖 pynput](https://pynput.readthedocs.io/en/latest/index.html)

