import palindrome as pal

# Finnish for a dealer in lye (caustic soda).
str = "saippuakivikauppias"
rslt = pal.palindrome_check(str)
print( str, rslt )

str = "No lemon, no melon!"
rslt = pal.palindrome_check(str);
print( str, rslt )

str = "A new order began, a more Roman age bred Rowena."
rslt = pal.palindrome_check(str)
print( str, rslt )

str = "Animal loots foliated detail of stool lamina."
rslt = pal.palindrome_check(str)
print( str, rslt )