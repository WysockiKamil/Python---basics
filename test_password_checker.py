from password_checker import password_strenght_checker
import pytest
@pytest.mark.parametrize(
    "password, expected_result",
    [
        # Puste hasło
        ("", "Password cannot be empty"), 
        # Słabe hasło
        ("12345678", "Słabe hasło"),
        ("12345", "Słabe hasło"),
        ("abcdefgh", "Słabe hasło"),
        ("abcdefgh1", "Słabe hasło"),
        ("abcdefgh!", "Słabe hasło"),
        # Średnie hasło
        ("Abcdefgh1", "Średnie hasło"),
        ("Abcdefgh!", "Średnie hasło"),
        ("12345678!", "Średnie hasło"),
        # Silne hasło
        ("Abcdefgh1!", "Silne hasło"),
        ("Abcdefgh1@#", "Silne hasło")
    ]
)
def test_password_strength_checker(password, expected_result):
    result = password_strenght_checker(password)
    assert result == expected_result