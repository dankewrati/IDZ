import pytest

from security_utils import validate_password


def test_valid_password():
    """Пароль відповідає всім вимогам."""
    assert validate_password("Super_User_2026") is True


def test_password_too_short():
    """Пароль коротший за 8 символів."""
    assert validate_password("Abc123") is False


def test_password_without_digits():
    """Пароль містить лише літери."""
    assert validate_password("SuperUser") is False


def test_password_with_admin_mixed_case():
    """Заборонене слово admin у змішаному регістрі."""
    assert validate_password("Admin12345") is False


def test_password_with_admin_inside():
    """Заборонене слово admin всередині пароля."""
    assert validate_password("root_admin_pass") is False
