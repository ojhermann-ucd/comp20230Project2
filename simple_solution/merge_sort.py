def merge_dict_supply_fill_cache(d1, d2):

	# create the return object 
	d = {}

	# get smallest elements until one dict is empty
	while len(d1) > 0 and len(d2) > 0:

		# create the traverse objects
		d1_small, d2_small = next(iter(d1)), next(iter(d2))

		# put the smallest score into the return dictionary
		if d1[d1_small] < d2[d2_small]:
			d[d1_small] = d1[d1_small]
			del d1[d1_small]
		else:
			d[d2_small] = d2[d2_small]
			del d2[d2_small]

	# add remaining elements
	while len(d1) > 0:
		d1_small = next(iter(d1))
		d[d1_small] = d1[d1_small]
		del d1[d1_small]
	while len(d2) > 0:
		d2_small = next(iter(d2))
		d[d2_small] = d2[d2_small]
		del d2[d2_small]

	# return
	return d

def merge_sort_dict_supply_fill_cache(d):

	# objects
	d1 = {}
	d2 = {}
	length = len(d)
	middle = int(length / 2)

	if len(d) > 1:
		for i in range(0, middle, 1):
			next_item = next(iter(d))
			d1[next_item] = d[next_item]
			del d[next_item]

		for i in range(middle, length, 1):
			next_item = next(iter(d))
			d2[next_item] = d[next_item]
			del d[next_item]

		d1 = merge_sort_dict_supply_fill_cache(d1)
		d2 = merge_sort_dict_supply_fill_cache(d2)
		d = merge_dict_supply_fill_cache(d1, d2)
	
	return d


def merge_dict_end_point_cache_preference(d1, d2):

	# create the return object 
	d = {}

	# get smallest elements until one dict is empty
	while len(d1) > 0 and len(d2) > 0:

		# create the traverse objects
		d1_small, d2_small = next(iter(d1)), next(iter(d2))

		# put the smallest score into the return dictionary
		if d1[d1_small] < d2[d2_small]:
			d[d1_small] = d1[d1_small]
			del d1[d1_small]
		else:
			d[d2_small] = d2[d2_small]
			del d2[d2_small]

	# add remaining elements
	while len(d1) > 0:
		d1_small = next(iter(d1))
		d[d1_small] = d1[d1_small]
		del d1[d1_small]
	while len(d2) > 0:
		d2_small = next(iter(d2))
		d[d2_small] = d2[d2_small]
		del d2[d2_small]

	# return
	return d

def merge_sort_dict_end_point_cache_preference(d):

	# objects
	d1 = {}
	d2 = {}
	length = len(d)
	middle = int(length / 2)

	if len(d) > 1:
		for i in range(0, middle, 1):
			next_item = next(iter(d))
			d1[next_item] = d[next_item]
			del d[next_item]

		for i in range(middle, length, 1):
			next_item = next(iter(d))
			d2[next_item] = d[next_item]
			del d[next_item]

		d1 = merge_sort_dict_end_point_cache_preference(d1)
		d2 = merge_sort_dict_end_point_cache_preference(d2)
		d = merge_dict_end_point_cache_preference(d1, d2)
	
	return d


def merge_dict_end_point_demand(d1, d2):

	# create the return object 
	d = {}

	# get smallest elements until one dict is empty
	while len(d1) > 0 and len(d2) > 0:

		# create the traverse objects
		d1_small, d2_small = next(iter(d1)), next(iter(d2))

		# put the smallest score into the return dictionary
		if d1[d1_small][1] < d2[d2_small][1]: # the [1] refers to the number of requests
			d[d1_small] = d1[d1_small]
			del d1[d1_small]
		else:
			d[d2_small] = d2[d2_small]
			del d2[d2_small]

	# add remaining elements
	while len(d1) > 0:
		d1_small = next(iter(d1))
		d[d1_small] = d1[d1_small]
		del d1[d1_small]
	while len(d2) > 0:
		d2_small = next(iter(d2))
		d[d2_small] = d2[d2_small]
		del d2[d2_small]

	# return
	return d

def merge_sort_dict_end_point_demand(d):

	# objects
	d1 = {}
	d2 = {}
	length = len(d)
	middle = int(length / 2)

	if len(d) > 1:
		for i in range(0, middle, 1):
			next_item = next(iter(d))
			d1[next_item] = d[next_item]
			del d[next_item]

		for i in range(middle, length, 1):
			next_item = next(iter(d))
			d2[next_item] = d[next_item]
			del d[next_item]

		d1 = merge_sort_dict_end_point_demand(d1)
		d2 = merge_sort_dict_end_point_demand(d2)
		d = merge_dict_end_point_demand(d1, d2)
	
	return d