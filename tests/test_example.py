import pytest


@pytest.mark.parametrize('a, b, result',
                         [
                             (1, 3, 4),
                             (-1, 3, 2),
                             (1, 3, 4),
                             (1, 3, 4),
                         ])
def test_one(a, b, result):
    print('This is test run')


def test_two(start_stop_rest_service):
    print('This is test run')
