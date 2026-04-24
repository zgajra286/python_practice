#  Check that a tuple type cannot be changed in python.
 
T = (1,2,"abc")

try:
        T[0] = 100
except TypeError:
        print("tuple is immutable")