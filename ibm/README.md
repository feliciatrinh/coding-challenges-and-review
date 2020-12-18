### Arrays

* [Aladdin and His Carpet](aladdin_carpet.py)
    * Given two integer arrays magic and distance, determine the lowest index from which Aladdin can start his
    journey and visit every place in the circular path in order or -1 if no solution.
    * Runtime: O(N), Space: O(1)
    * See related [Gas Station](../arrays/gas_station.py)
* [Merge Two Sorted Arrays](merge_sorted_arrays.py)
    * Given two sorted arrrays, return a single, sorted array with all items in non-decreasing order.
    * Runtime: O(N), Space: O(N)
* [Parking Dilemma](parking_dilemma.py)
    * Given an integer array cars and an integer k, return the minimum roof length needed to cover k cars.
    * Runtime: O(NlogN), Space: O(1)
* [Partitioning Array](partitioning_array_length_k.py)
    * Given an array of integers and integer k, return "Yes" if it's possible to partition the array into some
    subsequences of length k each such that each element in the array occurs in exactly one subsequence, all the numbers
    in a subsequence are distinct, and elements in the array having the same value must be in different subsequences; or
    "No" otherwise.
    * Runtime: O(N), Space: O(N)
* [Separating Students](separating_students.py)
    * Given an array of 0's and 1's, return the minimum number of swaps it takes to get all 0's on one side and all 1's
    on the other side.
    * Runtime: O(N), Space: O(1)
* [Shopper's Delight](shoppers_delight.py)
    * Given 4 arrays, each containing the price per unit for that particular item, and a budget; return the number of
    ways the shopper can purchase all 4 items.
    * Runtime: O(N^3), Space: O(N)? where N is the average length of the 4 arrays
* [Triplets](triplets.py)
    * Given array of n distinct integers d and integer threshold t, return number of (a, b, c) index triplets that
    satisfy d[a] < d[b] < d[c] and d[a] + d[b] + d[c] <= t
    * Runtime: O(N^2), Space: O(N)
    * See [Three Sum Smaller](../arrays/three_sum_smaller.py)

### Regex

* [Regex Sheet](regex.md)
* [Detecting Valid Latitude and Longitude Pairs](detecting_valid_latitude_longitude_pairs.py)
    * Given a list of strings that may represent latitude/longitude pairs, print "Valid" or "Invalid" for each test.
    * Runtime: O(N * M), Space: O(1) where N is the number of pairs in coordinates and M is average length of each
* [Valid Email Address](valid_email_addresses.py)
    * Given an email address, return True if valid and False otherwise.
    * Runtime: O(N), Space: O(1)

### Strings

* [Passage Filter](passage_filter.py)
    * Given a string representing a sequence of passages delimited by the '|' character, return a string representing
    the passages after filtering for certain rules and duplicates.
    * Runtime: O(M * N^2) where M is the average length of a passage and N is the number of passages, Space: O(N)
* [Perfect Team](perfect_team.py)
    * Given a string skills, return the total number of different teams satisfying the following: a team consists of 5
    students, each student is skilled in different subject, and a student may be on one team.
    * Runtime: O(N), Space: O(N)
* [Shifting Strings](shifting_strings.py)
    * Given string s, number of times to shift left, and number of times to shift right; return the string after
    performing the shifts.
    * Runtime: O(N), Space: O(1)
* [Two Strings](two_strings.py)
    * Given two arrays each containing N strings, for each index print whether the corresponding elements contain a
    common substring.
    * Runtime: O(N), Space: O(M) where M is the longest length of any string in either array
* [Who is the Closest](who_is_the_closest.py)
    * Given a string s of size m and an integer array queries of size n, return an integer array of size n that denotes
    the answer of each query.
    * Runtime: O(M + N * M)? Space: O(M)
    
### Other

* [Large Responses](large_responses.py)
    * Given a text file name containing a log on each line, parse through the file and create a file containing the
    number of requests that have more than 5000 bytes in their response and the total number of bytes sent by these responses.
    * Runtime: O(NM) where N is the number of lines in the file and M is the length of the longest log, Space: O(1)
* [Purchasing Supplies](purchasing_supplies.py)
    * Given integer budget n, unit cost of container, and integer number of empty containers to return for a free
    container m; return maximum number of empty containers a customer can receive.
    * Runtime: O(logN), Space: O(1)
    
### Linux

* [Basic Linux Interview Questions](../linux/linux-interview-questions.md)
* [Linux Commands in DevOps](../linux/linux-basics.md)
* [Docker: Environment Variables Task](../linux/docker.md)
    * Complete a file stub `script.sh` with one or more steps that does the following: runs a new Docker container
    'my-container' from the 'busybox' image (latest tag) in interactive background mode, with pseudo-TTY allocation; and
    passes an existing environment variable "MY_ENVIRONMENT_VARIABLE" to the "my-container" container.
