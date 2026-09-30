def print_10_or_less_elements(list_to_print):
	# 0(n) - Algorithm complexity
	list_len = len(list_to_print) # 0(1)
	for index in range(min(list_len, 10)): # 0(n)
		print(list_to_print[index]) # 0(1)