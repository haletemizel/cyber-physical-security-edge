# Uç Bilişim Cihazlarında Siber-Fiziksel Güvenlik: Nesne Tespiti ile Fiziksel İhlal Tespiti

Bu proje, Gazi Üniversitesi TUSAŞ-Kazan Meslek Yüksekokulu Bilgi Güvenliği Teknolojisi bölümü kapsamında geliştirilmiştir.

## Proje Ekibi ve Kurum
* **Hale Temizel**
* **Nilay Tulu**
* **Kurum:** Gazi Üniversitesi TUSAŞ-Kazan Meslek Yüksekokulu, Bilgi Güvenliği Teknolojisi Bölümü

## Proje Amacı
Kritik altyapılar ve sunucu odalarına yönelik yetkisiz fiziksel erişimleri (saldırgan/ihlal durumlarını) gerçek zamanlı olarak tespit edebilen, internet bağlantısı gerektirmeyen (kapalı devre) bir Uç Yapay Zeka (Edge AI) savunma sistemi tasarlamaktır.

## Kullanılan Teknolojiler ve Yöntemler
* **YOLO Mimarileri:** Hafifletilmiş YOLO modelleri (YOLOv8/v9/v10/v11). Bu depodaki gerçek zamanlı çıkarım betiği (`scripts/inference.py`), Ultralytics kütüphanesi üzerinden **YOLOv8n** (nano) mimarisini kullanmaktadır; YOLOv9/v10/v11 ise aynı Ultralytics arayüzüyle denenebilecek alternatif hafif mimariler olarak değerlendirilmektedir.
* **Uç Bilişim (Edge Computing):** Raspberry Pi / NVIDIA Jetson uyumlu optimize altyapı
* **Veri Seti:** Açık kaynaklı *intruder-detection* veri seti
* **Dil ve Kütüphaneler:** Python, Ultralytics YOLO, OpenCV

## Proje Yapısı
- `dataset/` : Eğitim ve test veri seti dosyaları. **Not:** Veri seti boyutu nedeniyle repoya dahil edilmemiştir; açık kaynaklı *intruder-detection* veri setinin bu klasöre yerleştirilmesi gerekmektedir.
- `models/` : Eğitilmiş model ağırlıkları (`.pt`)
- `scripts/` : Eğitim ve gerçek zamanlı test betikleri (`inference.py`)

## Kurulum ve Kullanım
```bash
pip install -r requirements.txt
cd scripts
python inference.py
```