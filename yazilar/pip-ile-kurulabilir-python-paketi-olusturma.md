---
description: >-
  Python paket yöneticisi olan pip ile projenizin indirilebilir olmasını
  sağlamak isterseniz okumaya devam edin.
---

# 📦 Pip ile Kurulabilir Python Paketi Oluşturma

## 👇 Nasıl bir şey mi yapmış olacaksınız

> Eski adı: Pip Üzerinde Paket Yayınlama

![](../.gitbook/assets/python_pypi.png)

## 🧾 PyPI'ya Kayıt olma

* [PyPI Register](https://pypi.org/account/register/)
* Email'inizi onaylayın

## 👷‍ Dosya Yapısını Oluşturma

### 📂 Dizin Yapısı

* 🔸 Açıklama metninizi **markdown** formatı ile `README.md` içerisine yazın.

![](https://github.com/YEmreAk/YPython/tree/242e99657e53eccf56e956980a7baf4dcda43744/.gitbook/assets/image%20%289%29.png)

### 👨‍🔧 setup.py kurulum dosyası

* 🔨 Kurulum yapılandırma dosyasıdır.

```python
from distutils.core import setup
import setuptools

VERSION = "1.0.0" # BURAYI AKLINIZDA TUTUN (Değiştirebilirsiniz)

long_description = ""
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()


setup(
    name='PAKET_İSMİ',         # How you named your package folder (MyLib)
    packages=setuptools.find_packages(),
    # Start with a small number and increase it with every change you make
    version=VERSION,
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Sık kullanılan python işlemleri için hazır paket',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='İsim Soyisim',                   # Adınızı soyadınız yazın
    author_email='eposta@gmail.com',      # E-posta adresiniz
    # Provide either the link to your github or to your website
    url='https://github.com/GITHUB_HESABI/PAKET_İSMİ',
    # I explain this later on
    download_url=f'https://github.com/GITHUB_HESABI/PAKET_İSMİ/archive/{VERSION}.tar.gz',
    # Keywords that define your package best
    keywords=['Alakalı', 'kelimeler'],
    # install_requires=[], # Bağımlılıklar
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # Komut isteminden kullanılacaksa, main'e verilen yol
    # entry_points={
    #     # Komut isteminden çalıştırma
    #     # örndeğin: ypackage
    #     # Kullanım: 'ypackge = ypackage.ypackage:main
    #     'console_scripts': [
    #         'komut_ismi = dizin.dosya:main',
    #     ]
    # },
)
```

### 🏹 `__init__` ile modülleri dışa aktarma

* ⤴️ Dosyanın amacı içerisindeki her paketleri dışarı aktarmaktır
* 💁‍♂️ Dosyanın içi boş olursa, tüm dizini ele alır

```python
from . import filesystem
from . import common
from . import gitbook
from . import markdown
```

{% hint style="warning" %}
📢 Bu dosya olmazsa diğer paketleri pip aracı algılayamaz
{% endhint %}

## 📡 GitHub'da Yayınlama

GitHub üzeinden repository oluşturun ve projenizi oraya upload edin.

> GitHub hakkında detaylar için arama sitemin arama motoruna `GitHub` yazabilirsiniz

* GitHub projenizin urline girin
* **Release** alanına tıklayın
* Daha önceden varsa Edit yoksa Create butonuna tıklayın ve yeni bir sürüm oluşturun
* `Tags` alanına `setup.py` dosyamızdaki `VERSION` değerini yazın
  * Download url kısmındaki `...{VERSION}.tar.gz'` yapısından dolayı
  * Örn: `1.0.0`
* Açıklamalarınızı yapıp Update Relesae butonuna basın
  * Ek olarak dosya eklemenize gerek yoktur

## 📦 Gerekli Paketlerin Kurulumu

Bu işlemleri için **python** ve **pip** araçlarının kurulu olması lazımdır.

```bash
pip install --upgrade setuptools wheel tqdm
pip install twine
```

## 📡 Projeyi PyPI'da Yayınlama

* Proje dizininize girin \([yukarıdaki resimdeki alan](pip-ile-kurulabilir-python-paketi-olusturma.md#dosya-yapisini-olusturma)\)
* `rm -rf build/ dist/` \(`del build/ dist/` veya el\) ile eski proje çalışmalarını silin
* `python setup.py sdist bdist_wheel` komutu ile projenizi aktarılmaya hazır hale getirin
* `twine upload dist/*` komutu ile PyPI'ya projenizi aktarın

## 🌌 Projeyi PyPI'da Güncelleme

* `setup.py`'daki `VERSION` bilginizi arttırın
  * Örn: `1.0.1`
* GitHub üzerinden `v<VERSION>` yeni **release** oluşturun
  * Örn: `v1.0.1`
* [📡 Projeyi PyPI'da Yayınlama](pip-ile-kurulabilir-python-paketi-olusturma.md#projeyi-pypida-yayinlama) alanındakileri uygulayın

## 🔗 Harici Bağlantılar

* [How to upload your python package to PyPi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)
* [Pakete python dosyası harici dosya ekleme - 1](https://stackoverflow.com/a/10924965)
* [Pakete python harici dosyalar ekleme - 2](https://stackoverflow.com/a/11848281)
* [Paket için Sembolik link oluşturma](https://www.reddit.com/r/learnpython/comments/8pvne4/create_symlink_on_pip_install/)

