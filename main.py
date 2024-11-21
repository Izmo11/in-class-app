import addition
import subtraction
import division
import squareroot
import multiplication

print("Using addition")
x = add_two_numbers(1, 2)
print("1 + 2 = " + x)

print("Using subtraction:")
x = subtraction.subtract_two_numbers(10, 5)
print("10 - 5 = " + str(x))

print("Using multiplication:")
y = multiplication.multiply_two_numbers(4, 3)
print("4 * 3 = " + str(y))

print("Using square root:")
z = squareroot.square_root(16)
print("√16 = " + str(z))
