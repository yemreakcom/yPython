---
description: Yüksek sayıdaki verileri daha anlaşılır hale getirme
---

# 📊 Verileri Kategorize Etme

## 🔰 Bilinmesi Gerekenler

Çok yüksek veriler ile başa çıkmak zordur.

* Kategorize işlemleri için birebir aynı metin aranmaz
* `Fuzzy Match` olan yöntem ile çok benzeyen metinler aynı gruba alınır

## 🥴 Fuzzy Match

Kelimelerin birbirine çok yakın olanlarını bulur.

```python
def fuzzy_match(word, s):
    words = set(word.split(' '))
    overlaps = [(k, len(v.intersection(words))) for k, v in s.items()]
    return max(overlaps, key=lambda x : x[1])[0]
```

```python
split_names = {i: set(i.split(' ')) for i in shares.keys()}
for i in petro_companies:
    match = fuzzy_match(i, split_names)
    print("matched {} to {}".format(i, match))
    market_share[i] = shares[match]
```

