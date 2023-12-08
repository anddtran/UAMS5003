import pytest
from FSM_simple import check, my_fsm

#test the check functions
def testchecktrue():
    assert check('010101010101') == True, 'This is a valid string of 0\'s and 1\'s'

def testcheckfalse():
    assert check('abc') == False, 'string of nonbinary characters'
    assert check('012345') == False, 'string of characters that are not just 0 or 1'

#test the my_fsm function
@pytest.mark.parametrize("current_state, current_transition, expected_state", [
    ('A', '1', 'E'),
    ('A', '0', 'B'),
    ('B', '1', 'D'),
    ('B', '0', 'C'),
    ('C', '0', 'E'),
    ('C', '1', 'E'),
    ('D', '0', 'E'),
    ('D', '1', 'D'),
    ('E', '0', 'E'),
    ('E', '1', 'E')
])

def test_my_fsm(current_state, current_transition, expected_state):
    assert my_fsm(current_state, current_transition) == expected_state, f"Failed at state {current_state} with transition {current_transition}"
