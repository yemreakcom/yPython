---
description: Python regex kütüphanelerini kullanma
---
# 💎 Regex İşlemleri

## 📦 Regex Paketi `re` Kullanımı

| Fonksiyon                                    | Açıklama                              |
| -------------------------------------------- | ------------------------------------- |
| `split(<regex>, <string>)`                   | Birden fazla karaktere göre parçalama |
| `sub(<regex>, <replace \| metot>, <string>)` | Regex'e göre metinleri değiştirme     |
| `compile(<regex>, <?flag>)`                  | Regex objesi oluşturma                |

{% hint style="info" %}
‍🧙‍♂ Regex objesi oluşturulduğunda tekrar tekrar `regex` tanımlaya gerek yoktur
{% endhint %}

## 💠 Regex için Metot Oluşturma

```python
color_regex = re.compile("#([0-9a-fA-F]{6,8})", re.IGNORECASE)

def my_method(content):
    text = content.group().lower()

content = color_regex.sub(my_method, content)
```

## 🔍 Arama İşlemleri

```python
result = re.search(r"\[([^\[]+)\]\((.*)\)", "- [name](url)")
result[0] # '[name](url)'
result[1] # 'name'
result[2] # 'url'
```

## 👨‍💻 Renkleri Tersine Çevirme

```python
FILE_PATH = "Buraya kendi yolunu yaz"

def invertHex(hexNumber):
    # invert a hex number
    inverse = hex(abs(int(hexNumber, 16) - 255))[2:]
    # if the number is a single digit add a preceding zero
    if len(inverse) == 1:
        inverse = '0'+inverse
    return inverse

def colorInvert(hexCode):
    # define an empty string for our new colour code
    inverse = ""
    # if the code is RGB
    if len(hexCode) == 6:
        R = hexCode[:2]
        G = hexCode[2:4]
        B = hexCode[4:]
    # if the code is ARGB
    elif len(hexCode) == 8:
        A = hexCode[:2]
        R = hexCode[2:4]
        G = hexCode[4:6]
        B = hexCode[6:]
        # don't invert the alpha channel
        inverse = inverse + A
    else:
        # do nothing if it is neither length
        return hexCode
    inverse = inverse + invertHex(R)
    inverse = inverse + invertHex(G)
    inverse = inverse + invertHex(B)
    return inverse

def replaceHex(matchobj):
    # exclude the preceding hash symbol of the matched object
    hexCode = matchobj.group(0)[1:]
    # invert the colour code and return with the hash
    return '#' + colorInvert(hexCode)

filestr = ""
with open(FILE_PATH, "r", encoding="utf-8") as file:
    filestr = file.read()

invertedFile = re.sub('#([0-9a-fA-F]{6,8})', replaceHex, filestr)
```
