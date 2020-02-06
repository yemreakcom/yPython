# ✨ Faydalı İşlemler

## 📑 PDF İşlemleri

PDF işlemleri için pdfkit modülü kullanılır.

* `pip install pdfkit` ile modülü indirin
* Modül için gerekli [wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf/releases) aracını indirin
* İndirdiğiniz aracın içerisindeki `wkhtmltopdf.exe` dosyasının yolunu bulun
  * İleride yapılandırma ayarı için kullanılacaktır
* İşlemler sırasında python kodunun çalıştırıldığı yola dikkat edin

> Farklı bir modül için [buraya](https://towardsdatascience.com/python-for-pdf-ef0fac2808b0) bakabilirsin

```python
import pdfkit

path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

pdfkit.from_file('file.html', 'out.pdf', configuration=config)
```

## 📊 İstatistiksel İşlemler

{% tabs %}
{% tab title="Median Alma" %}
```python
import statistic
```
{% endtab %}

{% tab title="Medyan Filtre" %}
```python
final = cv2.medianBlur(source, 3)
```
{% endtab %}
{% endtabs %}



