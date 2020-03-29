---
description: Python üzerinde pytest ve modülleri ile test işlemleri
---

# ⚗️ Test İşlemleri

## 📂 Test için Proje Yapılandırması

```yaml
setup.py
setup.cfg
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

## 🔨 Test için Yapılandırma

* 📃 Test yapılandırma dosyası olarak `setup.cfg` dosyası kullanılır
* 💡 `[<modül>]` şeklinde modüle özgü ayarlar tanımlanır
* 🧪 `pytest` için `[tool:pytest]` alanı altında test yapılandırması yapılır
* 👀 `pytest`'in bakacağı dizinler `python_files` ve `testpaths` alanında belirtilir

```yaml
[flake8]
max-line-length = 99
max-complexity = 11
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

## ⚗️ Test İşlemini Yapma

* 🖤 Test komutu `python -m pytest` olarak bilinir
* 🕵️‍♂️ `pytest` tüm test paketlerini `setup.cfg` dosyasında belirtildiği şekilde bulacaktır
* 🧐 `flake8 --exclude=venv* --statistics` komutu ile kod kalitesini ölçebilirsiniz

{% hint style="warning" %}
📢 Sadece `pytest`komutu hatalara sebebiyet vermekte
{% endhint %}

## 🔸 Unit Test İşlemleri

* 📦 Unit test için `unittest` paketi kullanılır
* 💠 `setUp`  metodu ile her test öncesi işlemler tanımlanır
* 💦 `tearDown` metodu ile de her test sonrası işlemler tanımlanır
* 👨‍💼 `python -m pytest` komutu ile çalıştırılabilirler

```python
from unittest import TestCase

class TestStringMethods(TestCase):

    def setUp(self):
        self.p = subprocess.Popen('notepad')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
            
    def tearDown(self):
        self.p.terminate()

if __name__ == '__main__':
    unittest.main()
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [`unittest`](https://docs.python.org/3/library/unittest.html) paketine bakabilirsin.
{% endhint %}

## 🐛 Hata Mesajları Bekleme

* 👮‍♂️ Beklenen hata mesajları için `with` yapısı kullanılır
* 🧐 Beklediğin hata tipini `with` içerisinde yazıp, alt scope'una kodlarını yazın
* 💁‍♂️ Eğer içeride hata fırlatılmazsa `pytest` test başarısız olarak gösterecektir

```python
with pytest.raises(subprocess.SubprocessError):
    subprocess.check_output(
        "ygitbookintegration {}".format(args),
        universal_newlines=True
    )
```

## 📃 Dokümantasyon ile Test İşlemleri

* 📑 PyDoc alanında `>>>` karakterleri ile kod yazabiliriz
* 👁️ Kod çıktılarını hemen alt satıra yazılır
* 👮‍♂️ String çıktıları için `'` karakteri arasına yazmanız gerekir
* 🚀 Harici fonksiyonlar da kullansa, doküman ile test edilebilir

{% hint style="warning" %}
📢 Whitespace karakterleri, örneğin `\n`  için `'` karakteri arasında `\\n` olarak belirtilir
{% endhint %}

```python
def find_level(root: Path, startpath: Path) -> int:
    """Dizin seviyesini bulma

    Arguments:
        root {Path} -- Dizin yolu
        startpath {Path} -- Ana dizin yolu

    Returns:
        int -- Derinlik seviyesi

    Examples:
        >>> find_level(Path("./Documents/Configuration"), Path("."))
        2
    """
    return len(root.relative_to(startpath).parts)


find_level(Path("./Documents/Configuration"), Path(".")) # 2
```

```python
def generate_custom_link_string(
    name: str,
    path: str,
    indent: Indent = None,
    is_list: bool = False,
    single_line: bool = False
) -> str:
    """Özel link metni oluşturma

    Arguments:
        name {str} -- Link'in ismi
        path {str} -- Link'in adresi

    Keyword Arguments:
        intent {Indent} -- Varsa girinti objesi (default: {None})
        is_list {bool} -- Liste elamanı olarak tanımlama '- ' ekler (default: {False})
        single_line {bool} -- Tek satırda yer alan link '\n' ekler (default: {False})


    Returns:
        {str} -- Oluşturulan link metni

    Examples:
        >>> generate_custom_link_string(\
            'YPackage',\
            'https://ypackage.yemreak.com',\
            indent=Indent(2),\
            is_list=True,\
            single_line=True\
        )
        '    - [YPackage](https://ypackage.yemreak.com)\\n'

    """
    return Link(name, path).to_str(indent=indent, is_list=is_list, single_line=single_line)
```

## 🔗 Faydalı Bağlantılar

* [📖 Choosing a test layout / import rules](https://docs.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules)

