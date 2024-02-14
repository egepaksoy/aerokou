import cv2

# Video kaydı için kullanılacak dosya adı ve çözünürlüğü
video_adı = 'kaydedilen_video.mp4'
video_cozunurlugu = (640, 480)

# Video kayıt nesnesini başlat
video_kaydi = cv2.VideoWriter(video_adı, cv2.VideoWriter_fourcc(*'mp4v'), 60.0, video_cozunurlugu)

# Kamera nesnesini başlat (0, yerleşik kamerayı temsil eder)
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan bir çerçeve al
    ret, cerceve = kamera.read()

    # Eğer çerçeve alınamazsa döngüyü sonlandır
    if not ret:
        break

    # Çerçeveyi görüntüle
    cv2.imshow('Video Kaydı', cerceve)

    # Video kaydı için çerçeveyi yaz
    video_kaydi.write(cerceve)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kullanılan kaynakları serbest bırak
kamera.release()
video_kaydi.release()

# Pencereyi kapat
cv2.destroyAllWindows()
