from user import User

def test_calculate_age(user):
    """ 
    GIVEN the values 2, 4, 8 and 20 
    WHEN the values are passed to the minimum function 
    THEN the result should equal 2 
    """
    age = User.calculate_age(user)
    assert age == "21"