---
description: Python üzerinde threadler
---
# 🧵 Multithreading

##  ❔ Nedir

* 🚶‍♂️ Thread ile satır satır ilerleyen kod yerine karma ilerleyen kodlar yazılabilir.
* 📦 `threading` paketi kullanılır

| Class     | Açıklama                                  |
| --------- | ----------------------------------------- |
| Thread    | Sırasız olarak bir fonksiyonu çalıştırma  |
| Timer     | Belirli saniyelerde fonksiyonu çalıştırma |
| Scheduler | Bir plana göre fonksiyonu çalıştırma      |

{% hint style="warning" %}
📢 Python'da eş zamanlı işler multi-threading değil [🎎 Multiprocessing](multiprocessing.md) yapısı kullanılır.
{% endhint %}

## 🧱 Yapısı

```python
import threading

def ela(fname, orig_dir, save_dir):
    """
    Paremetreli bir fonksiyon
    """
    pass

dirc = "Dizin"
for d in os.listdir(dirc):
    if d.endswith(".jpg") or d.endswith(".jpeg"):
        thread = threading.Thread(target=ela, args=[d, dirc, ela_dirc])
        threads.append(thread)
        thread.start()

# Join edilmez ise, arka planda çalışır, print yazısından sonra bitebiebilir
# Join edilirse threadlerin tamamlanmasını beklemiş oluruz.
for t in threads:
    t.join()

print("Finished!")
```

## 💫 Tekrarlamalı

```python
from time import sleep
from threading import Thread

def tekrarla(ne, bekleme):
    while True:
        print ne
        sleep(bekleme)

if __name__ == '__main__':
    dum = Thread(target = tekrarla, args = ("dum",1))
    tis = Thread(target = tekrarla, args = ("tis",0.5))
    ah = Thread(target = tekrarla, args = ("ah",3))

    dum.start()
    tis.start()
    ah.start()
    
# dum
# tis
# ah

# tis
# dumtis

# tis
# dumtis

# tis
# ah
# tisdum
```

## ⏱ Zamanlayıcı

```python
import threading


def run_check():
    print("Fonksiyon çalıştı.")
    threading.Timer(5.0, run_check).start()


run_check()
```

## 🎌 Planlı Çalışan

```python
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print "Doing stuff..."
    # do your stuff
    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()
```

## 🔗 Faydalı Bağlantılar

* ****[Python: How can I run python functions in parallel?](https://stackoverflow.com/questions/7207309/python-how-can-i-run-python-functions-in-parallel)
* [Keyword argument verilerini threading ile kullanma](https://stackoverflow.com/a/32717920/9770490)
