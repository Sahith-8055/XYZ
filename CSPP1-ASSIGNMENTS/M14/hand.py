"""It is a hand class"""
import random
class Hand(object):
    '''It is a class of hand'''
    def __init__(self, n):
        '''
        Initialize a Hand.
        n: integer, the size of the hand.
        '''
        assert type(n) == int
        self.hand_size = n
        self.vowels_letters = 'aeiou'
        self.consonants_letters = 'bcdfghjklmnpqrstvwxyz'
        # Deal a new hand
        self.deal_newhand()
    def deal_newhand(self):
        '''
        Deals a new hand, and sets the hand attribute to the new hand.
        '''
        # Set self.hand to a new, empty dictionary
        self.hand = {}
        # Build the hand
        num_vowels = self.hand_size // 3
        for _ in range(num_vowels):
            x_input = self.vowels_letters[random.randrange(0, len(self.vowels_letters))]
            self.hand[x_input] = self.hand.get(x_input, 0) + 1
        for _ in range(num_vowels, self.hand_size):
            x_input = self.consonants_letters[random.randrange(0, len(self.consonants_letters))]
            self.hand[x_input] = self.hand.get(x_input, 0) + 1
    def setdummyhand(self, hand_string):
        '''
        Allows you to set a dummy hand. Useful for testing your implementation.
        hand_string: A string of letters you wish to be in the hand. Length of this
        string must be equal to self.hand_size.
        This method converts sets the hand attribute to a dictionary
        containing the letters of hand_string.
        '''
        assert len(hand_string) == self.hand_size, "Length of hand_string ({0}) must equal length of hand_size ({1})".format(len(hand_string), self.hand_size)
        self.hand = {}
        for char in hand_string:
            self.hand[char] = self.hand.get(char, 0) + 1
    def calculatelen(self):
        '''
        Calculate the length of the hand.
        '''
        ans = 0
        for k in self.hand:
            ans += self.hand[k]
        return ans
    def __str__(self):
        '''
        Display a string representation of the hand.
        '''
        output = ''
        hand_keys = sorted(self.hand.keys())
        for letter in hand_keys:
            for _ in range(self.hand[letter]):
                output += letter
        return output
    def update(self, word):
        """
        Does not assume that self.hand has all the letters in word.
        Updates the hand: if self.hand does have all the letters to make
        the word, modifies self.hand by using up the letters in the given word.
        Returns True if the word was able to be made with the letter in
        the hand; False otherwise.
        word: string
        returns: Boolean (if the word was or was not made)
        """
        for alphabet in word:
            if alphabet in self.hand:
                self.hand[alphabet] -= 1
            else:
                return False
        return True
MY_HAND = Hand(7)
print(MY_HAND)
print(MY_HAND.calculatelen())
MY_HAND.setdummyhand('aazzmsp')
print(MY_HAND)
print(MY_HAND.calculatelen())
print(MY_HAND.update('za'))
print(MY_HAND)
