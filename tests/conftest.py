import random
import pytest
import os
import tempfile

from blog.models import Article


# @pytest.fixture
# def random_name():
#     names = ['John', 'Jane', 'Marry']
#     return random.choice(names)


# def test_fixture_usage(random_name):
#     assert random_name


# @pytest.fixture
# def some_fixture():
#     # do something before test
#     yield  # test runs here
#     # do something after test


@pytest.fixture(autouse=True)
def database():
    _, file_name = tempfile.mkstemp()
    os.environ['DATABASE_NAME'] = file_name
    Article.create_table(database_name=file_name)
    yield
    os.unlink(file_name)
