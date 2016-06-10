L = []
n = int(raw_input())
	for i in range(n+1):
		a = (raw_input().split(" "))
		if a[0] == 'insert':
		L.insert(int(a[1]),int(a[2]))
		if a[0] == 'print':
		print(L)
		if a[0] == 'remove':
		L.remove(int(a[1]))
		if a[0] == 'append':
		L.append(int(a[1]))
		if a[0] == 'sort':
		L.sort()
		if a[0] == 'pop':
		L.pop()
		if a[0] == 'reverse':
		L.reverse()
		if a[0] == 'index':
		L.index(int(a[1]))

