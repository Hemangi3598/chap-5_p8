# wapp to check for anagram

def mysort(s):
	d = sorted(s)
	ns = "".join(d)
	return ns

s1 = input("enter first string ")
s2 = input(" enter second string ")

if mysort(s1) == mysort(s2):
	print("yes")
else:
	print("no")
	