class SupplyData():

	
	def __init__(self, fileName):
		# initialise the object with the source of the data
		# Input: string of file name
		self.vid = "supply_data/video_id/" + fileName + ".txt"
		self.size = "supply_data/video_size/" + fileName + ".txt"


	def cache_video_id(self):

		# dictionary with keys of cache ID and values of list of video IDs that could be placed on the server
		cache_supply_video_id_dictionary = {}

		# populate cache_supply_video_id_dictionary
		with open(self.vid, "r") as f:
			for line in f:
				the_data = line.split()
				# first number identifies the cache, the subsequent numbers identify video ids
				cache_supply_video_id_dictionary[int(the_data[0])] = [int(x) for x in the_data[1:]]

		# dictionary with keys of cache ID and values of list of video IDs that could be placed on the server
		return cache_supply_video_id_dictionary


	def cache_video_size(self):

		# dictionary with key of cache id and values of lists of sizes for videos that can be placed on the cache
		cache_video_size_dictionary = {}

		# populate the dictionary
		with open(self.size, "r") as f:
			for line in f:
				the_data = line.split()
				# first number identifies the cache, the subsequent numbers identify video ids
				cache_video_size_dictionary[int(the_data[0])] = [float(x) for x in the_data[1:]]

		# dictionary with key of cache id and values of lists of sizes for videos that can be placed on the cache
		return cache_video_size_dictionary