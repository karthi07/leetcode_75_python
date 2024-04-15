
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

## BT - DFS

1. find max depth of the Tree
  - recursive -> return 1 + max(self.maxDepth(left), self.maxDepth(right))
  - iter -> use stack to store node and depth, find max(depth) and add child to stack
2. check leaf similarity of two tree
  - calc leaf using dfs find_leaf(node, leaf) -> if not node.left and not node.right -> leaf.append(node.val) find_leaf(node.left, leaf) find_leaf(node.right, leaf)
3. good nodes
  - use dfs with recursive and keep track of maxValue. return the good nodes

## BT - BFS

1. right side view of tree
  - use queue with node and level, and maintain previous_level. while traversing if not level != previous_level and add to res, add right to queue before left