# imports
import google_data_class as gdc
import supply_video_id as svi
import merge_sort as ms
import random
import solution_first_fill as sff


def end_point_cache_preference(fileName):

	# create GoogleData object
	GoogleDataObject = gdc.GoogleData(fileName)

	# number of endpoints
	VERCX = GoogleDataObject.vercx()
	E = VERCX[1]

	# source list
	cache_latency_list = svi.cache_latency(fileName)

	# end_point_cache_preference_dictionary
	end_point_cache_preference_dictionary = {}

	# populate end_point_cache_preference_dictionary
	for end_point in range(0, E, 1):
		end_point_new_dict = {}
		cache_count = 0
		for cache in cache_latency_list:
			if end_point in cache:
				end_point_new_dict[cache_count] = cache[end_point]
			cache_count += 1
		end_point_new_dict = ms.merge_sort_dict_end_point_cache_preference(end_point_new_dict)
		end_point_cache_preference_dictionary[end_point] = end_point_new_dict

	# dictionary with entry for each end point, containing a dictionary of cache id : latency to end point sorted ascending
	return end_point_cache_preference_dictionary


def score_first_fill(fileName):

	# list with E dictionaries, each containing a video : [video id, video requests, video size] for videos demanded by the end point
	end_point_demand_list = svi.end_point_demand(fileName)
	# dictionary with entry for each end point, containing a dictionary of cache id : latency to end point sorted ascending
	end_point_cache_preference_dictionary = end_point_cache_preference(fileName)
	# dictionary of cache : list of videos on the cache
	first_fill_dictionary = sff.first_fill(fileName)

	# calculate the score
	score = 0
	requests = 0
	end_point_count = 0
	video_score_dictionary = {}
	video_request_dictionary = {}
	for end_point in end_point_demand_list:
		videos_demanded_dictionary = end_point_demand_list[end_point_count]
		for cache in end_point_cache_preference_dictionary[end_point_count]:
			latency = end_point_cache_preference_dictionary[end_point_count][cache]
			server = first_fill_dictionary[cache]
			for video_demanded in videos_demanded_dictionary:
				if video_demanded in server:
					temp_score = videos_demanded_dictionary[video_demanded][1] * latency
					temp_requests = videos_demanded_dictionary[video_demanded][1]
					if video_demanded in video_score_dictionary:
						if video_score_dictionary[video_demanded] < temp_score:
							video_score_dictionary[video_demanded] = temp_score
							video_request_dictionary[video_demanded] = temp_requests
					else:
						video_score_dictionary[video_demanded] = temp_score
						video_request_dictionary[video_demanded] = temp_requests

		end_point_count += 1
	
	for video in video_score_dictionary:
		score += video_score_dictionary[video]
		requests += video_request_dictionary[video]

	return [(score * 1000) / requests, first_fill_dictionary]

import time
start = time.time()
print(score_first_fill('me_at_the_zoo')[0])
print(time.time() - start)



# first fill: GA/Random
## fill each cache randomly from cache_initial_offers
## for each end point in end_point_demand, check for each demanded video in end_point_cache_preference list (make from dict)
## calculate score

# Hill Climbing
## for each cache (randomly selected):
### try new random assortment; continue if score better; stop if two zero or negative changes
### compare score to existing solution; if better, save, else, drop

# Hill Climbing Precision
# could go further and do random changes of individual videos and compare at each stage, but I'm still keeping open a giant opportunity set and tryign to make this computationally tractable