from oper import operate
import pytest

def test_operate():

    ## Testing additions
    assert operate(4, 2, '+') == 6, "integer addition"
    assert operate(4, 0.25, '+') == 4.25, "float addition"

    ## Testing subtractions
    assert operate(4, 5, '-') == -1, "integer subtraction"
    assert operate(4, 3.75, '-') == 0.25, "float subtraction"

    ## Testing multiplications
    assert operate(4, 5, '*') == 20, "integer multiplication"
    assert operate(4, 0.1, '*') == 0.4, "float multiplication"

    ## Testing divisions
    assert operate(4, 2, "/") == 2, "integer division"
    assert operate(0.06, 0.3, "/") == 0.2, "float division"

    ## Testing exceptions
    with pytest.raises(ZeroDivisionError) as excinfo0:
        operate(4, 0, "/")
    assert excinfo0.value.args[0] == "division by zero is " + \
                                     "undefined"

    with pytest.raises(ValueError) as excinfo1:
        operate(4, 0, "string")
    assert excinfo1.value.args[0] == "oper must be one of '+', " + \
                                     "'/', '-', or '*'"
    
    with pytest.raises(TypeError) as excinfo2:
        operate(4, 0, 1)
    assert excinfo2.value.args[0] == "oper must be a string"
