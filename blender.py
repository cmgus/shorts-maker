import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread('backgrounds/final.jpg')

# Convertir la imagen a formato de punto flotante
image_float = image.astype(np.float32) / 255.0

# Reducir la opacidad multiplicando por un factor entre 0 y 1
opacity = 0.5  # Cambia este valor para ajustar la opacidad (0.0 - 1.0)
blended_image = image_float * opacity

# Convertir la imagen de nuevo a formato de 8 bits sin signo
blended_image = (blended_image * 255).astype(np.uint8)

# Guardar la imagen resultante
cv2.imwrite('backgrounds/final-back.jpg', blended_image)