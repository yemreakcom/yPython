---
description: IPython ile terminal komutları ve kullanım örnekleri
---
# 🖤 Terminal İşlemleri | IPython

## 🚴‍♂️ Komutları Tanıyalım

* Terminal komutları, **unix** komutlarıdır
* Terminal işlemlerinin her biri `!` ön eki ile başlamalıdır.
* Python değişkenlerini terminal komutunda kullanmak için:
  * `{<python_kodu>}` Arasına python komutu yazılır, return değeri kullanılır
  * `$` tek kelimelik değişkenlerin kullanımı 

| İşlem                   | Açıklama                                               |
| ----------------------- | ------------------------------------------------------ |
| `!echo {<python_kodu>}` | Python kodunun return değerini kullanma                |
| `!echo $<py_degiskeni>` | Tek kelimelik değişken (veya ortam değişkeni) kullanma |
| `!cd`                   | Sadece o satır için terminal dizini değiştirme         |
| `%cd`                   | Terminalin dizinini değiştirme                         |
| `!kill -9 -1`           | Sistemi sıfırlama                                      |

{% hint style="warning" %}
📢 Terminal (`!`) komutların en ufak yazım hatası, `{}` gibi operatörler ile python komutlarının alınmasını engeller.
{% endhint %}

## ⭐ Kod Örneği

```python
TEMP = 'gecici'
!echo {gecici} # Python değişkenini kullanma
!echo {gecici.split('i')[0]} # Python kod parçası kullanma

!echo $PYTHONPATH # Ortam değşkenini kullanma
```

