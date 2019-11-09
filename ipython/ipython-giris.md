# 🔰 IPython Giriş

## ❔ Nedir

* Tüm python özelliklerini destekler, python'a ek özellikler barındırır.
  * Bash, SQL, hız ölçümleri vs ...
* _Jupyter Notebook_ ve Google Collaboratory gibi platformlarda kullanılır

> Bu yazı Google Collaboratory temel almıştır.

## 💖 Önemli Hususlar

{% tabs %}
{% tab title="💎 Operatörler" %}
| Operatör | Açıklama |
| :--- | :--- |
| `!` | Komut terminal üzerinde çalıştırılır |
| `%` | Tüm os üzerinde kalıcı komutlar \(Magic function\) |
| `#` | Yorum satırı |
| `#@` | Form komutları |
| `\<satir_atlatma>` | Satır atlatmak için kullanılır |
| `<func>??` | Fonksiyonun kodlarını gösterir |
{% endtab %}

{% tab title="💫 Kısayollar" %}
| Kısayol | Açıklama |
| :--- | :--- |
| ⭾ Tab | Kod tamamlama |
| ⇧ Shift + ⭾ Tab | Seçili objenin ne olduğunu gösterme |
{% endtab %}

{% tab title="💠 Magic Function" %}
| Fonksiyon | Açıklama |
| :--- | :--- |
| `%%bash` | Kod bloğunun `bash` türünden olacağını belirtir |
| `%%timeit` | Blokta geçen süreyi hesaplar |
| `%%expect_exception AttributeError` | Hatayı fırlatır, run error engeller |
{% endtab %}
{% endtabs %}

## 🖤 Terminal İşlemleri

* Terminal komutları **unix** komutlarıdır
* Terminal işlemlerinin her biri `!` ön eki ile başlamalıdır.

{% tabs %}
{% tab title="📜 Açıklama" %}
| İşlem | Açıklama |
| :--- | :--- |
| `!echo {<python_kodu>}` | Python kodunun return değerini kullanma |
| `!echo $<py_degiskeni>` | Tek kelimelik değişken \(veya ortam değişkeni\) kullanma |
| `!cd` | Sadece o satır için terminal dizini değiştirme |
| `%cd` | Terminalin dizinini değiştirme |
| `!kill -9 -1` | Sistemi sıfırlama |

* Python değişkenlerini terminal komutunda kullanamk için:
  * `{<python_kodu>}` Arasına python komutu yazılır, return değeri kullanılır
  * `$` tek kelimelik değişkenlerin kullanımı

> `!` \(terminal\) komutların en ufak yazım hatası, `{}` gibi operatörler ile python komutlarının alınmasını engeller.
{% endtab %}

{% tab title="⭐ Kod Örneği" %}
```python
TEMP = 'gecici'
!echo {gecici} # Python değişkenini kullanma
!echo {gecici.split('i')[0]} # Python kod parçası kullanma

!echo $PYTHONPATH # Ortam değşkenini kullanma
```
{% endtab %}
{% endtabs %}

