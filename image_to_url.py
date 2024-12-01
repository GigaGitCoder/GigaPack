import requests
from image_compressor import compress_image

def getImageUrl(image_list: list):
    url = "https://api.imageban.ru/v1"
    headers = {
        # Получаем Token на Imageban (Вставляем вместо -)
        "Authorization": "TOKEN -",
        "User -Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36"
    }

    url_list = []
    for image in image_list:
        image = compress_image(image.split(",")[1])

        data = {
            "image": image
        }

        response = requests.post(url, headers=headers, data=data)

        # Проверка статуса ответа
        if response.status_code == 200:
            print("Запрос выполнен успешно!")
            print("Ссылка на изображение получена.")
            url_list.append(response.json()["data"]["link"])
        else:
            print("Произошла ошибка:", response.status_code)
            print("Ответ:", response.text)


    return url_list
