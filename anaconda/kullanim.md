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

## 📦 Paket ve Kütüphane Kurulumları

Paket kurulumları `conda` komutu yardımıyla yapılır.

* Tüm bu işlemlerin **Anaconda Prompt** üzerinde yapıldığına emin olun!
* Sanal ortama yükleme yapılmadan önce sanal ortamın **aktif edilmesi** gerekmektedir!

{% tabs %}
{% tab title="👨‍💼 Pip" %}
```bash
conda install pip
```
{% endtab %}

{% tab title="🧮 Numpy" %}
```bash
conda install -c anaconda numpy
```
{% endtab %}

{% tab title="👁‍🗨 OpenCV" %}
```
conda install opencv
```
{% endtab %}

{% tab title="🐧 Linux için OpenCV" %}
```bash
pip install opencv-contrib-python
```
{% endtab %}

{% tab title="🌍 Selenium" %}
Web siteleri üzerinde işlem yapmak için kullanılır.

```bash
conda install -c conda-forge selenium
conda install -c clinicalgraphics selenium-chromedriver
```
{% endtab %}

{% tab title="🎴 Pillow" %}
Python resim kütüphanesi resim işlemleri için kullanılır.

```bash
conda install -c anaconda pillow
```
{% endtab %}

{% tab title="🐍 Python" %}
```bash
conda create -n $PYTHON36_ENV_NAME python=3.6 anaconda  # set custom env name
```
{% endtab %}
{% endtabs %}

### 🧠 Yapay Zeka Paketleri Kurulumu

{% tabs %}
{% tab title="🏹 Tensorflow" %}
### Tensorflow CPU

Anaconda'nın resmi sitesindeki açıklama için [buraya](https://www.anaconda.com/tensorflow-in-anaconda/) bakabilirsin.

* Bu kurulum CPU kurulumu olarak da geçmekte
* GPU kurulumu CPU'ya nazaran oldukça hızlı eğitim seçeneği sağlar
* GPU kurulumu için gereksinimleri sağlıyorsanız GPU kurulumu \(tensorflow-gpu\) yapmanız tavsiye edilir

> Daha yüksek verim için tensorflow için ortam oluşturun.

```bash
conda install -c conda-forge tensorflow
```

### Sanal Ortama Tensorflow Kurulumu

Tensorflow için sanal ortam oluşturmak hız açısından daha faydalıdır.

```bash
conda create -n tensorflow-cpu tensorflow # Tensorflow ortamı oluşturma
conda activate tensorflow-cpu # Ortamı aktif etme
```

### Tensorflow-GPU Kurulumu

Anaconda'nın resmi sitesindeki açıklama için [buraya](https://www.anaconda.com/tensorflow-in-anaconda/) bakabilirsin.

* Bu kurulum GPU kurulumu olarak geçmekte
* GPU kurulumu CPU'ya nazaran oldukça hızlı eğitim seçeneği sağlar
* GPU kurulumu için gereksinimleri sağlamıyorsanız CPU kurulumu \(tensorflow\) yapmanız tavsiye edilir
  * Ekran kartınızın **NVIDIA olması ve desteklemesi** gerekmektedir
  * Kontrol için [buraya](https://developer.nvidia.com/cuda-gpus) tıklayabilirsin

> Daha yüksek verim için tensorflow-gpu için ortam oluşturun

```bash
conda search tensorflow-gpu --info # Sürüme karar vermek için
conda install -c anaconda tensorflow-gpu=<versiyon> # Belirli sürümü indirme
conda install -c anaconda tensorflow-gpu=1.12.0 # Örnek
```

#### Sanal Ortama Tensorflow-GPU Kurulumu

Tensorflow için sanal ortam oluşturmak hız açısından daha faydalıdır.

```bash
conda create -n tensorflow-gpu tensorflow-gpu
conda activate tensorflow-gpu
```
{% endtab %}

{% tab title="🎃 Keras" %}
```bash
conda install -c conda-forge keras
```
{% endtab %}

{% tab title="🕵️‍♂️ Tesseract" %}
Resimden yazıyı çekmek için kullanılır.

```bash
conda install -c mcs07 tesseract
conda install -c jim-hart pytesseract
```

> [Pillow \(Python Image Library\)](./#paket-ve-kuetuephane-kurulumlari) paketinin de indirilmesi gerekebilir.
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

