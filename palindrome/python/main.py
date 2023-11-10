#!/usr/bin/python3

import palindrome as pal

def TestPalindrome( str_input ):
    rslt = pal.palindrome_check(str_input)
    print( str_input, rslt )

TestPalindrome( "Dad" )

TestPalindrome( "Regular" )

# Finnish for a dealer in lye (caustic soda).
TestPalindrome( "saippuakivikauppias" )

TestPalindrome( "No lemon, no melon!" )

TestPalindrome( "A new order began, a more Roman age bred Rowena." )

TestPalindrome( "Animal loots foliated detail of stool lamina." )
