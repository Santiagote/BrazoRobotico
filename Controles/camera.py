import cv2

def grabar_objetos():
    cap = cv2.VideoCapture(0)  # 0 es el índice de la cámara, ajusta según sea necesario

    while True:
        ret, frame = cap.read()  # Leer un solo frame
        if not ret:
            break

        # Aquí puedes procesar el frame si lo necesitas
        # Por ejemplo, podrías aplicar algoritmos de detección de objetos

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Presiona 'q' para salir del bucle
            break

    cap.release()
    cv2.destroyAllWindows()