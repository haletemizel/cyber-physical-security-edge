# Uç Bilişim Cihazlarında Siber-Fiziksel Güvenlik: Nesne Tespiti ile Fiziksel İhlal Tespiti

Bu proje, Gazi Üniversitesi TUSAŞ-Kazan Meslek Yüksekokulu Bilgi Güvenliği Teknolojisi bölümü kapsamında geliştirilmiştir.

## Proje Ekibi ve Kurum
* **Hale Temizel**
* **Nilay Tulu**
* **Kurum:** Gazi Üniversitesi TUSAŞ-Kazan Meslek Yüksekokulu, Bilgi Güvenliği Teknolojisi Bölümü

## Proje Amacı
Kritik altyapılar ve sunucu odalarına yönelik yetkisiz fiziksel erişimleri (saldırgan/ihlal durumlarını) gerçek zamanlı olarak tespit edebilen, internet bağlantısı gerektirmeyen (kapalı devre) bir Uç Yapay Zeka (Edge AI) savunma sistemi tasarlamaktır.

## Kullanılan Teknolojiler ve Yöntemler
* **YOLO Mimarileri:** Hafifletilmiş ve optimize edilmiş **YOLOv11** mimarisi kullanılmaktadır. Bu depodaki gerçek zamanlı çıkarım betiği (`scripts/inference.py`), Ultralytics kütüphanesi üzerinden **YOLOv11n** (nano) mimarisini kullanmaktadır.
* **Uç Bilişim (Edge Computing):** Raspberry Pi / NVIDIA Jetson uyumlu optimize altyapı
* **Veri Seti:** Açık kaynaklı *intruder-detection* veri seti
* **Dil ve Kütüphaneler:** Python, Ultralytics YOLO, OpenCV

## Model Mimarisi ve Eğitim Bilgisi
* **Model Mimarisi:** YOLOv11n (YOLOv11 Nano)
* **Eğitilmiş Model Ağırlığı:** `models/best.pt`
* **Açıklama:** Projede fiziksel ihlal ve yetkisiz erişim tespiti amacıyla kullanılan `models/best.pt` ağırlık dosyası, **YOLOv11n** mimarisi temel alınarak eğitilmiştir. Bu hafif mimari, kısıtlı kaynaklara sahip uç bilişim (Edge AI) cihazlarında yüksek kare hızı (FPS), düşük gecikme ve enerji verimliliği ile yüksek doğrulukta tespit gerçekleştirmektedir.

## Proje Yapısı
- `dataset/` : Eğitim ve test veri seti dosyaları. **Not:** Veri seti boyutu nedeniyle repoya dahil edilmemiştir; açık kaynaklı *intruder-detection* veri setinin bu klasöre yerleştirilmesi gerekmektedir.
- `models/` : Eğitilmiş model ağırlıkları (`best.pt` dosyası YOLOv11n mimarisiyle eğitilmiştir)
- `scripts/` : Eğitim ve gerçek zamanlı test betikleri (`inference.py`, `yolo11n.pt`)

## Kurulum ve Kullanım
```bash
pip install -r requirements.txt
cd scripts
python inference.py
```
