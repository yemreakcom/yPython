---
description: >-
  Python ile Google Sheet verilerini otomatik olarak düzenleme, değiştirme,
  güncelleme
---

# 📑 Google Sheet Düzenleme

## 👮‍♂️ API ve İzinleri Oluşturma

* 👨‍💼 Google Cloud Platfowm üzerinden [Resource Manager](https://console.cloud.google.com/cloud-resource-manager) sayfasına girin
* **➕ Create Project** kısmından proje ismi oluşturun, ardından oluşturulan projeyi seçin
* ⚠️ Aşağıdaki işlemlerin her birini seçili projede yapmanız gerekmektedir
* 👆 [APIs & Services](https://console.cloud.google.com/apis/dashboard) kısmından [Enable APIs and Services](https://console.cloud.google.com/apis/library) butonuna tıklayın
* 👆 [Google Drive](https://console.cloud.google.com/apis/library/drive.googleapis.com) ve [Google Sheet](https://console.cloud.google.com/apis/library/sheets.googleapis.com) hizmetleri için **Enable** butonuna tıklayın
* ➕ [API & Services](https://console.cloud.google.com/apis/credentials) sayfasından **Create Credential** butonu ile projede kullanmak için kimlik oluşturun
  * **🗝 Service Accounts** alanı altından oluştulanı seçip **Keys** kısmından **Add Key** butonuna tıklayın
  * **📜 Create New Key**, ardından da **JSON** butonunu seçin ve kimlik bilgilerinizi json formatında indirin
* 📂 İndirdiğiniz dosyayı projenizin dizinine taşıyın,&#x20;
  * 👨‍💻 Kod üzerinden `gc = gspread.service_account(GS_CREDENTIAL_FILENAME)` komutu ile dosyaya erişeceğiz

{% hint style="warning" %}
📣 Uygulama ile erişmek istediğiniz Google Sheet dosyanızdan paylaşım ayarlarına girip **indirdiğiniz json** **dosyasındaki client\_email** **alanındaki e-posta adresi** ile paylaşın, aksi halde uygulama erişemez ve `SpreadSheetNotFound` hatası verir
{% endhint %}

## 👨‍💻 Kaynak Kod

* 📦 İlk olarak `pip install gspread` ile gerekli kütüphaneyi indiriyoruz
* 📄 Gspred kullanımı için detaylı bilgi arıyorsunuz [dokümantasyonuna](https://docs.gspread.org/en/v4.0.0/) bakabilirsiniz

{% hint style="warning" %}
💡 Aşağıdaki örnekte **Sheet2** üzerinden değişiklik yapıldığı için `GS_SHEET_INDEX` değeri 1'dir, normalde 0 olarak alabilirisiniz
{% endhint %}

```python
import gspread

GS_CREDENTIAL_FILENAME = "gs_credential.json"  # İndirilen json dosyası yolu
GS_FILENAME = "Cash Flow"  # Google Sheet dosyası adı
GS_SHEET_INDEX = 1  # Sheet2'e erişim için

gc = gspread.service_account(GS_CREDENTIAL_FILENAME)
wks = gc.open(GS_FILENAME).get_worksheet(GS_SHEET_INDEX)

# Formül ekleme
wks.update_acell("A1", "=2 * 10")

# Veri ekleme (formül ekleme çalışmaz)
wks.update("A2", "=123+122")

```

![](<../.gitbook/assets/Screen Shot 2021-08-06 at 13.41.36.png>)
