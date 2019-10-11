# 🖼 Python ile Görüntü İşleme Notları

## Median Alma

```python
import statistic

```

## Medyan Filtre

```python
final = cv2.medianBlur(source, 3)
```

## Resmi np.array Yapmak

OpenCV ile alırsak resim numpy formatında olur.

```python
import cv2
im = cv2.imread("abc.tiff",mode='RGB')
print type(im)
```

## Harici Bağlantılar

- [Noise filtering in Digital Image Processing](https://medium.com/image-vision/noise-filtering-in-digital-image-processing-d12b5266847c)
- [İki resmi birleştirme](https://stackoverflow.com/a/29108632/9770490)
- [Matplotlib resim işlemleri](https://matplotlib.org/3.1.1/tutorials/introductory/images.html)
