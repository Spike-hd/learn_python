"""""
Question 1 :

Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""


def fct1():
	liste=[]
	i = 2000
	while i <= 3200:
		if i % 7 == 0 and i % 5 != 0:
			liste.append(str(i))
		i+=1
	else: # en sortie de boucle (pas aligner avec if le else concerne la boucle pas le if)
		phrase = ", ".join(liste)
		print(phrase)


""""
Question 2:

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
Then, the output should be: 40320
"""

def fct2(n):
	if (n == 1):
		return (1)
	else :
		return n * (fct2(n-1))


"""""
Question:

With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
such that is an integral number between 1 and n (both included).
And then the program should print the dictionary.
Suppose the following input is supplied to the program: 8
Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""


def fct3(n):
	dico={}
	i = 1
	while (i <= n):
		dico.update({i : i*i})
		i += 1
	else:
		print(dico)

""""
Autre maniere de faire interessante
def fct3(n):
	n = int(input())
	dic = {}
	for i in range (1,n+1):
		dic[i] = i * i
	print(dic)
"""




def main():
	# q1
	fct1()

	#q2
	n = int(input())
	print(fct2(n))

	#q3
	n = int(input())
	fct3(n)

if __name__ == "__main__":
	main()
