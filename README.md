# Uç Bilişim Cihazlarında Siber-Fiziksel Güvenlik: Nesne Tespiti ile Fiziksel İhlal Tespiti

Bu proje, Gazi Üniversitesi TUSAŞ-Kazan Meslek Yüksekokulu Bilgi Güvenliği Teknolojisi bölümü kapsamında geliştirilmiştir.

## Proje Amacı
Kritik altyapılar ve sunucu odalarına yönelik yetkisiz fiziksel erişimleri (saldırgan/ihlal durumlarını) gerçek zamanlı olarak tespit edebilen, internet bağlantısı gerektirmeyen (kapalı devre) bir Uç Yapay Zeka (Edge AI) savunma sistemi tasarlamaktır.

## Kullanılan Teknolojiler ve Yöntemler
* **YOLO Mimarileri:** Hafifletilmiş YOLO modelleri (YOLOv8/v9/v10/v11)[cite: 1, 2]
* **Uç Bilişim (Edge Computing):** Raspberry Pi / NVIDIA Jetson uyumlu optimize altyapı[cite: 1, 2]
* **Veri Seti:** Açık kaynaklı *intruder-detection* veri seti[cite: 1, 2]
* **Dil ve Kütüphaneler:** Python, Ultralytics YOLO, OpenCV

## Proje Yapısı
- `dataset/` : Eğitim ve test veri seti dosyaları
- `models/` : Eğitilmiş model ağırlıkları (`.pt`)
- `scripts/` : Eğitim ve gerçek zamanlı test betikleri (`inference.py`)