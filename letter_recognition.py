import cv2
import pytesseract

def recognize_armenian_letter(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    # Предварительная обработка изображения
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Распознавание текста с помощью Tesseract
    config = '--psm 10 --oem 3 -l hye'  # Установка параметров для армянского языка
    text = pytesseract.image_to_string(gray, config=config)

    return text.strip()

# Пример использования
image_path = 'armenian_picture.png'  # Путь к изображению с буквой армянского алфавита
letter = recognize_armenian_letter(image_path)
print("Распознанная буква:", letter)