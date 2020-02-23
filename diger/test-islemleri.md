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

* 🖤 Test komutu `pytest` olarak bilinir
* 🕵️‍♂️ `pytest` tüm test paketlerini `setup.cfg` dosyasında belirtildiği şekilde bulacaktır
* 🧐 `flake8 --exclude=venv* --statistics` komutu ile kod kalitesini ölçebilirsiniz

## 🔗 Faydalı Bağlantılar

* [📖 Choosing a test layout / import rules](https://docs.pytest.org/en/latest/goodpractices.html#choosing-a-test-layout-import-rules)

