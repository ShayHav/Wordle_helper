import unittest
from Backend.Exceptions import IllegalArgumentException
from Backend.WordleSolver import WordleSolver

class wordle_solver_tests(unittest.TestCase):

    def check_list_empty_list(self):
        self.assertRaises(IllegalArgumentException, WordleSolver.check_list, [])
    
    def check_list_non_english(self):
        WordleSolver.check_list(['1'])
        self.assertRaises(WordleSolver.check_list, ['1'])
    
    def check_list_okey(self):
        self.assertEquals(WordleSolver.check_list(['a', 'b', 'c', 'd', 'e']), None)


if __name__ == '__main__':
    unittest.main()