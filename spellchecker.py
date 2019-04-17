fd= open('wiki.hist', 'r')
words = fd.read()
split = words.split()

input=str(input("Enter a Sentence: "))
input2= input.split()

for texts in input2:
	if texts  in split:
		print(texts, end=' ')
	else:
		print(texts + '*', end=' ')
print()
