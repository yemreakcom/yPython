# 💻 VsCode Üzerinde Python

## 🧩 Python Eklentileri

| Eklenti | Açıklama |
| :--- | :--- |
| 🐍 [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) | VsCode Dil desteği |
| [✨ DarkCode Theme](https://marketplace.visualstudio.com/items?itemName=yedhrab.darkcode-theme-adopted-python-and-markdown) | Python'a özel temam |
| 🏹 [Kite](https://marketplace.visualstudio.com/items?itemName=kiteco.kite) | AI destekli kod tamamlama |
| 🤖 [Visual Studio IntelliCode - **Preview**](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) | Sık kullanılan kod önerileri \(**eksik öneriler olabilir**\) |
| 📜 [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) | Dokümantasyon parçaları sağlayan eklenti |
| 🌈 [Bracket Pair Colorizer 2](https://marketplace.visualstudio.com/items?itemName=CoenraadS.bracket-pair-colorizer-2) | Parantezleri renklendirme |
| 🤖 [AREPL for python](https://marketplace.visualstudio.com/items?itemName=almenon.arepl) | Anlık çıktıları gösterme |

## 📏 Python Kodlarını Formatlama

* ✲ Ctrl + ⇧ Shift + `P` yapın
* Çıkan alana `Python: Select Linter` yazın
* `pylint` düzenleyicisini seçin
  * `pylint` aynı dizindeki modulleri bulamamakta, bu hatananın çözümü için `.pylintrc` dosyasını düzenlemek gerekmekte
  * `pylint --generate-rcfile .pylintrc` komutunu çalışma dizininde yazdıktan sonra, içini açıp `#init-hook` satırını `init-hook='import sys; system.path.append("${workspaceFolder}")'` ile değiştirin. \(Yorum satırı olmaktan kaldırın\)
  * Eğer girintiyi ⭾ Tab ile yapıyorsanız `pylint`'de _bug_'a sebebiyet vermekte, SPACE kullanın
* Python derleyicinize `autopep8` paketini aşağıdaki komutlarla veya VsCode arayüzü ile yükleyin
  * `pip install autopep8`
  * `conda install autopep8`
* Artık ⇧ Shift + ⎇ Alt + `F` ile kodları __düzenleyebilirsiniz.
* Dosyaya sağ tıklayarak derleyebilirsiniz.

## 🔨 Python Ayarlamaları

{% tabs %}
{% tab title="🐛 Debug Yapılandırması" %}
Detaylar için [buraya](https://code.visualstudio.com/docs/python/debugging) bakabilirsin.

* ✲ Ctrl + ⇧ Shift + `D` ile debug ekranını açın
* Sol üstte açılan ekrandan `ayarlar butonuna` tıklayın
* `Python` kısmını seçin

> Değişkenin objelerini ve değerlerini öğrenmek için debug çok faydalıdır 🌟
{% endtab %}

{% tab title="👐 Jupyter Desteği" %}
* Kod alanının üstüne `#%%` yazarak oluşturabilirsiniz.
* Detaylar için [buraya](https://code.visualstudio.com/docs/python/jupyter-support) bakabilirsin.
{% endtab %}

{% tab title="👨‍🔧 Derleyici Ayarlama" %}
Aktif olan derleyici ortamı, en altta bulunan durum çubuğunun solunda gösterilmektedir, değiştirmek için:

* ✲ Ctrl + ⇧ Shift + `P` tuş kombinasyonuna basın
* Çıkan alana `Python: Select Interpreter` yazınız
* Çıkan ekrandan istediğiniz derleyiciyi seçiniz
{% endtab %}

{% tab title="🔗 Diğer Ayarlar" %}
{% embed url="https://code.visualstudio.com/docs/python/settings-reference" %}
{% endtab %}
{% endtabs %}

##  🚩 Pythonpath Ayarlamaları

{% tabs %}
{% tab title="✨ Pythonpath Oluşturma" %}
* Çalışma dizininde `.env` dosyası oluşturun
* `.env` dosyasının içerisine `PYTHONPATH=` satırını ekleyin
  * Örnek için bir alttaki başlığa bakınız
* VsCode ayarlarına `"python.envFile": "${workspaceFolder}/.env"` satırını ekleyin
* VsCode'u yeniden başlatın

{% hint style="info" %}
Kaynak için [buraya](https://github.com/Microsoft/vscode-python/issues/3840#issuecomment-463789294) bakabilirsin. Ek olarak [buraya](https://stackoverflow.com/a/54083402/9770490) bakmanda da fayda var
{% endhint %}
{% endtab %}

{% tab title="⭐ Pythonpath Örneği" %}
Resmi döküman için [buraya](https://code.visualstudio.com/docs/python/environments#_environment-variable-definitions-file) bakabilirsin.

* VsCode birden fazla satıra sahip değişken değerlerini kabul etmez
* Ortam değişklenleri oluşturmak için proje ayarlarından **env file** seçmemiz gerekmekte
* Ardından içine değişkenlerimizi tanımlamamız gerkemekte

```javascript
"python.envFile": "${workspaceFolder}/prod.env"
```

```bash
# prod.env
# Python kaynak dizinleri
RESEARCH_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research
OBJECT_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research/object_detection
SLIM_FOLDER=C:/Users/YEmre/Documents/Tensorflow/models/research/slim
SCRIPT_FOLDER=C:/Users/YEmre/Documents/Tensorflow/scripts

# Python modül yolu
PYTHONPATH=${RESEARCH_FOLDER}:${OBJECT_FOLDER}:${SLIM_FOLDER}:${SCRIPT_FOLDER}
```

```bash
PYTHONPATH=./src:${PYTHONPATH}
```
{% endtab %}
{% endtabs %}

