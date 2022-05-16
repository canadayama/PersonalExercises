package com.rhayashi;

public class Palindrome {
    // Check if string is a Palindrome;
    // ignoring spaces, punctuation, and uppercase. 
    public static boolean check( String str ) {
        
        // Remove spaces, set to lowercase & remove punctuation
        str = str.replace(" ", "").toLowerCase().replaceAll( "[^a-z0-9]", "");

        int strLength = str.length();
        // Check length.
        if ( strLength < 3 ) {
            return false;

        }
        int i = 0,
            j = strLength - 1;
        while ( i < j ) {
            if ( str.charAt(i) != str.charAt(j) )
            {
                return false;
            }
            ++i;
            --j;
        }

        return true;
    }
}