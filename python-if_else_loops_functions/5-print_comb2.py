#!/usr/bin/python3
for i in range (0, 99):
	if i < 10:
		print("0{}", end=', ' .format(i))
	else:
		print("{}", end=', ' .format(i))
print("99")
