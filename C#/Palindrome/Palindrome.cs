using System;
using System.Linq;

namespace PalindromeProg
{
    /// <summary>
    /// 
    /// </summary>
    static class Palindrome
    {
        /// <summary>
        /// 
        /// </summary>
        /// <param name="strInput"></param>
        public static void TestPalindrome( string strInput )
        {
            var rslt = Check( strInput );
            Console.WriteLine( string.Format( "{0} {1}", strInput, rslt ) );
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="strInput"></param>
        /// <returns></returns>
        public static bool Check( string strInput )
        {
            // Remove all spaces and set to lowercase.
            strInput = strInput.Replace( " ", "" ).ToLower();
            // Remove all punctuation
            strInput = new string( strInput.Where( c => !char.IsPunctuation( c ) ).ToArray() );

            //Console.WriteLine( strInput );
            int strlen = strInput.Length;
            // Check length.
            if ( strlen < 3 )
            {
                return false;
            }

            int i = 0,
                j = strlen - 1;
            while ( i < j )
            {
                //Console.WriteLine( "{0}, {1}", i, j );
                if ( strInput[i] != strInput[j] )
                {
                    return false;
                }

                ++i;
                --j;
            }

            return true;
        }
    }
}
