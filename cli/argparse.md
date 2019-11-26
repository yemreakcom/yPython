---
description: Argparse ile terminal komutlarını ayrıştırma
---

# ✨ Argparse

## 🔰 Argparse'ı Tanıyalım

* Argüman ekleme işlemi `parser = argparse.ArgumentParser(...)` ile yapılmaktadır.
* Parametrelerin kullanımı `argparse.ArgumentParser(description='yok')` şeklindedir.

| Parametre | Açıklama |
| :--- | :--- |
| `description` | Uygulama ile alakalı açıklama metnidir |

## ➕ Argüman Ekleme

Argüman ekleme işlemi `parser.add_argument(...)` ile yapılmaktadır.

| Parametre | Açıklama |
| :--- | :--- |
| 1. parametre | Kısa kullanım komutunu içerir |
| 2. Parametre | Orjinal kullanım komutunu içerir |
| `help` | `-h` yazıldığında çıkacak olan yardım metni |
| `action` | Davranışı belirler |
| `type` | Tip bilgisini içerir \(int, string ...\) |
| `default` | Varsayılan değer |
| `dest` | Verinin aktarılacağı değişken ismi |
| `nargs` | Çoklu veri alma |
| `required` | Parametre girilmezse program çalışmaz |

## 🔤 String Üzerinden Argümanları Alma

Terminal üzerindeki komutlar yerine string üzerinden ayrıştırma da yapabiliriz.

```python
string = "-h"
command = [__file__] + string.split()
parser.parse_args(command)
```

{% hint style="warning" %}
📢 Genel kullanımda ilk argüman script yolu `__file__` olmaktadır
{% endhint %}

