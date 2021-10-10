---
description: Anaconda için ek / diğer notlar
---
# 🎪 Diğer Notlar | Conda

## 🌄 PyCharm Üzerinden Anaconda

{% tabs %}
{% tab title="🔨 Derleyici Ayarları" %}
Çalıştırma butonu üzerinden (⇧ Shift + `F9`) projeyi çalıştırmak için:

* Derleme butonu yanındaki `seçme kutusuna` tıklayın
* `Edit Configuration`
* Sol üstten `+` butonuna basın
  * `Python`
* `Script Path:` kısmından çalıştırmak istediğiniz **.py** uzantılı dosyayı seçin
* `OK`
{% endtab %}

{% tab title="✨ Sanal Ortam Oluşturma" %}
* ✲ Ctrl + ⎇ Alt + `S` ile ayarlara girin
* `Project: imgtotext`
  * `Project: Interpeter`
* Sağ üstteki `ayarlar butonu`na tıklayın
  * `Add`
  * `Conda Enviroment`
  * `OK`
* `+` butonu ile ek paket kurulumu yapabilirsiniz (_İsteğe Bağlı_)
{% endtab %}
{% endtabs %}

## 🐞 Conda SSL Hatası

{% tabs %}
{% tab title="👨‍🔧 Windows Üzerinden Ağ Sıfırlama" %}
Windows 10'daki `Ağı Sıfırla` ayarını deneyin

* Ayarlar (_Options_)
* Ağ ve İnternet (_Network & Internet_)
* Durum sekmesi (_Status tab_)
* Sayfanın en altına bakın (_Ağı Sıfırla / Network Reset_)
* Şimdi Sıfırla (_Reset Now_)

> Bu işlem kaydedilmiş WI-FI şifrelerini de silecektir.
{% endtab %}

{% tab title="⏬ OpenSSL Kurulumu" %}
Kurulum sayfasına gitmek için [buraya](https://slproweb.com/products/Win32OpenSSL.html) tıklayabilirsin.

> Kaynak için [buraya](https://github.com/conda/conda/issues/8046#issuecomment-450515815) tıklayabilirsin.
{% endtab %}

{% tab title="🥅 Conda ile Networkx İndirme" %}
```bash
conda install -c anaconda networkx
```
{% endtab %}

{% tab title="🔗 Diğerleri" %}
* [How to install the most recent version of OpenSSL on Windows 10 in 64 Bit](https://www.cloudinsidr.com/content/how-to-install-the-most-recent-version-of-openssl-on-windows-10-in-64-bit/)
* [Conda update failed: SSL error: \[SSL: CERTIFICATE_VERIFY_FAILED\] certificate verify failed](https://stackoverflow.com/a/35804869/9770490)
* [Setting SSL Verify](https://github.com/ContinuumIO/anaconda-issues/issues/494#issuecomment-155097614)
{% endtab %}
{% endtabs %}
