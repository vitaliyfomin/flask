*Запускаем виртуальную среду venv*
```
.\venv\Scripts\activate.ps1
```

*Устанавливаем FLASK*
```
pip install flask
```
*Дополнительно может понадобиться обновить pip*

```
python.exe -m pip install --upgrade pip
```

*Проверяем список установленных библиотек*
```
pip freeze
```
*Библиотеки можно перенаправить в файл requirements.txt, используемый для хранения этих зависимостей*
```
pip freeze > requirements.txt
```
*Установка зависимостей из файла requirements.txt*
```
pip install -r requirements.txt
```
*Запускаем наш проект на flask*
```
python task01.py
```
*Деактивация виртуального окружения*
```
deactivate
```