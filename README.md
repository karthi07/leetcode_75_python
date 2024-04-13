
## Array

1. Merge Strings Alternately
  - find min, loop over string and add the rest using res.append([word1[min:], word[min:]])
2. GCD of string
  - loop min(len1,len2), 0, -1 -> check if its a valid gcd | valid gcd -> if len1, len2 is divisible and base * n1 = str1, base * n2 = str2

## Two Pointers

1. Move all zeros to end
  - loop over array, maintain pointer for zeros. for each non-zero, swap the array and increment the zeroPtr
2. Is SubSequence
  - loop over main string, maintain pointer for matching chars, if s[ptr] == t[i] => ptr += 1, return true if ptr == len(s)
3. Container water distance
  - left and right index of array, calc current area and maintain gobal area max for each step. and update the idx based on max left and righ value