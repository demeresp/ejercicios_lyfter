def check_if_lists_have_an_equal(list_a, list_b):
	
    #0(n^2) - Algorithm complexity
	for element_a in list_a: #0(n)
		for element_b in list_b: #0(n)
			if element_a == element_b: #0(1)
				return True
				
	return False