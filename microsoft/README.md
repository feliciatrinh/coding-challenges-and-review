### Arrays

* [Fair Indices](fair_indices.py)
    * Given arrays A and B consisting of N integers each, return the number of fair indices.
    * Runtime: O(N), Space: O(1)
* [Largest K Such That Both K and -K Exist in Array](largest_k_both_exist.py)
    * Given an array of integers, return the largest K > 0 such that both values K and -K exist in array or 0 otherwise.
    * Runtime: O(n), Space complexity: O(n)
* [Largest M-aligned Subset](largest_m_aligned_subset.py)
    * Given an array A of N coordinates and integer M, return the size of the largest M-aligned subset of points from A
    * Runtime: O(N), Space complexity: O(M)
* [Largest Number X that Occurs X Times](largest_num_x_occurs_x_times.py)
    * Given array A, the biggest value X which occurs in A exactly X times, or 0 otherwise.
    * Runtime: O(N), Space complexity: O(N)
* [Light Bulb Switcher](light_bulb_switcher.py)
    * Given array A containing the order in which the A[k-th] (k in range [0, n - 1]) bulb is turned on for bulbs
    numbered 1 to N, return the number of moments for which all turned on bulbs are blue.
    * Runtime: O(N), Space: O(1)
* [Max Row Column Sum](max_row_col_sum.py)
    * Given a matrix, return the sum of the maximum row sum and the maximum column sum.
    * Runtime: O(M * N), Space: O(1)
* [Max Slices to Sort Array](max_slices_to_sort_array.py)
    * Given an array of N distinct integers, return the max number of slices for which the sorting algorithm will return
    a correctly sorted array.
    * Runtime: O(N), Space complexity: O(N)
* [Meeting Rooms](meeting_rooms.py)
    * Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...], find the minimum
    number of conference rooms required.
    * Runtime: O(NlogN), Space: O(N)
* [Number of Fractions that Sum to 1](num_fractions_add_to_one.py)
    * Given fractions, return the number of pairs that sum to one
    * Uses [two_sum](../arrays/two_sum.py) aka [sum_to_k](../arrays/sum_to_k.py) approach
    * Runtime: O(n), Space Complexity: O(n)
* [Numbers with Equal Digit Sum](numbers_equal_digit_sum.py)
    * Given array of n integers, return the max sum of two numbers whose digits add up to an equal sum or -1 otherwise
    * Runtime: O(n), Space complexity: O(n) or sub-linear?
* [Particle Velocity](particle_velocity.py)
    * Given N positions of a particle, return the number of periods of time when the movement of the particle is stable.
    * Runtime: O(N), Space: O(1)
* [Partition Sorted Array into K Buckets with Balanced Sums](partition_array_n_buckets_balanced_sum.py)
    * Given a sorted array of integers and integer k, partition array into k sub-arrays with approximately equal sums.
    * Runtime: O(), Space: O()
    * See related [Partition Array Into K Sub-arrays with Equal Sum](../arrays/partition_to_k_equal_sum_subsets.py)
* [Remove Duplicates](../arrays/remove_duplicates.py)
    * Runtime: O(n), Space complexity: O(1)
* [Set Matrix Zeros](set_matrix_zeroes.py)
    * Given m x n matrix, if an element is 0, set its entire row and column to 0. Do in-place.
    * Runtime: O(mn), Space complexity: O(m + n) naive, O(1) optimal

### Dynamic Programming
* [Aladdin Checkers Game](aladdin_checkers_game.py)
    * Similar to [Count Matrix Paths](../dynamic-programming/count_matrix_paths.py)
    * Given n x n checker board, return the maximum number of pawns owned by Aladdin that Jafar can beat in his turn
    * Recursive runtime: exponential; Dynamic programming runtime: O(n^2)

### Graphs/Paths

* [Aladdin Checkers Game](aladdin_checkers_game.py)
    * Similar to [Count Matrix Paths](../dynamic-programming/count_matrix_paths.py)
    * Given n x n checker board, return the maximum number of pawns owned by Aladdin that Jafar can beat in his turn
    * Recursive runtime: exponential; Dynamic programming runtime: O(n^2)
* [Max Network Rank](max_network_rank.py)
    * Given two arrays A, B consisting of M integers each and an integer N where A[i] and B[i] are cities at the two
    ends of the ith road, return the maximal network rank in the whole infrastructure
    * Runtime: O(M) + O(NM)?, Space complexity: O(N + M)?

### Heaps

* [Median of Data Stream](median_data_stream.py)
    * Design a data structure that supports adding a num from the data stream to the data structure and returning the
    median of all elements seen so far
    * Runtime: O(logn), Space complexity: O(n)

### Recursion

* [Tower of Hanoi](tower_of_hanoi.py)

### Search

