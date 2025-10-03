class Solution:
    def isPalindrome(self, x: int) -> bool:
        gedreht = ''
        number = x
        for i in range (0,len(str(number))):
            gedreht = str(number)[i] + gedreht
        if str(gedreht) == str(number):
            print(number,'reads as', gedreht, 'from left to right and from right to left.')
            return True
        else:
            print('From left to right, it reads', number, '. From right to left, it becomes', gedreht,'. Therefore it is not a palindrome.')
            return False
