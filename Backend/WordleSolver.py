import enchant
import string
from itertools import product
from Exceptions.IllegalArgumentException import IllegalArgumentException

class WordleSolver:

    def __init__(self, green_letters: list[str], yellow_letters: list[list[str]] , grey_letters: list[str]):
        self._green_letters = green_letters
        self._yellow_letters = [set(i) for i in yellow_letters]
        self._letters_pool = set(string.ascii_lowercase) - set(grey_letters)
        must_contains = set(self._green_letters)
        must_contains.remove('*')
        for lst in self._yellow_letters:
            must_contains = must_contains.union(lst)
        self.must_contains = must_contains
        


    def check_list(lst: list[str]) -> None:
        if len(lst) > 5:
            raise IllegalArgumentException('list contains more then 5 elements')
        for char in lst:
            if not char in string.ascii_lowercase:
                raise IllegalArgumentException('list must contain only single charcter elements')


    def get_options(self, indx: int) -> set[str]:
        """
        This method get input indx for a letter and return a set of all the possible letters
        for this indx
            Paramerts:
                indx (int): the index of the letter for the possible location
            Return: set of charcters
        """
        if self._green_letters[indx] != '*':
            return [self._green_letters[indx]]
        return self._letters_pool - self._yellow_letters[indx]
        
    
    def check_valid_word(self, word: str) -> set:
        for letter in self.must_contains:
            if letter not in word:
                return False
            
        return True
    

    def solve(self) -> list[str]:
        words = []
        english_dict = enchant.Dict('en_US')
        options = [self.get_options(i) for i in range(5)]
        for word_arr in product(*options):
            word = "".join(word_arr)
            if english_dict.check(word) and self.check_valid_word(word):
                words.append(word)
        return words
            
