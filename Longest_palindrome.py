def longestPalindrome(a, n):
    pair1 = [0]*n 
    pair2 = [0]*n 
    r = 0
    for i in range(n):
        print("me")
        s = a[i] 
	s = s[::-1]
	for j in range(i + 1, n):
            if (a[i] != "" and a[j] != ""):
                if (s == a[j]):
                    pair1[r] = a[i] 
		    pai

    s1 = "" 

    for i in range(n):
        s = a[i] 
	a[i] = a[i][::-1] 
	if (a[i] != ""): 
	    if (a[i] == s):
                s1 = a[i] 
		break

    ans = "" 

    for i in range(r):
        ans = ans + pair1[i] 
	
	if (s1 != ""): 
            ans = ans + s1 
	
	for j in range(r - 1, -1, -1): 
            ans = ans + pair2[j] 
	print(ans) 

a1 = ["aba", "aba"] 
n1 = len(a1) 
longestPalindrome(a1, n1) 

a2 = ["abc", "dba", "kop","abd", "cba"] 
n2 = len(a2) 
longestPalindrome(a2, n2) 
