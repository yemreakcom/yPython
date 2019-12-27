---
description: 'Python obje, json veya anahtar-değer (key-value) çifti yapısı (dict)'
---

# 📙 Dict

## 🔰 Dict Yapısını Tanıyalım

Verilerin anahtarlara \(_key_\) göre saklandığı `list` yapısıdır.

* Her _key_ değeri eşsiz \(_unique_\) olmalıdır
* _Key_ değerleri **ana değişkenleri** olabilir, `list`, `tuple` gibi listeler olamaz

> Alttaki işlemlerin her biri `dict` objesinin alt işlemidir.

## 💠 Dict İşlemleri

| İşlem | Açıklama |
| :--- | :--- |
| `dict[<key>]` & `get(<key>)` | Anahtar ile veri alma, veri yoksa hata fırlatır |
| `dict[<key>] = <değer>` | Belirli anahtara değer atama |
| `<key> in dict` | Anahtar `dict`'e var mı kontrolü |
| `json.dumps(dict)` | `dict`'i `str`'a çevirme |
| `json.loads(re.sub("//.*","",str,flags=re.MULTILINE))` | JSON'u yorum satırlarını atarak okuma |
| `dict( (a,1) for a in <list>)` | `<liste>`'nin her elamanı ile 1'i eşleyen dict |
| `copy_dict ? {**dict}` | `dict` kopyalama |

## 🔗 Dict için Faydalı Bağlantılar

* [`Dict`'i `str`'a çevirme](https://stackoverflow.com/a/4547331/9770490)
* [`Dict`'ten hızlı bir yöntem var mı](https://stackoverflow.com/a/40694623/9770490)
* [`Dict` kopyalama](https://stackoverflow.com/a/53413487/9770490)

