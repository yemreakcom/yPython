---
description: Python küme yapısı (set)
---

# ⭕ Set

## 🔰 Set Yapısını Tanıyalım

Küme işlemleri için kullanılır.

* Temel küme özelliklerini taşır.
  * _Keşisim, birleşim ..._
* Veriler **sıralı değildir**
* Set'in kendine özgü bir yerleştirme yapısı \(_hash_\) vardır.
  * Bu yapı sayesinde veriler, en hızlı olacak şekilde, **karmaşık** olarak dizilir
  * List'ten daha **hızlıdır**
  * Kaynak için [buraya](https://stackoverflow.com/a/7717046/9770490s) bakabilirsin
* Birbirinden farklı değişkenleri tutabilir
* Aynı değişken birden fazla **yazılamaz** \(küme özelliği\)
* Tüm değerlerin _inmutable_ \(değiştirilemez\) olması gerekmektedir
  * `myset = {[1, 2, 3]}` komutunda `[1, 2, 3]` list öğesi _mutable_ olduğundan değiştirilebilir \(ekleme çıkarma olabilir\)
* _Indexing_ \(indekslenme\) ve _slicing, subscription_ \(kesme, parçalama\) işlemlerini desteklemez
  * `myset[0]` çalışmaz

## 💠 Set Metotları

| Set Metodları | Açıklama |
| :--- | :--- |
| `add(<immutable>)` | Eleman ekleme |
| `for <isim> in <set>` | Elemanları döngü ile alma |
| `<isim> = next(iter(<set>))` | Elemanları sıra ile alma |

* `<immutable>` Herhangi değiştirilemez değer
  * Örn: `1`, `"yemreak"`, `tuple`, `str`, `int` vs
* `<isim>` Elemena verilecek isim
  * Örn: `i`, `e` vs

## 🔗 Set için Faydalı Bağlantılar

* [Hızlıca set açıklaması](https://www.programiz.com/python-programming/set)
* [Detaylı set açıklaması](https://www.datacamp.com/community/tutorials/sets-in-python)

