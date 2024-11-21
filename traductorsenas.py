import cv2
import tkinter as tk
from PIL import Image, ImageTk
import mediapipe as mp

# Configurar MediaPipe para detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title("Traductor de Lengua de Señas")
root.geometry("800x600")

# Etiqueta para mostrar la traducción
translation_label = tk.Label(root, text="Traducción: ", font=("Helvetica", 18))
translation_label.pack()

# Crear un widget de etiqueta para mostrar el video
video_label = tk.Label(root)
video_label.pack()

# Captura de video
cap = cv2.VideoCapture(0)

def update_frame():
    # Leer el cuadro del video
    success, frame = cap.read()
    if not success:
        return

    # Procesar el cuadro con MediaPipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    # Dibujar los puntos de referencia de la mano
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Aquí podrías implementar la lógica de traducción basada en los landmarks detectados
            # Ejemplo: Traducción ficticia
            gesture_detected = "Candado"  # Esto debería ser el resultado de tu modelo de reconocimiento de señas
            translation_label.config(text=f"Traducción: {gesture_detected}")

    # Convertir la imagen para mostrarla en Tkinter
    frame_pil = Image.fromarray(frame)
    frame_tk = ImageTk.PhotoImage(image=frame_pil)
    video_label.imgtk = frame_tk
    video_label.config(image=frame_tk)

    # Llamar a esta función de nuevo después de 10 ms
    root.after(10, update_frame)

# Iniciar la actualización del video
update_frame()

# Iniciar el bucle principal de Tkinter
root.mainloop()

# Liberar el video cuando se cierra la ventana
cap.release()