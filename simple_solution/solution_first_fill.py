# imports
import supply_class as sc
import merge_sort as ms
import random


def fill_cache(video_id_list, video_size_list):

	# Inputs
	## video_id_list: list of video id
	## video_size_list: list of size of video as % of cache server

	# make a dictionary
	video_dictionary = {}
	video_count = 0
	for video_id in video_id_list:
		video_size = video_size_list[video_count]
		video_dictionary[video_id] = video_size
		video_count += 1

	# sort the dictionary
	video_dictionary = ms.merge_sort_dict_supply_fill_cache(video_dictionary)

	# make new lists
	video_id_list = [vid for vid in video_dictionary]
	video_size_list = []
	for vid in video_dictionary:
		video_size_list.append(video_dictionary[vid])

	# populate the cache server with videos
	cache_videos = []
	cache_percent_available = 1
	while len(video_id_list) > 0 and cache_percent_available > video_size_list[0]:
		random_index = random.randint(0, len(video_id_list) - 1) # this range is inclusive, so adjust
		video_id_random = video_id_list.pop(random_index)
		video_size_random = video_size_list.pop(random_index)
		cache_videos.append(video_id_random)
		cache_percent_available -= video_size_random

	# list of video ids of the videos to be placed on the cache server
	return cache_videos


def first_fill(fileName):

	# data objects
	SupplyDataObject = sc.SupplyData(fileName)
	cache_video_id_dictionary = SupplyDataObject.cache_video_id()
	cache_video_size_dictionary = SupplyDataObject.cache_video_size()

	# create solutions
	solutions = {}
	for cache in cache_video_id_dictionary:
		video_id_list = cache_video_id_dictionary[cache]
		video_size_list = cache_video_size_dictionary[cache]
		solutions[cache] = fill_cache(video_id_list, video_size_list)

	# dictionary of cache : list of videos on the cache
	return solutions

