import pytest

from security_utils import validate_password


def test_valid_password():
    assert validate_password("Super_User_2026") is True


def test_password_too_short():
    assert validate_password("Abc123") is False


def test_password_without_digits():
    assert validate_password("SuperUser") is False


def test_password_with_admin_mixed_case():
    assert validate_password("Admin12345") is False


def test_password_with_admin_inside():
    assert validate_password("root_admin_pass") is False
