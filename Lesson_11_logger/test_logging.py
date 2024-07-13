import pytest

from Lesson_11_logger.homework_10 import log_event


@pytest.mark.parametrize("username,status,expected", [('Name', 'success', 'success'),
                                                      ('Name', 'expired', 'expired'),
                                                      ('Name', 'error', 'error')])
def test_logging(username, status, expected):
    log_event(username, status)
    with open("login_system.log", 'r') as f:
        last_line = f.readlines()[-1]
    assert last_line.endswith(f'{expected}\n')