# Лабораторная работа №2 — Linux: права доступа и процессы

![Ubuntu](https://img.shields.io/badge/Ubuntu-24.04-E95420?logo=ubuntu&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-008000)

Материалы [лабораторной №2 курса AppSec](https://course.geminishkv.tech/labs/basic/lab02/).

Автор: Andrey Fedotov ([Akdkkras](https://github.com/Akdkkras)).

Группа: ИУ10-96.

## Окружение

Ubuntu 24.04.5 LTS в WSL2, Bash, Python 3.12.3, Pygame 2.6.1.
Графическое окно запускается через WSLg.

## Файлы

| Файл | Назначение |
|---|---|
| `pygamesteel.py` | Исходный пример с тремя намеренными ошибками; запуск даёт NameError. |
| `pygamesteel_fixed.py` | Исправленное приложение: белый фон и зелёное приветствие. |
| `test_privesc.sh` | Учебный скрипт, выводящий имя пользователя; SUID после опыта снят. |
| `screen` | Пустой файл для проверки чтения через группу readgroup. |
| `nmapres.txt` | Пустой файл с ACL для результатов следующей лабораторной. |

## Запуск

Из корня репозитория:

```bash
cd lab02
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pygame==2.6.1
python pygamesteel_fixed.py
```

Ожидается окно 800×600 с белым фоном и зелёной надписью
`Hello appsec world*` по центру. Закрытие крестиком завершает программу.

## Результаты опытов

- `screen`: владелец akdkkras, группа readgroup, права 640.
  Пользователь smallman читает файл, но не может записать в него.
- `nmapres.txt`: ACL пользователя smallman разрешает rw,
  ACL группы readgroup — r; маска rw, права остальных отсутствуют.
- Linux проигнорировал SUID у скрипта. Временная копия бинарника id
  с владельцем root получила euid=0 и сразу была удалена.
- При правах 770 оба пользователя удаляли чужие файлы.
  При 1770 каждый удалял только свои файлы.
  Учебный каталог shared принадлежит root:readgroup и оставлен пустым.
- В корневой файловой системе Ubuntu найдено 14 SUID-файлов.
  Поиск ограничен этой файловой системой через find -xdev.
- Процессы с управляющим терминалом и без него различены по полю TTY.

В пункте 4 updatedb не завершился за 10 минут и был прерван.
Оставшаяся проверка поиска по индексу пропущена; пункт выполнен частично.

ACL, владельцы и специальные биты действуют локально и обычным
Git-коммитом не переносятся. Пустой каталог shared также не сохраняется в Git.
