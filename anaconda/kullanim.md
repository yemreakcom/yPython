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

## 🌆 Sanal Ortam İşlemleri

Sanal ortamlar üzerine çalışmak istediğimiz projeler için kurulur ve gerekmediği vakit kaldırılır.

{% hint style="success" %}
Projelerin bağımlılıkları arasında çakışma olmasını engeller.
{% endhint %}

{% tabs %}
{% tab title="✨ Oluşturma" %}
```bash
conda create -n <ortam_ismi>
conda create -n myenv # Örnek
```

#### Requirements Dosyasına Uygun Sanal Ortam Oluşturma

```bash
conda create --name <ortam_ismi> --file requirements.txt
```

#### Belirli Python Sürümünde Ortam Oluşturma

```bash
conda create -n <ortam_ismi> anaconda python=<versiyon>
conda create -n Tensorflow anaconda python=3.6 # Örnek
```

> Ortam _Anaconda3/env_ dizinine kaydedilir.
{% endtab %}

{% tab title="🎈 Aktif Etme" %}
```bash
conda activate <ortam_ismi>
conda activate myenv # Örnek
```

> Ortam seçildiğinde \(base\) yazan kısımda \(`<ortam_ismi>`\) yazar.
{% endtab %}

{% tab title="🩸 Pasif Etme" %}
```bash
conda deactivate
```
{% endtab %}

{% tab title="🚮 Kaldırma" %}
```bash
conda env remove -n <ortam_ismi>
conda env remove -n myenv # Örnek
```

{% hint style="info" %}
Anaconda Prompt `base` ortamına geri döner.
{% endhint %}
{% endtab %}
{% endtabs %}

