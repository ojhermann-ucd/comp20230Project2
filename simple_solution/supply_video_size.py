# imports
import google_data_class as gdc
import supply_class as sc

def supply_data_video_size(fileName):

	# data objects
	GoogleDataObject = gdc.GoogleData(fileName)
	video_size_reference = GoogleDataObject.v_data()
	VERCX = GoogleDataObject.vercx()
	cache_size = VERCX[4]
	video_id_list = sc.SupplyData(fileName).cache_video_id()

	# populate the dictionary
	cache_supply_size_dictionary = {}
	for cache in video_id_list:
		video_size_list = []
		video_list = video_id_list[cache]
		for video in video_list:
			video_size = video_size_reference[video] / cache_size
			video_size_list.append(video_size)
		cache_supply_size_dictionary[cache] = video_size_list

	# dictionary with key of cache id and values of lists of sizes for videos that can be placed on the cache
	return cache_supply_size_dictionary


def cache_supply_file(fileName):

	# data objects
	cache_supply_size_dictionary = supply_data_video_size(fileName)

	# put results into a text file
	with open("supply_data/video_size/" + fileName + ".txt", "w") as f:

		for cache in cache_supply_size_dictionary:
			# data objects
			cache_id = cache
			video_list = cache_supply_size_dictionary[cache_id]
			# start the line with the cache id
			f.write(str(cache) + " ")
			# write each video in the list
			for video in video_list:
				f.write(str(video) + " ")
			# create a new line
			f.write("\n")