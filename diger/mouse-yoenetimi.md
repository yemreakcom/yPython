# 🖱️ Mouse Yönetimi

## 🔴 Tekrarlama

* 👂 Mouse eylemlerini dinler
* 🔄 Dinleme işlemi bittiği zaman tüm eylemleri aynı sırayla tekrarlar

```python
import mouse

# Sol tuşa basılana kadar kaydeder
events = mouse.record(button=mouse.RIGHT)
mouse.play(events)
```

## 👨‍💻 Gelişmiş Kaydetme

```python
import mouse
import time

mouse_events = []
mouse.hook(mouse_events.append)

time.sleep(5)

mouse.unhook(mouse_events.append)
mouse.play(mouse_events)

```
