# 🚪 IPython Giriş

## Temel Bilgiler

- Tüm python özelliklerini destekler, python'a ek özellikler barındırır.
  - Bash, SQL, hız ölçümleri vs ...
- _Jupyter Notebook_ ve [Google Colabratory][Google Colabratory] gibi platformlarda kulanılır

> Bu yazı [Google Colabratory][Google Colabratory]'i temel almıştır.

## Hızlı Notlar

| Operatör           | Açıklama                                         |
| ------------------ | ------------------------------------------------ |
| `!`                | Komut terminal üzerinde çalıştırılır             |
| `%`                | Tüm os üzerinde kalıcı komutlar (Magic function) |
| `#`                | Yorum satırı                                     |
| `#@`               | Form komutları                                   |
| `\<satir_atlatma>` | Satır atlatmak için kullanılır                   |
| `<func>??`         | Fonksiyonun kodlarını gösterir                   |

### Kısayollar

| Kısayol                               | Açıklama                            |
| ------------------------------------- | ----------------------------------- |
| <kbd>⭾ Tab</kbd>                      | Kod tamamlama                       |
| <kbd>⇧ Shift</kbd> + <kbd>⭾ Tab</kbd> | Seçili objenin ne olduğunu gösterme |

## Terminal İşlemleri

- Terminal komutları **unix** komutlarıdır
- Terminal işlemlerinin her biri `!` ön eki ile başlamalıdır.

| İşlem                   | Açıklama                                               |
| ----------------------- | ------------------------------------------------------ |
| `!echo {<python_kodu>}` | Python kodunun return değerini kullanma                |
| `!echo $<py_degiskeni>` | Tek kelimelik değişken (veya ortam değişkeni) kullanma |
| `!cd`                   | Sadece o satır için terminal dizini değiştirme         |
| `%cd`                   | Terminalin dizinini değiştirme                         |
| `!kill -9 -1`           | Sistemi sıfırlama                                      |

- Python değişkenlerini terminal komutunda kullanamk için:
  - `{<python_kodu>}` Arasına python komutu yazılır, return değeri kullanılır
  - `$` tek kelimelik değişkenlerin kullanımı

> `!` (terminal) komutların en ufak yazım hatası, `{}` gibi operatörler ile python komutlarının alınmasını engeller.

### Terminal İşlemleri Örneği

```py
TEMP = 'gecici'
!echo {gecici} # Python değişkenini kullanma
!echo {gecici.split('i')[0]} # Python kod parçası kullanma

!echo $PYTHONPATH # Ortam değşkenini kullanma
```

### İşletim Sistemi Bilgileri

```ipynb
!less /etc/os-release
```

```sh
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
(END)^C
```

## Magic Function

| Func                                | Açıklama                                        |
| ----------------------------------- | ----------------------------------------------- |
| `%%bash`                            | Kod bloğunun `bash` türünden olacağını belirtir |
| `%%timeit`                          | Blokta geçen süreyi hesaplar                    |
| `%%expect_exception AttributeError` | Hatayı fırlatır, run error engeller             |


[Google Colabratory]: ../../Google%20Notlar%C4%B1%5CGoogle%20Colabrotory.md "Google'ın sunduğu bulut bilgisayarlar"
