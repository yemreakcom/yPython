# 🚩 Yol İşlemleri (Path)

Yol işlemleri için `os.path` modülü kullanılır.

| Metod                       | Açıklama                                           |
| --------------------------- | -------------------------------------------------- |
| `isfile(<yol>)`             | Dosya mı kontrolü                                  |
| `isdir(<yol>)`              | Dizin mi kontrolü                                  |
| `join(<yol1>, <dosya_adı>)` | Dizinleri birleştirme                              |
| `basename(<yol>)`           | Dosyanın adını ve uzantısını bulma                 |
| `splitext(<dosya_adı>)`     | Dosyanın yolunu ve uzantısını döndürür (path, ext) |

- `<yol>` Path, dosya yolu
  - _Örn: C:\Users\Username\help.txt_
- `<dosya_adı>` Dosyanın uzantısıyla birlikteki adı
  - _Örn: help.txt_

[dosya erişim modları]: https://stackoverflow.com/a/1466036/9770490
