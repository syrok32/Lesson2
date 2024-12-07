# Проект Django: Catalog

![Django](https://img.shields.io/badge/Django-4.x-green)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Описание

**Catalog** — это учебный проект на Django, предназначенный для отработки навыков работы с веб-фреймворком Django. Проект включает в себя базовый функционал приложения: домашняя страница, страница контактов, и форму обратной связи.

## Структура проекта

1. **Домашняя страница (`home.html`)**
   - Отображает приветственное сообщение.
   - Использует стили Bootstrap для базовой стилизации.
   
2. **Страница контактов (`contacts.html`)**
   - Содержит контактную информацию.
   - Включает форму обратной связи (доп. задание).

3. **Приложение `catalog`**
   - Реализует логику для отображения страниц и обработки формы обратной связи.

## Установка и запуск

### Шаг 1: Настройка окружения

Создайте директорию для проекта и настройте виртуальное окружение:

```bash
mkdir catalog_project
cd catalog_project
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
