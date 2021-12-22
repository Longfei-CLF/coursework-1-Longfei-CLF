# ModuleNotFoundError: No module named 'user'
# Solution: add the path of user.py into sys path
import sys
sys.path.append('/Users/Longfei/OneDrive - University College London/Longfei/Uni/CEng/Y3/Software engineering/coursework-1-Longfei-CLF')

# Start test
from user import User

def test_calculate_age(user):
    """ 
    GIVEN the date of birth is a string
    WHEN the users are passed to the age calculation function
    THEN the result should be "Age not calculated, date of birth wrong"
    """
    age = User.calculate_age(user)
    assert age == "Age not calculated, date of birth wrong"