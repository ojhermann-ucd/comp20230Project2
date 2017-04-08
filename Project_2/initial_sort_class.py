# imports
import data_class as dc

def merge_dict(d1, d2):

	# create the return object 
	d = {}

	# get smallest elements until one dict is empty
	while len(d1) > 0 and len(d2) > 0:

		# create the traverse objects
		d1_small, d2_small = next(iter(d1)), next(iter(d2))

		# put the smallest entry into the return dictionary
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

# # quick test
# dict1 = {'one':1, 'two': 2}
# dict2 = {'three':3, 'four':4, 'five': 5}
# print(merge_dict(dict1, dict2))


def ms(d):

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

		d1 = ms(d1)
		d2 = ms(d2)
		d = merge_dict(d1, d2)
	
	return d

# # quick test
# dict1 = {'one':1, 'two': 2, 'three': 3, 'four': 4}
# dict2 = {'five':5, 'six': 6, 'seven': 7, 'eight': 8}
# dict3 = {'five':5, 'six': 6, 'seven': 7, 'eight': 8, 'one':1, 'two': 2, 'three': 3, 'four': 4, }
# dict3 = ms(dict3)
# print(dict3)


class Supply():

	def __init__(self, eData):
		self.eData = eData

	def data(self):

		# data objects
		d_to_e_latency = self.eData[0] # for each e, there is a value of the latency from data centre to e
		c_latency = self.eData[1] # for each e, there is a list with C entries, either False or populated with latency from c to e
		supply_list = [] # list of e dictionaries; each dict contains c_index:latency for the relevant e

		# populate supply_list
		e_counter = 0 # keep track of the endpoints
		while e_counter < len(d_to_e_latency):
			e_dict = {} 
			d_latency = d_to_e_latency[e_counter]
			c_counter = 0
			for c in c_latency[c_counter]:
				if c is False:
					e_dict[c_counter] = 0
				else:
					e_dict[c_counter] = d_latency - c # the bigger this number, the faster the connection
				c_counter += 1
			
			# sort the data with merge sort (modified for dictionaries)
			e_dict = ms(e_dict) # testing

			# add the dictionary to the list
			supply_list.append(e_dict)
			
			# increment the counter
			e_counter += 1

		# return
		return supply_list


# # quick test
# myData = dc.GoogleData("kittens").e_data()
# mySupply = Supply(myData).data()
# print(len(mySupply))
# print(mySupply[0])


class Demand():

	def __init__(self, fileName):
		
		self.source = fileName

	def data(self):

		# data objects

		# main object
		main_object = dc.GoogleData(self.source)

		# size_list
		size_list = main_object.v_data()
		v_size_dict = {} # key is video ID, value is size of video
		v_count = 0
		for v in size_list:
			v_size_dict[v_count] = v
			v_count += 1

		# request data
		r_data = main_object.r_data()
		vid_list = r_data[0] # list with video ID in each spot
		end_list = r_data[1] # list with end point for corresponding index in vid_list
		req_list = r_data[2] # list with request for corresponding index in vid_list

		# E
		VERCX = main_object.vercx()
		E = VERCX[1]

		# size of request
		request_size_list = []
		v_count = 0
		for v in vid_list:
			size = v_size_dict[v]
			req = req_list[v_count]
			request_size_list.append(size * req)
			v_count += 1

		# demand_list: list with E dictionaries
		demand_list = [{} for e in range(0, E, 1)]

		# populate demand_list
		v_count = 0
		for video in vid_list:
			
			# input objects
			v_id = video
			end_point = end_list[v_count]
			size = request_size_list[v_count]

			# iteration 
			the_dict = demand_list[end_point]
			if v_id in the_dict:
				the_dict[v_id] += size
			else:
				the_dict[v_id] = size

			# increment v_count
			v_count += 1

		# sort the data with merge sort (modified for dictionaries)
		new_demand = []
		for d in demand_list:
			new_demand.append(ms(d))

		# return
		return new_demand # list of E dictionaries, each entry with V entries, each containing demand for that video at the end point


# # quick test
# myDemand = Demand("kittens")
# print(myDemand.data())