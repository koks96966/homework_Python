# homework_Python
## Создание отчетов в Allure Report
### Как запустить тесты для формирования отчёта
- Запуск всех тестов с Allure-отчётом
```
pytest --alluredir=allure-results
```
- Запуск конкретного теста или группы тестов
По имени теста:
```
pytest -k "test_shop_lesson7" --alluredir=allure-results
```
Для конкретного файла/класса/метода:
```
pytest lesson_10\shop_lesson10.py --alluredir=allure-results
```
### Как просмотреть сформированный отчёт
- через Allure CLI
```
allure serve allure-results
```
Команда запустит локальный сервер и автоматически откроет отчёт в браузере.