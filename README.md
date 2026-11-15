# ІДЗ — Частина 1

## Завдання 1.1. Unit-тестування

Файл `security_utils.py` містить функцію `validate_password`, а
`test_security.py` — окремі pytest-тести для позитивного сценарію,
короткого пароля, відсутності цифр і двох варіантів забороненого слова `admin`.

### Локальний запуск

```bash
python -m pip install pytest
pytest test_security.py
```

Очікувано: усі 5 тестів мають завершитися зі статусом `PASSED`.

## Завдання 1.2. GitHub Actions

Файл `.github/workflows/tests.yml` автоматично встановлює Python 3.12,
pytest і pytest-cov та запускає тести з вимірюванням покриття коду
після кожного `push`.

### Як опублікувати проєкт на GitHub

1. Створіть порожній репозиторій на GitHub.
2. Відкрийте термінал у кореневій папці цього проєкту.
3. Виконайте команди, підставивши URL власного репозиторію:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/ВАШ_ЛОГІН/НАЗВА_РЕПОЗИТОРІЮ.git
git push -u origin main
```

4. На GitHub відкрийте вкладку **Actions** і перевірте, що workflow
`Python Tests` завершився успішно.

Примітка: створення репозиторію та `git push` потрібно виконати у вашому
власному GitHub-акаунті. Файли проєкту й налаштування CI вже підготовлені.
