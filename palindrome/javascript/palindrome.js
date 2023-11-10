const palindrome_check = (str_input) => {
  if (typeof str_input != "string") {
    return false;
  }

  // Convert to lowercase, remove punctuation,
  // and make into list of characters.
  str_input = str_input
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "")
    .split("");

  // Get and check length.
  str_length = str_input.length;
  if (str_length < 3) {
    return false;
  }

  i = 0;
  j = str_length - 1;
  while (i < j) {
    //console.log(i, j);
    if (str_input[i] != str_input[j]) {
      return false;
    }
    ++i;
    --j;
  }

  return true;
};

module.exports = { palindrome_check };
