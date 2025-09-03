from app.main import check_1800
import pytest


@pytest.mark.parametrize(
    "string, expected_set",
    [
        (
            "1-800-CODE-WAR",
            {
                "1-800-CODE-WAR",
                "1-800-CODE-YAP",
                "1-800-CODE-WAS",
                "1-800-CODE-ZAP",
            },
        ),
        (
            "1-800-BOY-ARMY",
            {"1-800-BOY-ARMY", "1-800-COW-ARMY", "1-800-ANY-ARMY"},
        ),
        (
            "1-800-INK-WANT",
            {"1-800-INK-WANT", "1-800-HOLY-ANT", "1-800-HOLY-COT"},
        ),
        ("1-800-WORD-WTF", set()),
        ("1-800-WORD-TTT", set()),
        ("1-800-QQQQ-YOU", set()),
        ("1-800-XXXX-XXX", {"1-800-XXXX-XXX", "1-800-XXX-XXXX"}),
        ("1-800-SEX-TOYS", {"1-800-SEX-TOYS"}),
        ("1-800-BIG-JOHN", {"1-800-BIG-JOHN"}),
    ],
)
def test_check_1800(string, expected_set):
    assert check_1800(string) == expected_set, (
        f"Function should return {expected_set} " f"when s is equal to {string}"
    )
