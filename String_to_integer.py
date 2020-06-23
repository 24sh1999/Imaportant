def solutions(data):
	s = []
	data = data.lstrip()
	try:
		for i in range(len(data)):
			s.append(int(data[i]))
		s = int(''.join(map(str,s)))
		return  s

	except:
		s = int(''.join(map(str,s)))
		if  s <= 2147483647 and s >= -2147483647:
			return s
		elif s > 2147483647:
			return 2147483647
		elif s < -2147483647:
			return -2147483647
