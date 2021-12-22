# ModuleNotFoundError: No module named 'user'
# Solution: add the path of user.py into sys path
import sys
sys.path.append('/Users/Longfei/OneDrive - University College London/Longfei/Uni/CEng/Y3/Software engineering/coursework-1-Longfei-CLF')

import pytest
from user import User

# Create a new general public user
@pytest.fixture(scope='module')
def user():
   user = User(first_name='John', last_name='Smith', email='john@ucl.ac.uk', password='Password', dob = 'dateofbirth')
   yield user