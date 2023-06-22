import os
import cv2


video = cv2.VideoCapture(r"C:/Users/dimit/OneDrive/Documentos/videoPy/teste.mp4")

if video.isOpened() == False:
    print()
    print("Erro: não foi possível ler a câmera.")


height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("Height: ", height)
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
print("Width: ", width)
fps = video.get(cv2.CAP_PROP_FPS)
print("FPS: ",fps)

novoVideo = cv2.VideoWriter(r"C:/Users/dimit/OneDrive/Documentos/videoPy/novoTeste.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

while True:
    retorno, frame = video.read()
    cv2.imshow("Video", frame)
    novoVideo.write(frame)
    if cv2.waitKey(25) == 32:
        break

video.release()
novoVideo.release()
cv2.destroyAllWindows()