* [Quick Select](../search-and-sorting/quickselect.py)
    * Find the kth smallest element in an unordered list
    * Average runtime: O(n), Worst runtime: O(n^2)

### Sort

* [Max Slices to Sort Array](max_slices_to_sort_array.py)
    * Given an array of N distinct integers, return the max number of slices for which the sorting algorithm will return
    a correctly sorted array.
    * Runtime: O(N), Space complexity: O(N)

### Strings

* [Clock Variations/Permutations](clock_variations.py)
    * Given 4 integers b/w 0 and 9, return the number of valid 24-hour, digital clock formatted times you can form using
    these 4 integers
    * Runtime: O(n!), Space complexity: O(n!) where n is 4 here
* [Crop Words](crop_words.py)
    * Given a message and a limit k, crop a number of words from the end of the message and return the new message.
    * Runtime: O(n), Space: O(1)
* [Largest Alphabetic Character](largest_alphabetic_character.py)
    * Given a string s, find the largest alphabetic character whose both uppercase and lowercase appear in s. The
    uppercase character should be returned.
    * Runtime: O(n), Space complexity: O(n?) or max b/w n and number of unique characters possible?
* [Longest Substring With At Most K Distinct Characters](longest_substring_k_distinct.py)
    * Runtime: O(nk), Space complexity: O(k)
    * See related [Longest Substring Without Repeats](../strings/longest_substring_no_repeats.py)
* [Longest Substring Without k Contiguous Occurrences of Letter](longest_substring_without_k_contiguous.py)
    * Given string, return longest substring such that the substring does not contain more than two contiguous
    occurrences of a letter
    * Runtime: O(n), Space complexity: O(1)
* [Max Length of Concatenated String with Unique Characters](max_length_concatenated_string_unique_characters.py)
    * Given a array containing strings, return the maximum length of a concatenation of a sub-sequence of array
    containing unique characters.
    * Runtime: O(2^N), Space: O(2^N) where N is length of array
* [Max Value Insert Digit](max_value_insert_digit.py)
    * Given an integer num, return the maximum possible value obtained by inserting one '5' digit inside the decimal
    representation of num.
    * Runtime: O(N) where N is the number of digits in num, Space: O(1)
* [Min Cost to Get String Without Two Identical Consecutive Letters](min_cost_string.py)
    * Given a string s and costs, return the minimum total cost of deletions needed to achieve a string without two
    identical consecutive letters.
    * Runtime: O(n), Space complexity: O(1)
* [Min Deletions to Obtain String in Specific Format](min_deletions_to_obtain_string_in_format.py)
    * Given a string, return the minimum number of deletions needed to get the string into a specific format.
    * Runtime: O(N), Space: O(1)
* [Plane Seat Reservation](plane_seat_reservation.py)
    * Given a string of length M representing reserved seats, return the maximum number of four-person families you can
    fit.
    * Runtime: O(M), Space: O(M)
* [Postfix Evaluation](postfix_evaluation.py)
    * Given a postfix mathematical expression in the form of a string made of single-digit operands and 4 operators, return the
    answer to the expression.
    * Runtime: O(N), Space: O(N)
    * See related [Infix Evaluation](../strings/evaluate_math_expression.py)
* [Riddle](riddle.py)
    * Given string, return a copy of the string with all '?' replaced by lowercase letters (a-z) in such a way that the
    same letter does not occur next to each other.
    * Runtime: O(n), Space complexity: O(1)
* [Word Machine](word_machine.py)
    * Given a sequence of operations as a string, return the topmost value from the stack after all of the operations
    have been done or -1 if the machine would report an error.
    * Runtime: O(n), Space complexity: O(n)

### Trees

* [Binary Search Tree Lowest Common Ancestor](bst_lowest_common_ancestor.py)
    * Given a binary search tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    * Runtime: O(logn) on average; Space complexity: O(n) recursive solution, O(1) iterative solution
    * See [Binary Tree Lowest Common Ancestor](../trees/binary_tree_lowest_common_ancestor.py) for similar problem
* [Count Visible Nodes in a Binary Tree](visible_node_binary_tree.py)
    * Given a binary tree, count how many nodes are visible.
    * Runtime: O(n), Space complexity: O(n)
* [is BT a BST](is_bst.py)
    * Given a binary tree, determine if it is a binary search tree
    * Runtime: O(n)

### Other/Math

* [Buy Sell Stocks](buy_sell_stocks.py)
    * Given a timeline for a stock (A chronologically ordered list of day objects containing the highest and lowest
    price for the stock on that day) find the date to buy and the date to sell that would result in the highest profit.
    * Runtime: O(n^2)
* [Mean, Median, Mode](mean_median_mode_array.py)
    * Given an array, return the mean, median, and mode
    * Runtime: O(NlogN), Space: O(N)
