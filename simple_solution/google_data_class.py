class GoogleData():
	
	
	def __init__(self, fileName):
		# initialise the object with the source of the data
		# Input: string of full file name
		self.source = "google_data/" + fileName + ".in"

	
	def vercx(self):

		# Description: takes self, reads first line, and returns list of VERCX
		# Input: self
		# Output: list containing V, E, R, C, X

		with open(self.source, "r") as f:
			VERCX = [int(x) for x in f.readline().split()]
		return VERCX

	
	def v_data(self):

		# Description: takes self and generates a list with all the video sizes in MB
		# Input: self
		# Output: list containing video sizes in MB

		# imports
		import linecache

		# create the list
		v_size_list = [int(x) for x in linecache.getline(self.source, 2).split()]

		# return the list
		return v_size_list

	
	def e_data(self):

		# Description: takes self and generates a list of lists
		# Input: self
		# Output: 
		## list[0] is data centre to endpoint latency in miliseconds
		## list[1] list of lists, each containing latency of cache server (index of inner list) to endpoint (index position in outer list) in miliseonds

		# object data
		VERCX = GoogleData.vercx(self)
		E = VERCX[1]
		C = VERCX[3]

		# create objects
		d_to_e_latency = [] # data centre to endpoint; for each e, there is a value of the latency from data centre to e
		c_latency = [] # all cache to end point lists; for each e, there is a list with C entries, either False or populated

		# open the file
		with open(self.source, "r") as f:

			# go to start of endpoints
			e_count = 0
			while e_count < 2:
				next(f)
				e_count += 1

			# populating endpoint data
			e_count = 0
			
			while e_count < E:
				# create objects
				c_to_e_latency = [False] * C # cache to endpoint; populatd with False; will fill in where needed
				current = [int(x) for x in next(f).split()]
				
				# get the endpoint latency in milliseconds
				d_to_e_latency.append(current[0])
				
				# get the cache to endpoint latency
				if current[1] == 0:
					
					# if the endpoint is not connected to any cache servers, do nothing
					pass
				
				else:

					# iterate over the cache servers connected to the endpoint
					for item in range(current[1]):
						
						# create object
						current = [int(x) for x in next(f).split()]

						# populate cach to endpoint latency data
						c_to_e_latency[current[0]] = current[1]

				# add to c_latency
				c_latency.append(c_to_e_latency)

				# increment e_count
				e_count += 1

			return [d_to_e_latency, c_latency]

	
	def r_data(self):

		# Description: takes self and generates a list of lists describing all the video requests
		# Input: self
		# Output: one list containing three lists
		## list[0]: IDs of the requested videos
		## list[1]: IDs of the endpoint requesting the video in list[0] at same index
		## list[2]: number of requests for the video in list[0] at same index from the endpoint in list[1] at the same index

		# object data
		VERCX = GoogleData.vercx(self)
		R = VERCX[2]

		# objects
		vid_list = [] # video id list
		ep_list = [] # endpoint for requests of video
		req_list = [] # number of requests for video

		# count the lines
		lines = 0
		with open(self.source, "r") as f:
			# count the lines
			lines = 0
			for line in f:
				lines += 1

		# open the file
		with open(self.source, "r") as f:
		
			# go to first request
			start = lines - R
			r_count = 0
			while r_count < (start):
				next(f)
				r_count += 1

			# populate the lists
			r_count = 0
			while r_count < R:

				# go to a line and get the information
				current = [int(x) for x in next(f).split()]

				# add to lists
				vid_list.append(current[0])
				ep_list.append(current[1])
				req_list.append(current[2])

				# increment r_count
				r_count += 1

		return [vid_list, ep_list, req_list]