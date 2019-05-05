"""Tests for phone assistant"""

from unittest import mock
import pytest
from phone_assistant import read_from_db


def test_case_1():
    """First test case"""

    with mock.patch('phone_assistant.sqlite3') as mock_sql:
        mock_sql.connect().cursor().fetchall.return_value = [('380675674432',),
                                                             ('380672832500',),
                                                             ('380983567721',)]
        result = read_from_db('380')
        assert result == [380675674432, 380672832500, 380983567721]
        assert isinstance(result, list)
        assert len(result) <= 10


def test_case_2():
    """Second test case"""

    with mock.patch('phone_assistant.sqlite3') as mock_sql:
        mock_sql.connect().cursor().fetchall.return_value = [('380675674432',),
                                                             ('380672832500',)]
        result = read_from_db('38067')
        assert result == [380675674432, 380672832500]
        assert isinstance(result, list)
        assert len(result) <= 10


def test_case_3():
    """Third test case"""

    with mock.patch('phone_assistant.sqlite3') as mock_sql:
        mock_sql.connect().cursor().fetchall.return_value = [('380983567721',)]
        result = read_from_db('380983')
        assert result == [380983567721]
        assert isinstance(result, list)
        assert len(result) <= 10


def test_empty():
    """Empty result test"""

    with mock.patch('phone_assistant.sqlite3') as mock_sql:
        mock_sql.connect().cursor().fetchall.return_value = []
        result = read_from_db('8098')
        assert result == []
        assert isinstance(result, list)


@pytest.fixture(scope='session')
def get_test_data():
    """Test data"""

    return [('380675', [('380675592288',), ('380675344544',)]),
            ('380954', [('380954971217',)]),
            ('380983', [('380983009520',)])]


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Read data from db"""

    print('\nFetching data from db')
    yield
    print('\nSaving test run data in db')


def test_case_db(get_test_data):
    for data in get_test_data:
        argv = data[0]
        expected = [int(x[0]) for x in data[1]]
        assert read_from_db(argv) == expected
