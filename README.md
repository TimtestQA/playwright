# Playwright UI Tests

## Структура проекта

- `tests/` — тестовые сценарии
- `pages/` — Page Object Model (POM)
- `utils/` — вспомогательные модули
- `conftest.py` — фикстуры pytest для Playwright

## Быстрый старт

1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Установите браузеры:
   ```bash
   playwright install
   ```
3. Запустите тесты:
   ```bash
   pytest
   ``` 