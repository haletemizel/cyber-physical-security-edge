import cv2
from ultralytics import YOLO

# Eğittiğimiz YOLOv11 modelini yüklüyoruz
model = YOLO("yolo11n.pt")

# Kamerayı başlatıyoruz (0: Varsayılan bilgisayar kamerası)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Model ile nesne tespiti yapma
    results = model(frame)

    # Tespit edilen kutuları ekrana çizdirme
    annotated_frame = results[0].plot()

    cv2.imshow("Siber-Fiziksel Guvenlik - Ihlal Tespiti", annotated_frame)

    # Çıkmak için klavyeden 'q' tuşuna basın
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()