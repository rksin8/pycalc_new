# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    num0, num1 = float(num0), float(num1)
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    elif operator == '*':
        return num0 * num1
    elif operator == '/':
        return num0 / num1
    else:
        print('unknown operator!')
        print("basic edit")
        return None


# this is some random text to test merge conflict
# this and that
# use module x for y
# :wq


# add this line to test merge confilt 
