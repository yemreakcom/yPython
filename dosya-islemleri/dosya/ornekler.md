---
description: Dosya okuma kodu ve örnekleri
---

# ⭐ Okuma Örnekleri

## 🎈 Tek Satır Okuma

```python
with open('./data/sample.txt', 'r') as f:
    print(f.readline())
```

## 👁‍🗨 Tüm Satırları Okuma

```python
with open('./data/sample.txt', 'r') as f:
    print(f.readlines())
```

## 🤸‍♂️ Dosyayı Kapatmadan Yazma

Sürekli açık olan bir dosya için:

* `flush()` metodu ile değişikliklerinizi kaydetmelisiniz
* Dosyayı kapatmak için `close()` metodunu kullanın

```python
DOSYA_YOLU = "README.md"
DOSYA_MODU = "w+" # w, a, r, w+ ...
ENCODING = "utf-8" # Özel karakterleri aktif etmek için

file = open(DOSYA_YOLU, DOSYA_MODU, encoding=ENCODING)
file.flush() # Dosyaya yapılan işlemleri kaydetme
file.close() # Dosyayı kapatır
```

## 👨‍💻 Encoding

| Komut | Açıklama |
| :--- | :--- |
| `sys.stdout.reconfigure(encoding='utf-8')` | 🚀 Emoji gibi farklı formattaki metinler üzerinde çalışırken kullanılır \(Terminal bunları algılayamaz\) |

> [How to set sys.stdout encoding in Python 3?](https://stackoverflow.com/a/52372390/9770490)



