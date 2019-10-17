# 👮‍ Kurallar ve Zaman İşlemleri

## 📏 Assertion (Kural Koyma)

Boolean değeri sağlanmazsa hata verir ve programı kapatır.

```python
assert <bool>, <açıklama>
```

- `<bool>` Kontrol değişkeni
  - _Örn: 0 > 5_
- `<açıklama>` Hatanın neden verildiğine dair metin
  - _Örn: Küçük bir değer girildi_

### 🌠 Assertion Örnekleri

```python
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
```

```sh
451
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print KelvinToFahrenheit(-5)
  File "test.py", line 4, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
```

## 🐞 Try / Except Yapısı

Olası hatalarda programın kapanmasını engelleyerek hata kontrolü sağlar.

```python
try:
    a = float("Ben sayı değilim")
except ValueError as err:
    print("Bu sayı değil", err)
```

## ⏱ Zaman İşlemlemleri (Time, Datetime)

```python
import time
from datetime import datetime

time.time() # Anlık süreyi saniye cinsinden verir
datetime.utcnow() # UTC formatında tarihi verir
datetime.now() # Yerel formatta tarihi verir (Türkiye)
datetime.now().strftime('%d-%b-%Y-%H:%M:%S') # Formatlı zaman bilgisi 26-Jun-2019-16:00:07
```

## 🙇‍ Program Kapandığında İşlem Yapma (on Exit)

```python
import atexit

def exit_handler():
    print 'My application is ending!'

atexit.register(exit_handler)
```

> [Doing something before program exit](https://stackoverflow.com/a/3850271/9770490)
