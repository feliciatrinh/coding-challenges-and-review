"""
Input: text file name
Output: a file names bytes_filename.txt containing the number of requests that have more than 5000 bytes on one line
        and the total sum of bytes sent by all responses sending more than 5000 bytes on the second line.

Each line in the text file contains a single log record with 7 different space-separated columns. The last column is the
number of bytes in the response.

Example
Input: input1.txt
Output: a file called bytes_input1.txt containing something similar to '3\n18000\n'
"""


def large_responses(filename):
    """
    Runtime: O(NM) where N is the number of lines in the file and M is the length of the longest log, Space: O(1)
    """
    import os
    file_path = os.path.join(os.path.dirname(__file__), filename)

    num_reqs = 0
    total_bytes = 0
    with open(file_path, 'r') as f:
        for line in f:
            num_bytes = int(line.split(" ")[-1].strip('\n '))
            if num_bytes > 5000:
                num_reqs += 1
                total_bytes += num_bytes

    output_path = os.path.join(os.path.dirname(__file__), "bytes_" + filename)
    with open(output_path, 'w') as f:
        f.write("{}\n{}\n".format(num_reqs, total_bytes))

