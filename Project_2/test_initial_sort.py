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


class TestInitialSort(unittest.TestCase):

	def test_supply_data(self):

		# imports
		import data_class as dc
		import initial_sort_class as sc

		# generate list of test files
		theFiles = TestFiles.get_files(self)

		# check the files
		print("")
		print("Supply.data() works for:")
		for f in theFiles:
			# preliminary data
			source_data = dc.GoogleData(f)
			e_data = source_data.e_data()
			supply_list = sc.Supply(e_data).data()
			E = source_data.vercx()[1]
			C = source_data.vercx()[3]

			# tests
			self.assertEqual(len(supply_list), E)
			for s in supply_list:
				self.assertEqual(len(s), C)
			# result
			print("-", f)

	def test_demand_data(self):

		# imports
		import data_class as dc
		import initial_sort_class as sc

		# generate the list of test files
		theFiles = TestFiles.get_files(self)

		# check the files
		print("")
		print("Demand.data() works for:")
		for f in theFiles:
			# preliminary data
			demand_data = sc.Demand(f).data()
			VERCX = dc.GoogleData(f).vercx()
			E = VERCX[1]
			V = VERCX[0]

			# tests
			self.assertEqual(len(demand_data), E)
			for d in demand_data:
				self.assertTrue(len(d) <= V)

			# result
			print("-", f)


# run the unit test
if __name__ == "__main__":
	print("")
	print("Test results for initial_sort_class.py")
	unittest.main()