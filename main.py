from addition import add_two_numbers
from subtraction import subtract_two_numbers
from multiplication import multiply_two_numbers
from squareroot import square_root

# Test addition
print("Using addition:")
x = add_two_numbers(1, 2)
print("1 + 2 = " + str(x))

# Test subtraction
print("Using subtraction:")
y = subtract_two_numbers(10, 5)
print("10 - 5 = " + str(y))

# Test multiplication
print("Using multiplication:")
z = multiply_two_numbers(4, 3)
print("4 * 3 = " + str(z))

# Test square root
print("Using square root:")
w = square_root(16)
print("√16 = " + str(w))
