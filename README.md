<h1 align="center">GigaPack</h1>

> 🏆 Этот проект был разработан в рамках IX межрегионального хакатона «RinHack» (29 ноября - 01 декабря 2024) <br>
> <img src="https://img.icons8.com/fluency/48/000000/microsoft-powerpoint-2019.png" width="20" height="20"/> **[Презентация проекта](GigaPack.pptx)** 

> RinHack - межрегиональный хакатон, организованный Ростовским государственным экономическим университетом (РИНХ), посвященный вопросам кибербезопасности, искусственному интеллекту и разработке программного обеспечения. Мероприятие проходит в Центре истинных ценностей (г. Ростов-на-Дону).

**GigaPack** — это веб-приложение для создания уникальных подарочных обёрток по заданным параметрам пользователя. С помощью GigaPack вы можете легко и быстро создать индивидуальную упаковку для любого подарка, выбирая цвет, стиль и другие характеристики.

## 🛠 Технологии

* <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="13" height="13"/> Python
* <img src="https://static.djangoproject.com/img/icon-touch.e4872c4da341.png" width="13" height="13"/> Django
* <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="13" height="13"/> HTML5
* <img src="https://upload.wikimedia.org/wikipedia/commons/6/62/CSS3_logo.svg" width="13" height="13"/> CSS3
* <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg" width="13" height="13"/> JavaScript
* <img src="https://yt3.googleusercontent.com/ytc/AIf8zZRL5lBi2as7dUbkjbYm7uJZw_bt3kOFrjE1t8yD=s900-c-k-c0x00ffffff-no-rj" width="13" height="13"/> API сервиса "МоиОтчеты облако"
* <img src="https://imageban.ru/favicon.ico" width="13" height="13"/> API сервиса "imageban"

## 🚀 Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/GigaGitCoder/GigaPack.git
cd GigaPack
```

2. Создайте и активируйте виртуальное окружение:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. ⚠️ ВАЖНО: Настройка API-ключей
   - Получите API-ключ с сервиса "МоиОтчеты облако" и вставьте его в файл `api.py`
   - Получите Auth-token с сервиса "imageban" и вставьте его в файл `image_to_url.py`

5. Выполните миграции базы данных:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Запустите сервер разработки:
```bash
python manage.py runserver
```

## 📝 Использование

1. Откройте браузер и перейдите по адресу `http://localhost:8000`
2. Выберите параметры для создания обёртки
3. Загрузите изображение или выберите готовый шаблон
4. Настройте параметры под свои потребности
5. Сгенерируйте и скачайте готовую обёртку

## 👥 Команда разработчиков

<table>
  <tr>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/GigaGitCoder.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Егор Холкин</b><br />
      <sub><i>Тимлид, Full-stack разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Разработка основного алгоритма генерации обёрток<br />
      • Основной дизайн проекта<br />
      • Full-stack разработка<br />
      • Координация команды
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/GigaGitCoder">GitHub</a> • <a href="https://t.me/IgorXmel">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/Anton2442.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Антон Михайличенко</b><br />
      <sub><i>Backend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Работа с предоставленным API<br />
      • Скриптовая часть проекта<br />
      • Backend разработка
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/Anton2442">GitHub</a> • <a href="https://t.me/Kish242">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/Xqyat.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Роман Колесников</b><br />
      <sub><i>Frontend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Frontend разработка<br />
      • Разработка дизайна<br />
      • JavaScript разработка
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/Xqyat">GitHub</a> • <a href="https://t.me/Forliot">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/dencraz.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Даниил Сапронов</b><br />
      <sub><i>Frontend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Frontend разработка<br />
      • Разработка дизайна<br />
      • JavaScript разработка
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/dencraz">GitHub</a> • <a href="https://t.me/dencraz">Telegram</a>
      </div>
    </td>
    <td align="center" style="border: 1px solid #555;">
      <img src="https://github.com/DynamitNS.png" width="100" height="100" style="border-radius: 50%" alt="avatar"><br />
      <b>Сергей Товмасян</b><br />
      <sub><i>Frontend разработчик</i></sub>
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <div align="left">
      <b>Вклад в проект:</b><br />
      • Frontend разработка<br />
      • Разработка дизайна<br />
      • UI/UX дизайн
      <hr style="border: 1px solid #555; margin: 10px 0;">
      <b>Контакты:</b><br />
      <a href="https://github.com/DynamitNS">GitHub</a> • <a href="https://t.me/DynamitNS">Telegram</a>
      </div>
    </td>
  </tr>
</table>

## 📄 Лицензия

Этот проект лицензирован под лицензией Apache-2.0. Подробности в файле [LICENSE](LICENSE).

## 🤝 Вклад

Если вы хотите внести свой вклад в проект, пожалуйста, создайте форк репозитория, внесите изменения и отправьте пулл-реквест. Мы будем рады вашему участию!

## 💬 Поддержка

Если у вас есть вопросы или предложения, вы можете связаться с нами через Telegram. Мы всегда рады помочь!

Спасибо за использование GigaPack!
