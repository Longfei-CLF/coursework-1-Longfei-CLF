import pytest
from tests.user import User

@pytest.fixture(scope='module')
def user():
   user = User(first_name='John', last_name='Smith', email='john@ucl.ac.uk', password='Password', dob = None)
   yield user