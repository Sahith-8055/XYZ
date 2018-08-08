"""Exercise : Function and Objects Exercise-1"""
def apply_to_each(L, f):
	for i in range(len(L)):
		L[i] = f(L[i])
	return L	
def main():
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))
if __name__ == "__main__":
    main()
