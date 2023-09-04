import pytest


@pytest.fixture(scope='session')
def start_stop_rest_service(start_db):
    print('Start Rest service')
    yield
    print('Stop Rest service')


@pytest.fixture(scope='session')
def start_db():
    print('Start DB')
    yield
    print('Stop DB')
