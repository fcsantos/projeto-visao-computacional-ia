import cv2
from cvzone.HandTrackingModule import HandDetector

# inicializa a webcam
webcam = cv2.VideoCapture(0)

# inicializa o detector de mãos
rastreador = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    # captura a imagem da webcam
    sucesso, imagem = webcam.read()

    # detecta as mãos no quadro
    hands, imagem_maos = rastreador.findHands(imagem)

    # mostra o quadro com as marcações
    cv2.imshow("Projeto Visao computacional IA", imagem_maos)

    # Encerra a aplicação quando qualquer tecla é pressionada
    if cv2.waitKey(1) != -1:
        break

# libera a webcam e fecha as janelas
webcam.realease()
cv2.destroyAllWindows()