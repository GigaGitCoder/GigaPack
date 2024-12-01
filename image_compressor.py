import base64
from io import BytesIO
from PIL import Image


def compress_image(base64_image, target_size_kb=10):
    # Декодируем изображение из base64
    image_data = base64.b64decode(base64_image)

    # Открываем изображение с помощью Pillow
    image = Image.open(BytesIO(image_data))

    # Определяем целевой размер в байтах
    target_size_bytes = target_size_kb * 1024

    # Если изображение уже меньше целевого размера, возвращаем его
    if len(image_data) <= target_size_bytes:
        return base64_image

    # Сжимаем изображение
    quality = 95  # Начальное качество
    while True:
        # Создаем буфер для сохранения изображения
        buffer = BytesIO()

        # Сохраняем изображение в буфер с заданным качеством
        image.save(buffer, format="JPEG", quality=quality)

        # Получаем размер сжатого изображения
        compressed_image_data = buffer.getvalue()

        # Проверяем размер
        if len(compressed_image_data) <= target_size_bytes or quality <= 10:
            break

        # Уменьшаем качество для дальнейшего сжатия
        quality -= 5

    # Кодируем сжатое изображение обратно в base64
    compressed_base64_image = base64.b64encode(compressed_image_data).decode('utf-8')

    return compressed_base64_image
