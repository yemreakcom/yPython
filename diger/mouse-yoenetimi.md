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

