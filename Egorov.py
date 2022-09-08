# Первое задание
word = "лщклрапр"#input("Введите слово: ")

def first(word):
	for x in range(len(word)):
		if word[x] == "а":
			return x+1
	return False


def second(word):
	finished = False
	x = 0
	while not finished:
		if word[x] == "а":
			return x+1
		x+=1


print(first(word))
print(second(word))

# Второе задание

M = range(1,21)


for x in range(0,20):
	print(f"Если i = {M[x]}, то d={(M[x]-M[19])*(20*M[x])/2}")
