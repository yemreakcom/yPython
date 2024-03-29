---
description: Assert ile kural koyma yapısı
---
# 👮‍ Kural Koyma

## 🧱 Temel Kullanım

Boolean değeri sağlanmazsa hata verir ve programı kapatır.

```python
assert <bool>, <açıklama>
```

* `<bool>` Kontrol değişkeni
  * _Örn: 0 > 5_
* `<açıklama>` Hatanın neden verildiğine dair metin
  * _Örn: Küçük bir değer girildi_

**⭐ Örnek**

```python
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
```

**📋 Sonuç**

```python
451
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print KelvinToFahrenheit(-5)
  File "test.py", line 4, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
```

##
