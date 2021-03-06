import string

def palindrome_check( str_input ):
    # Remove all spaces and set to lowercase.
    str_input = str_input.replace( " ", "" ).lower()
    # Remove all punctuation
    str_input = str_input.translate(str.maketrans('', '', string.punctuation))

    str_length = len(str_input)
    # check length.
    if str_length < 3:
        return False

    i = 0
    j = str_length - 1
    while i < j:
        #print( i, j )
        if  str_input[i] != str_input[j]:
            return False
        i += 1
        j -= 1

    return True
