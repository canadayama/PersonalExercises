import com.rhayashi.Palindrome;

public class Main {
    // Static Method.
    static void TestPalindrome( String str ) {
        Boolean rslt = Palindrome.check( str );
        System.out.println( String.format( "%s %b", str, rslt ) );
    }

    // Statring point.
    public static void main(String args[]) {
        TestPalindrome( "Regular" );

        TestPalindrome( "saippuakivikauppias" );
   
        TestPalindrome( "No lemon, no melon!" );
        
        TestPalindrome( "A new order began, a more Roman age bred Rowena." );

        TestPalindrome( "Animal loots foliated detail of stool lamina." );
    }
}