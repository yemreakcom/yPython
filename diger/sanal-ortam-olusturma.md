---
description: Python ile virtual environment oluşturma (venv)
---

# 🌇 Sanal Ortam Oluşturma

## 🚴‍♂️ Sanal Ortama Giriş

* 🌇 Sanal ortamlar ile python paketleri ve sürümlerinin çakışması engellenir
* 🦄 Her projeye özgü bir python ortamı kullanılır
* 📈 Verimliliği artırır

```bash
# Sanal ortamı kurma
python3 -m venv tutorial-env
```

## 🐣 Sanal Ortamı Aktif Etme

{% tabs %}
{% tab title="✴️ Windows" %}
```text
tutorial-env\Scripts\activate.bat
```
{% endtab %}

{% tab title="🐧 Linux / MacOS" %}
```text
source tutorial-env/bin/activate
```
{% endtab %}
{% endtabs %}

