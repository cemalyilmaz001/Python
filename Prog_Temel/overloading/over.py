# Overloading

def add(a=0, b=0, c=0):
	sayac = 0
	if a >= 1:
		sayac += 1

	if b >= 1:
		sayac += 1

	if c >= 1:
		sayac += 1

	return ((a + b + c) / int(sayac))

print(add(2, 3))     # Output: 2.5
print(add(2, 3, 4))  # Output: 3.0
