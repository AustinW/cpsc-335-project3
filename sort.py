'''
Austin White
austinw@csu.fullerton
10/25/2014

Project 3
Sorting Algorithms
Part 1 - Selection sort

Instructions:
1. loads the input file,
2. allows you to specify a value of n to use,
3. prints the first 10 words,
4. sorts the first n words,
5. measures the elapsed time of the sorting process,
6. prints out the first 10 words in the sorted sequence, and
7. prints the elapsed time.
'''

import sys, time

'''
In place selection sort developed in class with some python
additions to the pseudocode
'''
def ip_selection_sort(L):
	n = len(L)

	for k in range(n - 1):
		j = k
		for i in range(k+1, n):
			if L[i].lower() < L[j].lower():
				j = i
		# swap(L[k], L[j])
		L[k], L[j] = L[j], L[k]

	return L

'''
Selection sort developed in class
'''
def selection_sort(L):
	unsorted = L
	sorted = []

	while len(unsorted) > 0:
		least = unsorted[0]

		for e in unsorted:
			if e.lower() < least.lower():
				least = e

		unsorted.remove(least)
		sorted.append(least)

	return sorted

def do_selection_sort():
	filename = input("Specify a file to read (beowulf.txt): ")

	# Provide default option
	if filename == "":
		filename = "beowulf.txt"

	try:
		# 1. Load input file
		f = open(filename, "r")
	except:
		print("Invalid file specified")
		sys.exit(0)

	# 2. Specify n to use
	n = int(input("For what n? "))

	L = []

	i = 0
	for line in f:
		if i == n:
			break

		L.append(line.strip())

		i += 1

	# Be a good citizen
	f.close()

	# 3. Print the first 10 words
	print_first_lines(L, 10)

	print("In place selection sort...")

	start = time.perf_counter()

	# 4. Sort the first n words
	sorted = ip_selection_sort(L[:n])

	end = time.perf_counter()

	# 5. Measure running time
	elapsedTime = end - start

	# 6. Print the first 10 words in sorted sequence
	print("Sorted:")
	print_first_lines(sorted, 10)

	# 7. Print the elapsed time
	print("Elapsed time: " + str(elapsedTime) + " seconds")

def merge(AS, BS):
	merged = []
	ai = bi = 0

	while ai < len(AS) and bi < len(BS):
		if AS[ai].lower() <= BS[bi].lower():
			merged.append(AS[ai])
			ai += 1
		else:
			merged.append(BS[bi])
			bi += 1

	return merged + AS[ai:] + BS[bi:]

def merge_sort(L):
	n = len(L)

	if n <= 1:
		return L
	else:
		half = int(n / 2)
		A = L[:half]
		B = L[half:]

		return merge(merge_sort(A), merge_sort(B))

def do_merge_sort():
	filename = input("Specify a file to read (beowulf.txt): ")

	# Provide default option
	if filename == "":
		filename = "beowulf.txt"

	try:
		# 1. Load input file
		f = open(filename, "r")
	except:
		print("Invalid file specified")
		sys.exit(0)

	# 2. Specify n to use
	n = int(input("For what n? "))

	L = []

	i = 0
	for line in f:
		if i == n:
			break

		L.append(line.strip())

		i += 1

	# Be a good citizen
	f.close()

	# 3. Print the first 10 words
	print_first_lines(L, 10)

	print("Merge sort...")

	start = time.perf_counter()

	# 4. Sort the first n words
	sorted = merge_sort(L[:n])

	end = time.perf_counter()

	# 5. Measure running time
	elapsedTime = end - start

	# 6. Print the first 10 words in sorted sequence
	print("Sorted:")
	print_first_lines(sorted, 10)

	# 7. Print the elapsed time
	print("Elapsed time: " + str(elapsedTime))

def print_first_lines(inp, n):
	for i in range(0, n):
		print(str(i + 1) + ". " + inp[i])

def main():

	print("1. Selection Sort (s)")
	print("2. Merge Sort (m)")
	print("3. Quit (q)")

	ans = input("What would you like to do? ")

	if ans == "1" or ans == "s":

		do_selection_sort()

	elif ans == "2" or ans == "m":

		do_merge_sort()

	elif ans == "3" or ans == "q":
		print("\nGoodbye")
		sys.exit(0)
	elif ans != "":
		print("\nNot a valid choice, try again")

	sys.exit(0)

if __name__ == '__main__':
	main()