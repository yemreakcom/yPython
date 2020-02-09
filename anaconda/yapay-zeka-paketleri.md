# 🧠 Yapay Zeka Paketleri \| Conda

## 🏹 Tensorflow

{% tabs %}
{% tab title="🎛️ Tensorflow CPU" %}
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
{% endtab %}

{% tab title="🚀  Tensorflow-GPU" %}
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
{% endtabs %}

## 🎃 Keras

```bash
conda install -c conda-forge keras
```

## 🕵️‍♂️ Tesseract

Resimden yazıyı çekmek için kullanılır.

```bash
conda install -c mcs07 tesseract
conda install -c jim-hart pytesseract
```

> [Pillow \(Python Image Library\)](./#paket-ve-kuetuephane-kurulumlari) paketinin de indirilmesi gerekebilir.

## 

