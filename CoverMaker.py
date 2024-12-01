from export import export
from api import headers
from datetime import datetime
from image_to_url import getImageUrl
import requests
import random
import json, base64

def coverMake(data):

    print("Начало")
    MM_multiplier = 3.78  # multiplier to convert mm to inches
    StyleName = data["template"]

    # Page and Cover dimensions
    Pwidth_Cwidth = float(data["coverWidth"])
    Pheight_Cheight = float(data["coverHeight"])

    # Cover settings
    Border_Width = float(data["borderWidth"])
    Border_Color = data["borderColor"][4:-1]
    BG_Color = data["coverColor"][4:-1]

    # Pictures settings
    Pics_N = 0
    Pics_Hei = float(data["imageWidthHeight"])
    Pics_Wid = float(data["imageWidthHeight"])
    Pics_Colums = int(data["columns"])
    Pics_Lines = int(data["rows"])
    Pics_Hyperlinks_List = getImageUrl(data["imageFiles"])

    # Rotation settings
    Random_Rotation = 0
    Rotate = 0
    Rotation_Degree = 0
    if data["rotate"] == "Random":
        Random_Rotation = 1
    elif data["rotate"] == "Yes":
        Rotate = 1
        Rotation_Degree = int(data["rotationDegrees"])
    else:
        pass

    # Offset settings
    Offset_Left = (Pwidth_Cwidth * MM_multiplier - Pics_Wid * MM_multiplier * Pics_Colums) / (Pics_Colums + 1)
    Offset_Top = (Pheight_Cheight * MM_multiplier - Pics_Hei * MM_multiplier * Pics_Lines) / (Pics_Lines + 1)

    # Создаем начало шаблона
    last_str = f"""<?xml version="1.0" encoding="utf-8"?>
    <Report ScriptLanguage="CSharp" ReportInfo.Created="{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}" ReportInfo.Modified="{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}" ReportInfo.CreatorVersion="2025.1.1.0">
    <Dictionary/>
    <ReportPage Name="CoverP" PaperWidth="{Pwidth_Cwidth}" PaperHeight="{Pheight_Cheight}" BottomMargin="0" TopMargin="0" LeftMargin="0" RightMargin="0" Watermark.Font="Arial, 60pt">
        <ReportTitleBand Name="CoverT" Width="{Pwidth_Cwidth}" Height="{Pheight_Cheight}">
        <ShapeObject Name="Cover" Width="{Pwidth_Cwidth * MM_multiplier}" Height="{Pheight_Cheight * MM_multiplier}" Border.Color="{Border_Color}" Border.Width="{Border_Width}" Fill.Color="{BG_Color}"/>
    """



    # Style - BigMinCover
    if StyleName == "BigMinCover":
        for i in range (Pics_Colums):
            if Pics_Lines % 2 == 0:
                Pics_N += 1
            for j in range (Pics_Lines):
                Pics_N += 1
                if Pics_N % 2 == 1:
                    last_str += f"""
                        <PictureObject 
                        Name="Picture{Pics_N}" 
                        Left="{Offset_Left * (i + 1) + Pics_Wid * MM_multiplier * i + Offset_Left * 0.2 * random.choice([-1, 1])}" 
                        Top="{Offset_Top * (j + 1) + Pics_Hei * MM_multiplier * j + Offset_Top * 0.2 * random.choice([-1, 1])}" 
                        Width="{Pics_Hei * MM_multiplier}" 
                        Height="{Pics_Wid * MM_multiplier}" 
                        Angle="{random.randint(0, 360) * Random_Rotation + Rotate * Rotation_Degree}" 
                        ImageFormat="Png" 
                        ImageLocation="{random.choice(Pics_Hyperlinks_List)}"/>
                    """
                else:
                    last_str += f"""
                        <PictureObject 
                        Name="Picture{Pics_N}" 
                        Left="{(Offset_Left * (i + 1) + Pics_Wid * MM_multiplier * i) + (Pics_Hei * MM_multiplier / 4) + Offset_Left * 0.2 * random.choice([-1, 1])}" 
                        Top="{(Offset_Top * (j + 1) + Pics_Hei * MM_multiplier * j) + (Pics_Wid * MM_multiplier / 4) + Offset_Top * 0.2 * random.choice([-1, 1])}" 
                        Width="{Pics_Hei * MM_multiplier / 2}" 
                        Height="{Pics_Wid * MM_multiplier / 2}" 
                        Angle="{random.randint(0, 360) * Random_Rotation + Rotate * Rotation_Degree}" 
                        ImageFormat="Png" 
                        ImageLocation="{random.choice(Pics_Hyperlinks_List)}"/>
                    """


    # Style - ChessCover
    elif StyleName == "ChessCover":
        for i in range (Pics_Colums):
            for j in range (Pics_Lines):
                Pics_N += 1
                if Pics_N % 2 == 1:
                    last_str += f"""
                        <PictureObject 
                        Name="Picture{Pics_N}" 
                        Left="{Offset_Left * (i+1) + Pics_Wid * MM_multiplier * i + Offset_Left * 0.2 * random.choice([-1, 1])}" 
                        Top="{Offset_Top * (j+1) + Pics_Hei * MM_multiplier * j + Offset_Top * 0.2 * random.choice([-1, 1])}" 
                        Width="{Pics_Hei * MM_multiplier}" 
                        Height="{Pics_Wid * MM_multiplier}" 
                        Angle="{random.randint(0, 360) * Random_Rotation + Rotate * Rotation_Degree}" 
                        ImageFormat="Png" 
                        ImageLocation="{random.choice(Pics_Hyperlinks_List)}"/>
                    """

    # Style - DefaultCover
    elif StyleName == "DefaultCover":
        for i in range (Pics_Colums):
            for j in range (Pics_Lines):
                Pics_N += 1
                last_str += f"""
                    <PictureObject 
                    Name="Picture{Pics_N}" 
                    Left="{Offset_Left * (i+1) + Pics_Wid * MM_multiplier * i + Offset_Left * 0.2 * random.choice([-1, 1])}" 
                    Top="{Offset_Top * (j+1) + Pics_Hei * MM_multiplier * j + Offset_Top * 0.2 * random.choice([-1, 1])}" 
                    Width="{Pics_Hei * MM_multiplier}" 
                    Height="{Pics_Wid * MM_multiplier}" 
                    Angle="{random.randint(0, 360) * Random_Rotation + Rotate * Rotation_Degree}" 
                    ImageFormat="Png"
                    ImageLocation="{random.choice(Pics_Hyperlinks_List)}"/>
                """



    last_str += f"""
        </ReportTitleBand>
    </ReportPage>
    </Report>
    """

    url = "https://hygieia.fast-report.com/api/rp/v1/Templates/Root"
    # Отправка GET-запроса
    response = requests.get(url, headers=headers, verify=False)

    # Проверка статуса ответа
    if response.status_code == 200:
        print("Корневая папка получена!")
        print("Ответ:", response.json())  # Выводим ответ в формате JSON
        template_folder_id = response.json()['id']
    else:
        print("Произошла ошибка:", response.status_code)
        print("Ответ:", response.text)


    File_Name = f'{StyleName} W={Pwidth_Cwidth}mm H={Pheight_Cheight}mm B={Border_Width} {datetime.now().strftime("%m_%d_%Y %H_%M_%S")}'
    url = f"https://hygieia.fast-report.com/api/rp/v1/Templates/Folder/{template_folder_id}/File"
    data = {
        "name": File_Name,
        "content": base64.b64encode(last_str.encode("utf-8")).decode("utf-8")
    }

    # Отправка POST-запроса
    response = requests.post(url, headers=headers, verify=False, data=json.dumps(data))

    # Проверка статуса ответа
    if response.status_code == 200:
        print("Запрос выполнен успешно!")
        print("Ответ:", response.json())  # Выводим ответ в формате JSON
        template_id = response.json()['id']

        print("\n\n" + "=" * 40 + "\n            Шаблон успешно создан!\n" + "=" * 40 + "\n\n")
    else:
        print("Произошла ошибка:", response.status_code)
        print("Ответ:", response.text)

    # Export And Delete
    return export(template_id, File_Name)
