# Ozon Bank Test Task

Программа получает данные из Superhero API и находит самого высокого супергероя по полу и наличию работы.

## Запуск

```cmd
git clone https://github.com/EgorMishalkin/ozon_test-task.git
cd ozon_test-task
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python main.py
```

## Тесты

Запуск всех тестов:

```cmd
python -m pytest
```

Запуск отдельных групп тестов:

```cmd
python -m pytest tests/test_logic.py
python -m pytest tests/test_api.py
python -m pytest tests/test_smoke.py
```

* `test_logic.py` — логика поиска и проверка аргументов;
* `test_api.py` — HTTP-ошибки и повторные запросы;
* `test_smoke.py` — работа с реальным API.

## Использование функции в Python-коде

Функцию `highest_character()` можно импортировать в другой Python-файл.

Например, создайте в папке проекта файл `example.py`:

```python
from main import highest_character

hero = highest_character("Male", True)

print(hero["name"])
print(hero["appearance"]["height"][1])
print(hero["work"]["occupation"])
```

Запустите этот файл через командную строку:

```cmd
python example.py
```

Параметры функции:

* `gender` — `"Male"` или `"Female"`;
* `has_job` — `True` для героя с работой, `False` для героя без работы.

Герои с некорректно указанным ростом пропускаются.
