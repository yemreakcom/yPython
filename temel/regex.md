---
description: Python regex kütüphanelerini kullanma
---

# 💎 Regex İşlemleri

## 📦 Faydalı Paketler

| Paket | Fonksiyon | Açıklama |
| :--- | :--- | :--- |
| `re` | `split(<ayırıcı_karakterler>, <string>)` | Birden fazla karaktere göre parçalama |

* `<ayırıcı_karakterler>` Metni hangi karakterlere göre böleceğimizi ifade eder
  * Birden fazla olacaksa `|` ile birbirinden ayrılır
  * Ayırma sırasında `boşluk karakteri`nin kullanılması sorun oluşturur
  * _Örn:_ `'\n|\t|\*'`
* `<string>` Ayrıştırılacak metin
  * _Örn:_ `'yemreak.com'`

## 👨‍💻 Renkleri Tersine Çevirme

```python
p6 = re.compile("#[0-9a-f]{6}", re.IGNORECASE)
p3 = re.compile("#[0-9a-f]{3}", re.IGNORECASE)

content = file(FILEPATH,'r').read()

def Modify (content):
    text = content.group().lower()
    code = {}
    l1="#0123456789abcdef"
    l2="#fedcba9876543210"
    for i in range(len(l1)):
        code[l1[i]]=l2[i]
    inverted = ""
    for j in text:
        inverted += code[j]
    return inverted

content = p6.sub(Modify,content)
content = p3.sub(Modify,content)
out = file(filepath,'w')
out.write(content)
out.close()
```

