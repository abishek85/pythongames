# Unit test functions in wordsWithFriends
# Author :A. Kashinath

from wordsWithFriends import *
import unittest


class TestWordMethods(unittest.TestCase):
    
    def test_getWordScore(self):
        """
        Unit test for getWordScore
        """
        # dictionary of words and scores
        words = {("", 7):0, ("it", 7):4, ("was", 7):18, ("scored", 7):54, \
                 ("waybill", 7):155, ("outgnaw", 7):127, ("fork", 7):44, \
                 ("fork", 4):94}
        for (word, n) in words.keys():
            self.assertEqual(getWordScore(word, n), words[(word, n)])
            
    def test_updateHand(self):
        """
        Unit test for updateHand
        """
        # case 1
        handOrig = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
        handCopy = handOrig.copy()
        word = "quail"
            
        hand2 = updateHand(handCopy, word)
        expectedHand = {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
        self.assertEqual(hand2, expectedHand)
        self.assertEqual(handCopy, handOrig)
        
        # case 2
        handOrig = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        handCopy = handOrig.copy()
        word = "evil"
    
        hand2 = updateHand(handCopy, word)
        expectedHand = {'e':0, 'v':1, 'n':1, 'i':0, 'l':1}
        self.assertEqual(hand2, expectedHand)
        self.assertEqual(handCopy, handOrig)
        
        # case 3
        handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        handCopy = handOrig.copy()
        word = "hello"   
        
        hand2 = updateHand(handCopy, word)
        expectedHand = {'h': 0, 'e': 0, 'l': 0, 'o': 0}
        self.assertEqual(hand2, expectedHand)
        self.assertEqual(handCopy, handOrig)
        
    def test_isValidWord(self):
        """
        Unit test for isValidWord
        """
        # case 1
        word = "hello"
        handOrig = getFrequencyDict(word)
        handCopy = handOrig.copy()

        self.assertTrue(isValidWord(word, handCopy, [word]))
        self.assertEqual(handCopy, handOrig)
        self.assertFalse(isValidWord(word, handCopy, ['world']))
        
        # case 2
        hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
        word = "rapture"
        self.assertFalse(isValidWord(word, hand, [word]))
        
        # case 3
        hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
        word = "honey"
        self.assertTrue(isValidWord(word, hand, [word]))
        
        # case 4
        hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
        word = "honey"
        self.assertFalse(isValidWord(word, hand, [word]))
        
        # case 5
        hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
        word = "liven"
        self.assertTrue(isValidWord(word, hand, [word]))
        
        # case 6
        word = "even"
        self.assertFalse(isValidWord(word, hand, [word]))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWordMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)