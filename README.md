[<img src='https://img.shields.io/badge/Python-3776AB?style=flat-square'><img src='https://img.shields.io/badge/3.13-23283d?style=flat-square'>](https://www.python.org/)
[<img src='https://img.shields.io/badge/beautifulsoup4-148024?style=flat-square'><img src='https://img.shields.io/badge/4.13-23283d?style=flat-square'>](https://www.python.org/)
[<img src='https://img.shields.io/badge/requests-0073b7?style=flat-square'><img src='https://img.shields.io/badge/2.32-23283d?style=flat-square'>](https://www.python.org/)
[<img src='https://img.shields.io/badge/tabulate-ffd343?style=flat-square'><img src='https://img.shields.io/badge/0.9-23283d?style=flat-square'>](https://www.python.org/)
[<img src='https://img.shields.io/badge/tqdm-cca8c4?style=flat-square'><img src='https://img.shields.io/badge/4.67-23283d?style=flat-square'>](https://www.python.org/)

<br>

# phpMyAdmin table parsing
Скрипт, который через HTTP-запросы авторизуется в интерфейсе **phpMyAdmin** и извлекает содержимое таблицы из базы данных.

<br>

### Разделы
- [Установка](#установка)
- [Переменные окружения](#описание-переменных-окружения)
- [Запуск](#запуск)

<br>

## Установка
Клонировать репозиторий и перейти в корневую директори:
```bash
git@github.com:SivikGosh/test_phpMyAdmin_parsing.git
cd test_phpMyAdmin_parsing/
```

Создать виртуальное окружение
```bash
python3.13 -m venv venv
source venv/bin/activate
```

Установить зависимости
```bash
pip3 install .
```

Добавить переменные окружения в **.env** файл (см. [Переменные окружения](#описание-переменных-окружения))
```bash
cp .env.exapmle .env
```

<br>

## Запуск
```bash
python3.13 -m src.main --db testDB --table users  # [!] аргументы обязательны
```

<br>

### Описание переменных окружения
| Переменная | Описание                       |
| ---------- | ------------------------------ |
| URL        | Адрес расположения phpMyAdmin. |
| LOGIN      | Имя пользователя.              |
| PASSWORD   | Пароль.                        |

<br>

<div align="right">

## Author's contact
<a href='https://t.me/sivikgosh' target='_blank'><img src='https://img.shields.io/badge/SivikGosh-white?style=flat-square&logo=Telegram&logoColor=26A5E4'></a>

</div>
