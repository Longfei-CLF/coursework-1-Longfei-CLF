from user import User

def test_create_full_name(user):
    """ 
    GIVEN the values 2, 4, 8 and 20 
    WHEN the values are passed to the minimum function 
    THEN the result should equal 2 
    """
    full_name = User.create_full_name(user)
    assert full_name == "John Smith"