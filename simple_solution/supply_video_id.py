# imports
import random
import google_data_class as gdc
import merge_sort as ms


# functions
def end_point_demand(fileName):

	# create GoogleData object
	GoogleDataObject = gdc.GoogleData(fileName)

	# number of videos, end points, cache server size
	VERCX = GoogleDataObject.vercx()
	V = VERCX[0]
	E = VERCX[1]
	X = VERCX[4]

	# video sizes
	video_size_list = GoogleDataObject.v_data()

	# demand data
	demand = GoogleDataObject.r_data()
	vid_list = demand[0]
	ep_list = demand[1]
	req_list = demand[2]

	# counter and counter bound
	count = 0
	count_bound = len(vid_list)

	# end point demand dictionaries
	end_point_requests = [{} for e in range(0, E, 1)]

	# populate end point demand data
	while count < count_bound:

		# discard videos that are too large for a cache server
		if video_size_list[vid_list[count]] <= X:

			# data objects
			end_point = ep_list[count]
			video_id = vid_list[count]
			video_requests = req_list[count]
			video_size = video_size_list[video_id]
			video_demand = [video_id, video_requests, video_size]

			# identify the appropriate end point dictionary
			end_point_dict = end_point_requests[end_point]

			# video demand profile
			if video_id in end_point_dict:
				end_point_dict[video_id][1] += video_requests
			else:
				end_point_dict[video_id] = video_demand

		# increment the count
		count += 1

	# sort each dictionary in end_point_requests by video requests
	count = 0
	for dictionary in end_point_requests:
		new_dictionary = ms.merge_sort_dict_end_point_demand(dictionary)
		end_point_requests[count] = new_dictionary
		count += 1

	# list with E dictionaries, each containing a video : [video id, video requests, video size] for videos demanded by the end point
	return end_point_requests


def cache_latency(fileName):

	# create GoogleData object
	GoogleDataObject = gdc.GoogleData(fileName)

	# number of endpoints
	VERCX = GoogleDataObject.vercx()
	E = VERCX[1]
	C = VERCX[3]

	# cache latency list
	cache_latency_list = [{} for c in range(0, C, 1)]

	# source data
	source_data = GoogleDataObject.e_data()
	data_centre_to_end_point_latency = source_data[0]
	end_point_to_cache_latency = source_data[1]

	# populate cache latency list
	for e in range(0, E, 1):
		end_point = e
		end_point_latency_list = end_point_to_cache_latency[e]
		latency = data_centre_to_end_point_latency[e]
		cache_count = 0
		for cache in end_point_latency_list:
			if cache is False:
				pass
			else:
				latency_value = latency - cache
				cache_latency_list[cache_count][end_point] = latency_value

			cache_count += 1

	# list with C dictionaries, each containing end point : latency for each connected endpoint
	return cache_latency_list


def cache_supply_source(fileName):

	# data objects
	end_point_demand_list = end_point_demand(fileName) # list with E dictionaries, each containing a video : [video id, video requests, video size] for videos demanded by the end point
	cache_latency_list = cache_latency(fileName) # list with C dictionaries, each containing end point : latency for each connected endpoint

	# cache initial offers
	cache_supply_source_dictionary = {}

	# populate cache_supply_source_list
	cache_count = 0
	# iterate over each cache server
	for cache in cache_latency_list:
		# create a list to be the value of the dictionary entry
		cache_video_list = []
		# iterate over each end_point in cache, dictionary of end point : latency for the cache
		for end_point in cache:
			# find the dictionary of all videos desired by the end point
			video_dict = end_point_demand_list[end_point]
			# iterate over the videos and add if not already in the cache_video_list
			for video in video_dict:
				if video in cache_video_list:
					pass
				else:
					cache_video_list.append(video)
		# add the dictionary entry: cache id : cache_video_list
		cache_supply_source_dictionary[cache_count] = cache_video_list
		# increment cache_count
		cache_count += 1

	# dictionary with keys of cache ID and values of list of video IDs that could be placed on the server
	return cache_supply_source_dictionary

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
def cache_supply_file(fileName):

	# data objects
	cache_supply_source_dictionary = cache_supply_source(fileName)

	# put results into a text file
	with open("supply_data/video_id/" + fileName + ".txt", "w") as f:

		for cache in cache_supply_source_dictionary:
			# data objects
			cache_id = cache
			video_list = cache_supply_source_dictionary[cache_id]
			# start the line with the cache id
			f.write(str(cache) + " ")
			# write each video in the list
			for video in video_list:
				f.write(str(video) + " ")
			# create a new line
			f.write("\n")