# 💎 Operatörler

## 🔢 Aritmetik Operatörler

{% tabs %}
{% tab title="🧱 Temel" %}
| Operatör | Açıklama |
| :--- | :--- |
| `+, -, /, *` | 4 işlem |
| `=` | Atama işlemi |
| `a, b = c, d` | Tek satırda çoklu atama |
| `+=, -=, /=, *=` | Kendisiyle işleme sokup kendisine atama |
| `<operatör>=` | Kendisiyle işleme sokup kendisine atama |
| `( )` | Parantej ile öncelik belirleme |

> `<operatör>` herhangi bir operatörü temsil eder.
{% endtab %}

{% tab title="🌍 Diğerleri" %}
| Operatör | Açıklama | Örnek | Çıktı |
| :--- | :--- | :--- | :--- |
| `%` | Mod alma işlemi | `6 % 2` | `0` |
| `**` | Kuvvet alma | `6 ** 2` | `36` |
| `//` | Kalansız bölümü alma | `13 // 2` | `6` |
{% endtab %}
{% endtabs %}

## 🔛 Karşılaştırma Operatörleri

| Operatör | Açıklama | Örnek | Çıktı |
| :--- | :--- | :--- | :--- |
| `>` | Büyük | `3 > 2` | `True` |
| `<` | Küçük | `3 < 2` | `False` |
| `==` | Eşit | `3 == 3` | `True` |
| `!=` | Eşit değil | `2 != 2` | `False` |
| `>=` | Büyük eşit | `2 >= 5` | `False` |
| `<=` | Küçük eşit | `2 <= 2` | `True` |

## 🤔 Mantıksal Operatörler

{% tabs %}
{% tab title="🧱 Temel" %}
| Operatör | Açıklama | Örnek | Çıktı |
| :--- | :--- | :--- | :--- |
| `and` | Ve işlemi | `True and False` | `False` |
| `or` | Veya işlemi | `False or True` | `True` |
| `not` | Değili | `not False` | `True` |
{% endtab %}

{% tab title="🅾 Bit Düzeyinde" %}
| Operatör | Açıklama | Örnek |  |  |
| :--- | :--- | :--- | :--- | :--- |
| `&` | Ve | `x & y = 0 (0000 0000)` |  |  |
| \` | \` | Veya | \`x | y = 14 \(0000 1110\)\` |
| `~` | Değili | `~ x = -11 (1111 0101)` |  |  |
| `^` | XOR | `x ^ y = 14 (0000 1110)` |  |  |
| `>>` | Sağa kaydırma | `x >> 2 = 2 (0000 0010)` |  |  |
| `<<` | Sola kaydırma | `x << 2 = 40 (0010 1000)` |  |  |
{% endtab %}
{% endtabs %}

## 🆔 Kimlik Belirleme

{% tabs %}
{% tab title="💎 Operatörler" %}
| Operatör | Açıklama | Örnek | Çıktı |
| :--- | :--- | :--- | :--- |
| `is` | Aynı objeye işaret etme | `[1, 2, 3] and [1, 2, 3]` | `False` |
| `is not` | Farklı objeye işaret etme | `1 is not 1` | `False` |

{% hint style="warning" %}
Ek değişkenlerde objelerin adresleri farklı olduğunda ilk çıktı `False` olur.
{% endhint %}
{% endtab %}

{% tab title="⭐ Örnek" %}
```python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
```
{% endtab %}
{% endtabs %}

## 🏠 Üyelik Belirleme

{% tabs %}
{% tab title="💎 Operatörler" %}
| Operatör | Açıklama | Örnek | Çıktı |
| :--- | :--- | :--- | :--- |
| `in` | Anahtar var | `5 in x` | `False` |
| `not in` | Anahtar yok | `1 not in x` | `False` |

> `x = [1, 2, 3, 4]`
{% endtab %}

{% tab title="⭐ Örnek" %}
```python
x = 'Hello world'
y = {1:'a',2:'b'}

print('H' in x) # True
print('hello' not in x) # True (h'si büyük değil)
print(1 in y) # True
print('a' in y) # False ('a' bir değerdir anahtar değildir)
```
{% endtab %}
{% endtabs %}

