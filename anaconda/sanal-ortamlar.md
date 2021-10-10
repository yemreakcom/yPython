# 🌇 Sanal Ortamlar | Conda

## 🚴‍♂️ Giriş 

* 💁‍♂️ Sanal ortamlar üzerine çalışmak istediğimiz projeler için kurulur ve gerekmediği vakit kaldırılır.

{% hint style="success" %}
Projelerin bağımlılıkları arasında çakışma olmasını engeller.
{% endhint %}

## 🏗️ Oluşturma

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

## 🐣 Aktif Etme

```bash
conda activate <ortam_ismi>
conda activate myenv # Örnek
```

> Ortam seçildiğinde (base) yazan kısımda (`<ortam_ismi>`) yazar.

## 🐥 Pasif Etme

```bash
conda deactivate
```

## 💦 Kaldırma

```bash
conda env remove -n <ortam_ismi>
conda env remove -n myenv # Örnek
```

{% hint style="info" %}
Anaconda Prompt `base` ortamına geri döner.
{% endhint %}

