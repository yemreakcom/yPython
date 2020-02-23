---
description: >-
  Python ve GitHub üzerinde sürekli entegrasyon, otomatik testler ve pytest
  kullanımı
---

# 🔄 Continuous İntegration \(CI\)

## 👀 Hızlı Bakış

![](../.gitbook/assets/github_ci_example.png)

![](../.gitbook/assets/ci_fast_notes.png)

## 📂 CI Dizini Oluşturma

* 👨‍💼 Daha verimli çalışma adına CI dosyaları aynı dizinde toplanır

![](../.gitbook/assets/ci_folder_structure.png)

### 📃 Gereksinimleri tanımlama

{% code title="requirements.txt" %}
```yaml
pytest
wheel
flake8
```
{% endcode %}

### 🏗️ Kurulum işlemlerini tanımlama

{% code title="ci/install.bat" %}
```bash
python -m venv venv
call venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install --upgrade -r .\ci\requirements.txt
python -m pip install --upgrade .
call deactivate

```
{% endcode %}

### ⚗️ Test işlemlerini tanımlama

{% code title="ci/test.bat" %}
```text
call venv\Scripts\activate.bat
pytest
call deactivate

```
{% endcode %}

### 🧪 Kod kalitesini test etme

{% code title="ci/quality\_test.bat" %}
```text
call venv\Scripts\activate.bat
flake8 --exclude=venv* --statistics
call deactivate

```
{% endcode %}

### 👷‍♂️ Derleme işlemleri

{% code title="ci/build.bat" %}
```text
call venv\Scripts\activate.bat
python setup.py sdist bdist_wheel
call deactivate

```
{% endcode %}

### 🛰️ Yayınlama işlemleri

{% code title="ci/upload.bat" %}
```text
twine upload dist/*
```
{% endcode %}

## 🔀 GitHub Workflow Oluşturma

{% code title=".github/workflows/pythonpackage.yml" %}
```yaml
name: 🕵️‍♂️ Continuous integration
on: [push]
jobs:
  build:
    runs-on: ${{ matrix.os }}
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.8]
        os: [macos-latest, ubuntu-latest, windows-latest]
        include:
          - os: windows-latest
            INSTALL: .\ci\install.bat
            TEST: .\ci\test.bat
            QUALITY_TEST: .\ci\quality_test.bat
          - os: macos-latest
            INSTALL: .\ci\install.sh
            TEST: .\ci\test.sh
            QUALITY_TEST: .\ci\quality_test.sh
          - os: ubuntu-latest
            INSTALL: .\ci\install.sh
            TEST: .\ci\test.sh
            QUALITY_TEST: .\ci\quality_test.sh
    steps:
      - uses: actions/checkout@v1
      - name: 🏗️ Python ${{ matrix.python-version }} setup
        uses: actions/setup-python@v1
        with:
          python-version: ${{ matrix.python-version }}
      - name: 📦 Installing dependencies
        run: |
          ${{matrix.INSTALL}}
      - name: ⚗️ Functional testing
        run: |
          ${{matrix.TEST}}
      - name: 🧐 Python code style testing
        run: |
          ${{matrix.QUALITY_TEST}}
```
{% endcode %}

## 🔗 Faydalı Linkler

* [📖 Good Integration Practices](https://docs.pytest.org/en/latest/goodpractices.html)
* [📃 Continuous integration with python](https://realpython.com/python-continuous-integration/)
* [📖 Workflow syntax for GitHub Actions](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions)
* [📖 Virtual environments for GitHub-hosted runners](https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners)
* [👪 Create matrix with multiple OS and env for each one](https://github.community/t5/GitHub-Actions/Create-matrix-with-multiple-OS-and-env-for-each-one/td-p/38339)

