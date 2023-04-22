---
description: >-
  My Network → Connection alanındaki tüm bağlantıları ilk kişiden itibaren tek
  tek kaldıran script
---

# 🧹 LinkedIn üzerindeki bağlantıları temizleme

## 🔰 Hızlı Bakış

* `My Network` → `Connection` alanındaki tüm bağlantıları ilk kişiden itibaren tek tek kaldıran script
  * İşlem için alttaki URL’e veya manuel olarak gerekli alana giriş yapın
  * [https://www.linkedin.com/mynetwork/invite-connect/connections/](https://www.linkedin.com/mynetwork/invite-connect/connections/)
* Tarayıcınızda `Console`'u açıp, alttaki kaynak kodunu kopyalayın
  * _Kopyalamadan önce incelemenizi tavsiye ederim_ 😅
  * `*Console`'u nasıl açacağını bilmeyenler Google veya ChatGPT üzerinden aratabilir\* 💁‍♂️

{% hint style="info" %}
Ufak hatalar ve gecikmeler olabiliyor, **sayfayı yenileyin** ve baştan çalıştırın
{% endhint %}

## 👨‍💻 Kaynak Kod

{% code overflow="wrap" lineNumbers="true" %}
```javascript
collections = document.getElementsByClassName("artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view mn-connection-card__dropdown-trigger artdeco-button--tertiary artdeco-button--muted artdeco-button--circle p1")

async function waitForPopupAndClick(class_name, index) {
    return new Promise(resolve => {
        let interval = setInterval(() => {
            let popup = document.getElementsByClassName(class_name)[index];
            console.log(popup)
            if (popup) {
                clearInterval(interval);
                popup.click()
                resolve();
            }
        }, 100);
    });
}

async function waitForCollectionSizeToChange(collection, expectedSize) {
    return new Promise(resolve => {
        let interval = setInterval(() => {
            if (collection.length === expectedSize) {
                clearInterval(interval);
                resolve();
            }
        }, 100);
    });
}


function clickAndWait(expectedSize) {
    if (expectedSize === 2) {
        console.log("Done", expectedSize, collections.length)
        return
    }
    console.log("waiting ang clicking...", expectedSize, collections.length)
    waitForCollectionSizeToChange(collections, expectedSize).then(() => {
        collections[0].click()
        waitForPopupAndClick("display-flex align-items-center t-14 t-black--light t-normal", 2).then(() => {
            waitForPopupAndClick("artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view", 0).then(() => {
                console.log(`Removed, col:${collections.length} expected:${expectedSize - 1}`)
                clickAndWait(expectedSize - 1)
            })
        })
    })
}

// collections.length
clickAndWait(collections.length)
```
{% endcode %}
