import unittest

from main import Solution

class SolutionMethods(unittest.TestCase):
	def test_case1(self):
		""" Check if the entire program run as expected """
		solution = Solution()
		self.assertEqual(solution.run("23-10"), "Sun-2016 Fri-2020 Sat-2021 Sun-2022 Fri-2026 Sat-2027 Sat-2032 Sun-2033 Fri-2037 Sat-2038 Sun-2039 Fri-2043 Sun-2044 Fri-2048 Sat-2049 Sun-2050 Fri-2054 Sat-2055 Sat-2060 Sun-2061 Fri-2065 ")

	def test_case2(self):
		""" Check if the entire program run as expected """
		solution = Solution()
		self.assertEqual(solution.run("01-05"), 'Sun-2016 Fri-2020 Sat-2021 Sun-2022 Fri-2026 Sat-2027 Sat-2032 Sun-2033 Fri-2037 Sat-2038 Sun-2039 Fri-2043 Sun-2044 Fri-2048 Sat-2049 Sun-2050 Fri-2054 Sat-2055 Sat-2060 Sun-2061 Fri-2065 ')

	def test_case3(self):
		""" Check if the entire program run as expected """
		solution = Solution()
		self.assertEqual(solution.run("02-05"), "Sat-2020 Sun-2021 Fri-2025 Sat-2026 Sun-2027 Fri-2031 Sun-2032 Fri-2036 Sat-2037 Sun-2038 Fri-2042 Sat-2043 Sat-2048 Sun-2049 Fri-2053 Sat-2054 Sun-2055 Fri-2059 Sun-2060 Fri-2064 Sat-2065 ")

	def test_case4(self):
		""" Check if list_to_string() runs as expected """
		solution = Solution()
		words_list = ["Sat-2016 ", "Sun-2017 ", "Fri-2018 ", "Sat-2019 ", "Sun-2020"]
		self.assertEqual(solution.list_to_string(words_list), "Sat-2016 Sun-2017 Fri-2018 Sat-2019 Sun-2020")

if __name__ == "__main__":
	unittest.main()
