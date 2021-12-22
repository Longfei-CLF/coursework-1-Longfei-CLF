# ModuleNotFoundError: No module named 'user'
# Solution: add the path of user.py into sys path
import sys
sys.path.append('/Users/Longfei/OneDrive - University College London/Longfei/Uni/CEng/Y3/Software engineering/coursework-1-Longfei-CLF')

# Start test
from user import User

def test_create_full_name(user):
    """ 
    GIVEN the first name is "John" and the last name is "Smith"
    WHEN the values are passed to full name creation function
    THEN the result should be "John Smith"
    """
    full_name = User.create_full_name(user)
    assert full_name == "John Smith"