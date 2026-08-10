import pytest
from company_table import Database

DATABASE_URL = "PLACE URL"


@pytest.fixture
def db():
    return Database(DATABASE_URL)
