# 🌟 Sık Kullanılanlar | Dosya

## 🧱 Temel İşlemler

Dizin işlemleri için `os` veya `glob` paketi kullanılır.

| Paket  | Fonksiyon                      | Açıklama                                         |
| ------ | ------------------------------ | ------------------------------------------------ |
| `os`   | `listdir(<yol>)`               | Dizinin içindekileri listeler                    |
| `os`   | `rename(<eski_ad>, <yeni_ad>)` | Dosya veya dizin adlandırma                      |
| `glob` | `glob(<yol_şablonu>)`          | Dosya ve dizinleri döndürür                      |
| `glob` | `iglob(<yol_şablonu>)`         | Dosya ve dizinleri generator yapısı ile döndürür |

* `<yol_şablonu>` Özel dizin sorguları
  * _Örn: \`_.txt`,`../help\`\*

## 📦 OS Path Modülü

| 💠 Metot                      | 📝 Açıklama                                                |
| ----------------------------- | ---------------------------------------------------------- |
| `os.path.dirname(<path>)`     | Bulunduğu dizinin adını alma                               |
| `os.path.basename(<path>)`    | Dosya (uzantı ile) veya dizin adını alma                   |
| `os.path.normpath(<path>)`    | OS'lar için farklılık gösteren `/`, `\\` sorununu düzeltme |
| `os.path.join(<path>, <str>)` | Path birleştirme (tanımlama)                               |
| `os.path.relpath(<path>)`     | Relative path'e çevirir (`.` `..` ile )                    |
| `os.path.realpath(<path>)`    | Tam path değerini verir                                    |
| `os.mkdir(<path>)`            | Dizin oluşturma                                            |
| `os.walk(<path>)`             | Verilen path üzerinden ilerleme (sırasız)                  |
| `os.path.splittext(<path>)`   | Adı ve uzantısına göre ayırma                              |

{% hint style="info" %}
⚠️ `os.walk` metodundan sonra `sort` ile içeriklerin sıralanması gerekmektedir, aksi halde işletim sistemlerine göre farklı çalışacaktır
{% endhint %}
