def GoogleData_test(fileName):

	# Description: a function that tests the GoogleData object
	# Input: string of the fileName
	# Output: result of tests

	# imports
	import data_class as dc

	# make GoogleData object
	gObject = dc.GoogleData(fileName)

	# VERCX
	VERCX = gObject.vercx()
	# make sure the length is five
	if len(VERCX) != 5:
		return fileName + " VERCX length is not correct."

	# object values
	V = VERCX[0]
	E = VERCX[1]
	R = VERCX[2]
	C = VERCX[3]
	X = VERCX[4]

	# v_data
	v_data = gObject.v_data()
	# make sure the actual lengths match the expected lengths
	if len(v_data) != V:
		return fileName + " expected V is " + str(V) + " and actual len(v_data) is " + str(len(v_data))

	# e_data
	e_data = gObject.e_data()
	d_to_e_latency = e_data[0]
	c_latency = e_data[1]

	# d_to_e_latency
	if len(d_to_e_latency) != E:
		return fileName + " expected d_to_e_latency length is " + str(E) + " and actual value is " + str(len(d_to_e_latency))

	# c_latency
	# make sure there are E entries, one for each endpoint (containing latency from data centre to end point)
	if len(c_latency) != E:
		return fileName + " expected c_latency length is " + str(E) + " and actual value is " + str(len(c_latency))
	# makre sure ther are C entires in each list in c_latency (containing one entry for each cache server: either False or latency)
	for i in range(E):
		if not (len(c_latency[i]) == C):
			return fileName + " c_latency entry " + str(i) + " is not of length " + str(C)

	# r_data
	r_data = gObject.r_data()
	vid_list = r_data[0]
	ep_list = r_data[1]
	req_list = r_data[2]
	# vid_list
	if len(vid_list) != R:
		return fileName + " vid_list is not of length " + str(R)
	# ep_list
	if len(ep_list) != R:
		return fileName + " ep_list is not of length " + str(R)
	# vid_list
	if len(req_list) != R:
		return fileName + " req_list is not of length " + str(R)

	# all is OK
	return fileName + ": works as a GoogleData object"

# run the test
import os
for f in os.listdir("data/"):
	if f.endswith(".in"):
		f = f.split(".")[0]
		print(GoogleData_test(f))