# 👮‍ Kural Koyma

## 📏 Assertion

Boolean değeri sağlanmazsa hata verir ve programı kapatır.

{% tabs %}
{% tab title="✨ Kullanım" %}
```python
assert <bool>, <açıklama>
```

* `<bool>` Kontrol değişkeni
  * _Örn: 0 &gt; 5_
* `<açıklama>` Hatanın neden verildiğine dair metin
  * _Örn: Küçük bir değer girildi_
{% endtab %}

{% tab title="⭐ Örnek" %}
```python
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
```
{% endtab %}

{% tab title="📋 Örnek Çıktısı" %}
```python
451
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print KelvinToFahrenheit(-5)
  File "test.py", line 4, in KelvinToFahrenheit
    assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!
```
{% endtab %}
{% endtabs %}

## 🐛 Try / Except Yapısı

Olası hatalarda programın kapanmasını engelleyerek hata kontrolü sağlar.

```python
try:
    a = float("Ben sayı değilim")
except ValueError as err:
    print("Bu sayı değil", err)
```

## 

