---
description: Anaconda & miniconda üzerinde conda ile paket kurulumları
---
# 📦 Paket Kurulumları | Conda

## 🚴‍♂️ Kurulumlara Giriş

Paket kurulumları `conda` komutu yardımıyla yapılır.

* Tüm bu işlemlerin **Anaconda Prompt** üzerinde yapıldığına emin olun!
* Sanal ortama yükleme yapılmadan önce sanal ortamın **aktif edilmesi** gerekmektedir!

```bash
conda install pip # 👨‍💼 Pip
conda install -c anaconda numpy # 🧮 Numpy
conda install opencv # 👁‍🗨 OpenCV
```

## 🌍 Selenium

Web siteleri üzerinde işlem yapmak için kullanılır.

```bash
conda install -c conda-forge selenium
conda install -c clinicalgraphics selenium-chromedriver
```

## 🎴 Pillow

* 🖼️ Python resim kütüphanesi resim için kullanılır.

```bash
conda install -c anaconda pillow
```

## 🐍 Python Sürümü

```bash
conda create -n $PYTHON36_ENV_NAME python=3.6 anaconda  # set custom env name
```

##
