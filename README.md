# AppSec Lab 01 — Git SCM

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Typer](https://img.shields.io/badge/Typer-0.29.2-009688)

Учебный CLI для приветствия пользователя. Проект создан при выполнении
[лабораторной работы №1 курса AppSec](https://course.geminishkv.tech/labs/basic/lab01/).

Автор: Andrey Fedotov ([Akdkkras](https://github.com/Akdkkras)).
Группа: ИУ10-96.

## Возможности

- Имя пользователя передаётся обязательным аргументом.
- Фамилия задаётся опцией `--lastname`.
- Формальный режим включается через `--formal` или `-f`.
- Справка доступна через `--help`.

## Установка

Проверенное окружение: Ubuntu 24.04 в WSL2, CPython 3.12.3.

```bash
git clone https://github.com/Akdkkras/appsec-lab01.git
cd appsec-lab01
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Версии зависимостей зафиксированы в `requirements.txt`.
В Ubuntu для создания окружения требуется пакет `python3-venv`.

## Запуск

```bash
python typersteel.py --help
python typersteel.py Andrey
python typersteel.py Andrey --lastname Fedotov --formal
python typersteel.py Andrey --lastname Fedotov -f
```

Обычный режим выводит:

```
Привет, Andrey!
```

Оба варианта формального режима выводят:

```
Добрый день, Andrey Fedotov!
```

## Проверка изменений

```bash
git diff --check
```

После изменения программы повторите четыре команды из раздела «Запуск»:
проверьте справку и соответствие приветствий приведённым результатам.

## История лабораторной

- [PR №1](https://github.com/Akdkkras/appsec-lab01/pull/1):
  переход от интерактивного скрипта к CLI на Typer, добавление комментариев.
- [PR №2](https://github.com/Akdkkras/appsec-lab01/pull/2):
  изменение стиля, воспроизведение конфликта, rebase и ручное разрешение.

Учебные коммиты подписаны GPG. После rebase переписанный коммит подписан заново.
