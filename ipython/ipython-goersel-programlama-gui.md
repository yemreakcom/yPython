---
description: IPython Görsel Programlama (GUI)
---

# 🔆 Görsel Arayüz \(GUI\)

## 📃 Form Oluşturma İşlemleri \(GUI\)

* Form komutları `#@` ile başlar

```python
#@title ## Model Kullanma Aracı { vertical-output: true, display-mode: "form" }

#@markdown - Markdown örneği
#@markdown     - Madde1

#@markdown - Markdown örneği
#@markdown     - Madde2

str_obj = "ssd" #@param {type:"string"}
list_obj = "train" #@param ["model_main", "train", "export_inference_graph"]
slider = 20000 #@param {type:"slider", min:100, max:20000, step:100}
bool_obj = False #@param {type:"boolean"}
```

## ⭕ Progress Bar

```python
from IPython.display import HTML, display
import time

def progress(value, max=100):
    return HTML("""
        <progress
            value='{value}'
            max='{max}',
            style='width: 100%'
        >
            {value}
        </progress>
    """.format(value=value, max=max))

out = display(progress(0, 100), display_id=True)
for ii in range(101):
    time.sleep(0.02)
    out.update(progress(ii, 100))
```

