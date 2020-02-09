---
description: Anaconda Kullanımı
---

# ✨ Anaconda Kullanımı

## 🧰 Temel Condo Kullanımı

Anaconda paket yönetim aracı `conda`'dır.

* `requirements.txt` dosyası sayesinde projeyi farklı ortamlara aktarmak istediğimizde, gerekli kurulumları hızlıca yapabiliriz.
* \*\*\*\*[Difference between pip freeze and conda list](https://stackoverflow.com/questions/41249401/difference-between-pip-freeze-and-conda-list)

### ✨ Güncelleme İşlemleri

```bash
# ✨ Conda'yı Güncelleme
conda update -n base -c defaults conda

# 📋 Tüm Paketleri Güncelleme
conda update --all
 
# 📦 Paket Sürümlerini Gösterme
conda search <paket> --info
conda search tensorflow-gpu --info # Örnek

```

### ⏬ Yükleme İşlemleri

{% tabs %}
{% tab title="⏬ Yükleme İşlemleri" %}
```bash
conda install <ayarlar> <framework | package | lib>
conda install -c <depo-ismi> <frameword vs.>

conda install -c conda-forge python-socketio # Örnek (dev olabilir)
conda install -c anaconda  flask # Örnek (stable olabilir)
```
{% endtab %}

{% tab title="⏬ Belli Bir Sürümü İndirme" %}
```bash
conda install -c <depo_ismi> <paket>=<versiyon>
conda install -c anaconda tensorflow-gpu=<versiyon> # Örnek
```
{% endtab %}

{% tab title="📃 Requirement Dosyası Oluşturma" %}
```bash
conda list --export > requirements.txt
conda create --name <envname> --file requirements.txt # Dosyadan ortam oluşturma
```
{% endtab %}
{% endtabs %}



