using System;

namespace PalindromeProg
{
    /// <summary>
    /// 
    /// </summary>
    class Program
    {
        /// <summary>
        /// 
        /// </summary>
        /// <param name="args"></param>
        static void Main( string[] args )
        {
            Palindrome.TestPalindrome( "Dad" );

            Palindrome.TestPalindrome( "Regular" );

            // Finnish for a dealer in lye (caustic soda).
            Palindrome.TestPalindrome( "saippuakivikauppias" );

            Palindrome.TestPalindrome( "No lemon, no melon!" );

            Palindrome.TestPalindrome( "A new order began, a more Roman age bred Rowena." );

            Palindrome.TestPalindrome( "Animal loots foliated detail of stool lamina." );
        }
    }
}
