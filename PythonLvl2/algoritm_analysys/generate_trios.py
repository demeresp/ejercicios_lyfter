def generate_list_trios(list_a, list_b, list_c):
	
    #0(n^3) - Algorithm complexity
	result_list = []
	for element_a in list_a: #0(n)
		for element_b in list_b:#0(n)
			for element_c in list_c:#0(n)
				result_list.append(f'{element_a} {element_b} {element_c}')#0(1)
				
	return result_list 