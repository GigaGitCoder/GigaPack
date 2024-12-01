import time
import requests, json
from api import headers

def export(template_id: str, File_Name: str):
    # Экспорт шаблона

    # Получени корневой папки экспортов
    url = "https://hygieia.fast-report.com/api/rp/v1/Exports/Root"
    # Отправка GET-запроса
    response = requests.get(url, headers=headers, verify=False)

    # Проверка статуса ответа
    if response.status_code == 200:
        print("Корневая папка получена!")
        print("Ответ:", response.json())  # Выводим ответ в формате JSON
        export_folder_id = response.json()['id']
    else:
        print("Произошла ошибка:", response.status_code)
        print("Ответ:", response.text)

    url = f"https://hygieia.fast-report.com/api/rp/v1/Templates/File/{template_id}/Export"
    data = {
        "folderId": export_folder_id,
        "fileName": "result.pdf",
        "format": "PDF",

    }


    success = False
    attempt = 0
    print("Создание экспорта")
    while not success and attempt <= 10:
        # Отправка POST-запроса
        response = requests.post(url, headers=headers, verify=False, data=json.dumps(data))

        # Проверка статуса ответа
        if response.status_code == 200:
            print("Запрос выполнен успешно!")
            print("Ответ:", response.json())  # Выводим ответ в формате JSON
            success = True
        else:
            print("Произошла ошибка:", response.status_code)
            print("Ответ:", response.text)
            time.sleep(3)
            attempt += 1


    # Получение файла
    export_id = response.json()["id"]
    url = f"https://hygieia.fast-report.com/download/e/{export_id}?preview=false"

    success = False
    attempt = 0
    print("Получение PDF")
    while not success and attempt <= 20:
        response = requests.get(url, headers=headers, verify=False)

        if response.status_code == 200:
            print("Запрос выполнен успешно!")
            pdf_content = response.content
            print("PDF файл успешно сохранен.")

            print("\n\n" + "=" * 40 +"\n            PDF файл успешно сохранен!\n" + "=" * 40 + "\n\n")
            success = True
        else:
            print("Произошла ошибка:", response.status_code)
            print("Ответ:", response.text)
            time.sleep(3)
            attempt += 1


    # Удаление экспорта
    url = f"https://hygieia.fast-report.com/api/rp/v1/Exports/File/{export_id}"
    success = False
    attempt = 0
    print("Удаление экспорта")
    while not success and attempt <= 10:
        response = requests.delete(url, headers=headers, verify=False)

        if response.status_code == 204:
            print("Запрос выполнен успешно!")
            print("Экспорт успешно удалён.")
            success = True
        else:
            print("Произошла ошибка:", response.status_code)
            print("Ответ:", response.text)
            time.sleep(3)
            attempt += 1

    # Удаление шаблона
    url = f"https://hygieia.fast-report.com/api/rp/v1/Templates/File/{template_id}"
    success = False
    attempt = 0
    print("Удаление шаблона")
    while not success and attempt <= 10:
        response = requests.delete(url, headers=headers, verify=False)

        if response.status_code == 204:
            print("Запрос выполнен успешно!")
            print("Экспорт успешно удалён.")

            print("\n\n" + "=" * 40 +"\n            Экспорт успешно удалён!\n" + "=" * 40 + "\n\n")
            success = True
        else:
            print("Произошла ошибка:", response.status_code)
            print("Ответ:", response.text)
            time.sleep(3)
            attempt += 1
    
    return pdf_content
