import pytest
from company_table import Database

DATABASE_URL = "postgresql://postgres:qweqweffq124a@localhost:5432/QA"


@pytest.fixture
def db():
    return Database(DATABASE_URL)
