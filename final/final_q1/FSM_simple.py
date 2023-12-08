import sys


def check(a_string):
    tmp = list(a_string)
    for item in tmp:
        if item not in {'0', '1'}:
            valid = False
            break
    else:
        valid = True
    return valid


def my_fsm(current_state, current_transition):
    if current_state == 'A':
        if current_transition == '1':
            return 'E'
        else:
            return 'B'
    elif current_state == 'B':
        if current_transition == '1':
            return 'D'
        else:
            return 'C'
    elif current_state == 'C':
        return 'E'
    elif current_state == 'D':
        if current_transition == '1':
            return 'D'
        else:
            return 'E'
    else:
        return 'E'


if __name__ == '__main__':
    my_string = sys.argv[1]
    if check(my_string):
        state = 'A'
        for transition in list(my_string):
            state = my_fsm(state, transition)
        else:
            if state in {'C', 'D'}:
                print(f"String Accepted")
            else:
                print(f"String Rejected")
    else:
        print(f"Invalid String it should contain only 0's and 1's")
