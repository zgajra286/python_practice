# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
for i in range(2):
    values = input("Enter values: ")
    s.add(values)

print(type(s))
