# Lexicographic-Sorting
Qualia Challenge

The runtime complexity of this solution is bounded by the sorted() function, which runs with complexity O(n log n), where n is the size of the input array.  As long as the length of the strings in the first input array are relatively small compared to n, both the convert_to_numbers and the convert_to_letters functions scale linearly with n, so they will not effect the complexity.  The creation of the dictionaries will take constant time since the second input can have at most 26 characters.

If the size of the array is significantly smaller than the lengths of the words in the array, then there may be faster solutions.  It could be faster to compare the strings after looking at each character in the string.  This would significantly increase the number of comparisons, but could eliminate the need to convert the entire length of the string into numbers and then back into letters.
