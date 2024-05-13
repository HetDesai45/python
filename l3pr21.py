def evenodd(mix):
	evenlist = []
	oddlist = []
	for i in mix:
		if (i % 2 == 0):
			evenlist.append(i)
		else:
			oddlist.append(i)
	print("Even lists:", evenlist)
	print("Odd lists:", oddlist)

mix = [2, 10, 45, 18, 93, 63, 75]
evenodd(mix)
