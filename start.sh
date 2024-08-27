#!/bin/bash

# Останавливаем скрипт при ошибке
set -eu

# Настраиваем буферизацию вывода Python, чтобы видеть логи в режиме реального времени
export PYTHONUNBUFFERED=true

# Создаем виртуальное окружение
VIRTUALENV=.venv

if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALENV
fi

# Устанавливаем pip, если он еще не установлен
if [ ! -f $VIRTUALENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | $VIRTUALENV/bin/python
fi

# Устанавливаем зависимости
$VIRTUALENV/bin/pip install -r requirements.txt

# Запускаем приложение
$VIRTUALENV/bin/python3 bot.py
