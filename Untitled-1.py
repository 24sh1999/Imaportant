for t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	flag = True
	for i in range(n - 1):
		d = a[i] - b[i]
		if a[i] < b[i] or a[i + 1] - d < b[i + 1]:
			flag = False 	
			break
		else:
			a[i + 1] -= d
	if flag == False or a[n - 1] != b[n - 1]:
		print("NO")
	else:
		print("YES")


        