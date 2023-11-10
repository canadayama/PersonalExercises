const { palindrome_check } = require("./palindrome.js");

function TestPalindrome(str_input) {
  let result = palindrome_check(str_input);
  console.log(str_input, result);
}

TestPalindrome("Dad");

TestPalindrome("Regular");

// Finnish for a dealer in lye (caustic soda).
TestPalindrome("saippuakivikauppias");

TestPalindrome("No lemon, no melon!");

TestPalindrome("A new order began, a more Roman age bred Rowena.");

TestPalindrome("Animal loots foliated detail of stool lamina.");
