# imports
import unittest

class TestFiles():

	# initialise
	def __init__(self):
		self

	# generate a list of files to test
	def get_files(self):
		
		# imports
		import os

		# generate an list of files to test
		output = []
		for f in os.listdir("data/"):
			if f.endswith(".in"):
				f = f.split(".")[0]
				output.append(f)
		return output


class TestVERCX(unittest.TestCase):

	def test_len_vercx(self):

		# Purpose: make sure .vercx has the correct length

		# imports
		import data_class as dc
		
		# run the test
		theFiles = TestFiles.get_files(self)

		# check the files
		print("")
		print(".vercx() works for:")
		for f in theFiles:
			# length of VERCX
			theLen = len(dc.GoogleData(f).vercx())
			# test
			self.assertEqual(theLen, 5)
			# result
			print("-", f)

	def test_len_v_data(self):

		# Purpose: make sure .vercx has the correct length

		# imports
		import data_class as dc
		
		# run the test
		theFiles = TestFiles.get_files(self)

		# check the files
		print("")
		print(".v_data() works for:")
		for f in theFiles:
			# V
			V = dc.GoogleData(f).vercx()[0]
			# v_data
			v_data = dc.GoogleData(f).v_data()
			lenV = len(v_data)
			self.assertEqual(lenV, V)
			print("-", f)

	def test_len_e_data(self):

		# imports
		import data_class as dc

		# get the test files
		theFiles = TestFiles.get_files(self)

		# check the files
		print("")
		print(".e_data() works for:")
		for f in theFiles:
			# E and C
			E = dc.GoogleData(f).vercx()[1]
			C = dc.GoogleData(f).vercx()[3]
			# e_data
			e_data = dc.GoogleData(f).e_data()
			# e_data outputs
			d_to_e_latency = e_data[0]
			c_latency = e_data[1]
			# tests
			lenDtoE = len(d_to_e_latency)
			lenC = len(c_latency)
			self.assertEqual(lenDtoE, E)
			self.assertEqual(lenC, E)
			for i in range(E):
				self.assertEqual(len(c_latency[i]), C)
			print("-", f)


	def test_len_r_data(self):

			# imports
			import data_class as dc

			# get the test files
			theFiles = TestFiles.get_files(self)

			# check the files
			print("")
			print(".r_data() works for:")
			for f in theFiles:
				# R
				R = dc.GoogleData(f).vercx()[2]

				# r_data
				r_data = dc.GoogleData(f).r_data()
				vid_list = r_data[0]
				ep_list = r_data[1]
				req_list = r_data[2]

				# tests
				self.assertEqual(len(vid_list), R)
				self.assertEqual(len(ep_list), R)
				self.assertEqual(len(req_list), R)
				print("-", f)


# run the unit test
if __name__ == "__main__":
	print("Test results for data_class.py")
	unittest.main()