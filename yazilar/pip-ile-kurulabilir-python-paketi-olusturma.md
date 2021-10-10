---
description: Python paket yöneticisi olan pip ile projenizin indirilebilir olmasını sağlamak isterseniz okumaya devam edin.
---
# 📦 Pip ile Kurulabilir Python Paketi Oluşturma

## 👀 Hızlı Bakış

* 🛰️ Bu yazı projenin GitHub ve PyPI üzerinden yayınlanmasını sağlar
* ⏬ `pip install <paket>` komutu ile paketiniz indirilebilir

![](../.gitbook/assets/python_pypi.png)

## 🧾 PyPI'ya Kayıt olma

* [PyPI Register](https://pypi.org/account/register/)
* Email'inizi onaylayın

## 👷‍ Dosya Yapısını Oluşturma

### 📂 Dizin Yapısı

* 🔸 Açıklama metninizi **markdown** formatı ile `README.md` içerisine yazın.
* 💖 Önemli alanlar kırmızı ile ifade edilmiştir

```
setup.py
src/
    mypkg/
        __init__.py
        app.py
        view.py
tests/
    __init__.py
    foo/
        __init__.py
        test_view.py
    bar/
        __init__.py
        test_view.py
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Choosing a test layout / import rules](https://docs.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules) alanına bakabilirsin.
{% endhint %}

### 👨‍🔧 `setup.py` kurulum dosyası

* 🔨 Kurulum yapılandırma dosyasıdır.
* 🏗️ Alttaki taslağı kullanabilirsiniz

```python
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

VERSION = "2.7.4.3"
README_PATH = "docs/README.md"

# test_requirements = ["behave", "behave-classy", "pytest"]

long_description = ""
with open(README_PATH, "r", encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="ypackage",
    version=VERSION,
    license="Apache Software License 2.0",
    description="Proje açıklaması",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yazar ismi",
    author_email="eposta@gmail.com",
    url="https://github.com/<username>/<projectname>",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/yedhrab/YPackage/blob/master/docs/CHANGELOG.md",
        "Issue Tracker": "https://github.com/yedhrab/YPackage/issues",
    },
    keywords=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["requests"], # Bağlı olduğu paketler, örn: requests
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=="2.6"": ["argparse"],
    },
    setup_requires=[
        "pytest-runner",
    ],
    entry_points={
        # Komut isteminden çalıştırma
        # örndeğin: ypackage
        # Kullanım: "ypacakge = ypackage.ypackage:main
        "console_scripts": [
            "ygitbookintegration = ypackage.cli.integrate_into_gitbook:main",
            "ygoogledrive = ypackage.cli.gdrive:main",
            "ygooglesearch = ypackage.cli.gsearch:main",
            "yfilerenamer = ypackage.cli.file_renamer:main",
            "ythemecreator = ypackage.cli.theme_creator:main"
        ]
    },
    # tests_require=test_requirements,
)

```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Python Packaging - Setup Script](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-setup-script) alanına bakabilirsin.
{% endhint %}

### 🔨 `setup.cfg` yapılandırma dosyası

* 👨‍💼 Bu yapılandırma dosyası sayesinde test işlemleri ve diğer paket hizmetleri yönetilir
* 👨‍🔧 `src/ypackage` kısmına kendi paketinizin adını yazın

```bash
[flake8]
max-line-length = 99
exclude = */migrations/*

[options]
# tests_require is a list of dependencies that are *absolutely required*
# to run the tests. tests_require is used when running tests from your
# *current* Python environment (that is, not using tox).
# tests_require is ignored by tox.
#
# As such, you can usually get away with neglecting tests_require ---
# it's not a big deal if some of the dependencies get left out.
#
# If you're running tests from your current environment, it's because
# you're actively developing, in which case you usually have an
# environment you built for development. But if you have to change
# environments mid-development for any reason, tests_require can save you
# from getting tripped up.
#
# tests_require is used when running tests and debugging through an IDE like
# PyCharm, to ensure the environment the IDE is using has the requirements.
#
# Unless you're in one of those situations, you can simply ignore this.
tests_require = pytest

[aliases]
# Alias `setup.py test` to `setup.py pytest`
test = pytest

[tool:pytest]
# If a pytest section is found in one of the possible config files
# (pytest.ini, tox.ini or setup.cfg), then pytest will not look for any others,
# so if you add a pytest config section elsewhere,
# you will need to delete this section from setup.cfg.
norecursedirs =
    .git
    .tox
    .env
    venv
    dist
    build
    migrations

python_files =
    test_*.py
    *_test.py
    tests.py
addopts =
    -ra
    --strict
    --ignore=docs/conf.py
    --ignore=setup.py
    --ignore=ci
    --ignore=.eggs
    --doctest-modules
    --doctest-glob=\*.md
    --tb=short
    --pyargs
# The order of these options matters. testpaths comes after addopts so that
# nameless in testpaths is interpreted as
# --pyargs nameless.
# Any tests in the src/ directory (that is, tests installed with the package)
# can be run by any user with pytest --pyargs nameless.
# Packages that are sensitive to the host machine, most famously NumPy,
# include tests with the installed package so that any user can check
# at any time that everything is working properly.
# If you do choose to make installable tests, this will run the installed
# tests as they are actually installed (same principle as when we ensure that
# we always test the installed version of the package).
# If you have no need for this (and your src/ directory is very large),
# you can save a few milliseconds on testing by telling pytest not to search
# the src/ directory by removing
# --pyargs and nameless from the options here.
testpaths =
    src/ypackage
    tests/

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

## 📑 Manifest Dosyası

* 🕵️‍♂️ Manifest dosyası ile paket içerisindeki dosyaların projeye dahil olması sağlanır
* 📌 Bu dosya proje dizininde bulunmalıdır
* ➕ `include` komutu ile harici dosyalar dahil edilir
* 🗃️ `recursive-include` komutu ile dizin ve içerisindeki tüm dosyalar dahil edilir

{% code title="MANIFEST.in" %}
```elixir
include LICENSE
include README.md # docs/README.md
# recursive-include src/ypackage/templates *

```
{% endcode %}

## ⚗️ Paketi Test Etme

* 👨‍🔬 Paket kurulumunu `pip install -e .` komutu ile yerel olarak yapabilirsin.
* 💁‍♂️ Kaynak kodunu değiştirmeye ve istenildiği zaman yeniden test edilmeye olanak sağlar

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için Good Integration Practice - Install Package With Pip alanına bakabilirsin.
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
* Açıklamalarınızı yapıp Update Release butonuna basın
  * Ek olarak dosya eklemenize gerek yoktur

## 🛰️ Projeyi PyPI'da Yayınlama

### 📦 Gerekli Paketlerin Kurulumu

Bu işlemleri için **python** ve **pip** araçlarının kurulu olması lazımdır.

```bash
pip install --upgrade setuptools wheel tqdm
pip install twine
```

### 🏗️ Projeyi Derleme

* Proje dizininize girin ([yukarıdaki resimdeki alan](pip-ile-kurulabilir-python-paketi-olusturma.md#dosya-yapisini-olusturma))
* `rm -rf build/ dist/` (`del build/ dist/` veya el) ile eski proje çalışmalarını silin
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
