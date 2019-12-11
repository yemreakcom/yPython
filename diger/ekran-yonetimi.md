# 🔳 Ekran Yönetimi

## 💠 Ekran Yönetimi Metotları

{% tabs %}
{% tab title="💾 Ekran Görüntüsünü Alma ve Kaydetme" %}
```python
from PIL import ImageGrab as ig

import numpy as np
import time
import cv2

# Hata ayıklama ve bilgilendirme notlarını aktif edery
DEBUG = True

# Çıktı kaydını aktif etme
KEEP = False

# Yakalanacak ekranın konum bilgileri (x0, y0, x1, y1)
CAPTURE_AREA = (80, 101, 1111, 923)

# Yakalanan ekranın gösterilme boyutu (Varsayılan için 0 yapın)
WIDTH = 0
HEIGHT = 0

# FPS sayacını tanımlama
if DEBUG:
    frame_count = 0
    last_time = time.time()

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'XVID'),
    5.0,
    (CAPTURE_AREA[2] - CAPTURE_AREA[0], CAPTURE_AREA[3] - CAPTURE_AREA[1])
) if KEEP else None

while True:
    screen = ig.grab(bbox=CAPTURE_AREA)
    screen_np = np.array(screen)

    # BGR tipindeki görüntüyü RGB yapıyoruz
    screen_np_RGB = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)

    # Gösterilecek ekranın boyutunu ayarlama
    screen_width = WIDTH if WIDTH != 0 else CAPTURE_AREA[2] - CAPTURE_AREA[0]
    screen_height = HEIGHT if WIDTH != 0 else CAPTURE_AREA[3] - CAPTURE_AREA[1]

    # Kaydedilen ekranı uygun boyutta görüntüleme
    cv2.imshow(
        'Ekran görüntüsü',
        cv2.resize(
            screen_np_RGB,
            (
                screen_width,
                screen_height
            )
        )
    )

    # Dosyaya yazma
    out.write(screen_np_RGB) if KEEP else None

    # 'q' tuşuna basıldığında çıkma işlemi
    if cv2.waitKey(25) & 0xFF == ord('q'):
        out.release() if KEEP else None
        cv2.destroyAllWindows()
        break

    # FPS bilgilerini hesaplama ve ekrana basma
    if DEBUG:
        frame_count += 1
        if time.time() - last_time >= 1:
            print('FPS: {}'.format(frame_count))
            frame_count = 0
            last_time = time.time()
```
{% endtab %}

{% tab title="🟦 Kısayol ile Ekran Alanı Seçme" %}
```python
def draw_dimension(hotkey="ctrl_l") -> tuple:
    """Ekrandan seçilen alanın koordinatlarını verir

    Keyword Arguments:
        hotkey {string} -- Klavye kısayolu (default: {None})

    Returns:
        tuple -- Seçilen alanın koordinatları `(x0, y0, x1, y1)`
    """

    # Farenin başlangıç ve bitiş konumları
    start_position, end_position = (0, 0)

    def listen_keyboard():
        with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
            keyboard_listener.join()

    def on_press(key):
        # Başlangıç koordinatlarını oluşturma
        if key == keyboard.Key[hotkey]:
            nonlocal start_position
            start_position = mouse.Controller().position

    def on_release(key):
        # Bitiş koordinatlarını başlangıca ekleme
        if key == keyboard.Key[hotkey]:
            nonlocal end_position
            end_position = mouse.Controller().position

            # Dinleyiciyi kapatma
            return False

    print(
        f"Seçmek istediğiniz alanın başlangıç noktasına farenizi getirin ve {hotkey} tuşuna basılı tutarak farenizi alanın bitiş noktasına götürün.")

    listen_keyboard()
    return start_position + end_position

print(draw_dimension())
```
{% endtab %}
{% endtabs %}

