---
description: Argparse ile terminal komutlarını ayrıştırma
---
# ✨ Argparse

## 🔰 Argparse'ı Tanıyalım

* Argüman ekleme işlemi `parser = argparse.ArgumentParser(...)` ile yapılmaktadır.
* Parametrelerin kullanımı `argparse.ArgumentParser(description='yok')` şeklindedir.

| Parametre     | Açıklama                               |
| ------------- | -------------------------------------- |
| `description` | Uygulama ile alakalı açıklama metnidir |

## ➕ Argüman Ekleme

Argüman ekleme işlemi `parser.add_argument(...)` ile yapılmaktadır.

| Parametre    | Açıklama                                    |
| ------------ | ------------------------------------------- |
| 1. parametre | Kısa kullanım komutunu içerir               |
| 2. Parametre | Orjinal kullanım komutunu içerir            |
| `help`       | `-h` yazıldığında çıkacak olan yardım metni |
| `action`     | Davranışı belirler                          |
| `type`       | Tip bilgisini içerir (int, string ...)      |
| `default`    | Varsayılan değer                            |
| `dest`       | Verinin aktarılacağı değişken ismi          |
| `nargs`      | Çoklu veri alma                             |
| `required`   | Parametre girilmezse program çalışmaz       |

## 🔤 String Üzerinden Argümanları Alma

* 🖤 Terminal üzerindeki komutlar yerine string üzerinden ayrıştırma da yapabiliriz.
* 📢 Genel kullanımda ilk argüman, script yolu yani `__file__` olmalıdır
* 💎 Sistem argümanları varsayılan olarak ayrıştırılır

```python
import shlex

arguments = '-rgc -ll 2 -ru CE -ic "yemreak com" "sd" -cm "💫"'

# String listesi üzerinden ayrıştırma
arguments  = [__file__] + shlex.split(arguments)
parser.parse_args(arguments)

# Ayrıştırma normalde işlemi system argümanlarına yapılmaktadır
sys.argv = [__file__] + shlex.split(arguments)
parser.parse_args()

```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Parsing a string as a Python argument list](https://stackoverflow.com/a/49723227/9770490) alanına bakabilirsin.
{% endhint %}
