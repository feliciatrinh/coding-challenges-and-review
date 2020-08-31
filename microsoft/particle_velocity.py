"""
Similar to Leetcode 413. Arithmetic Slices

Input: array of N positions of a particle
Output: number of periods of time when the movement of the particle was stable

Movement of a particle is stable when the velocity remains the same.
You need at least 3 measurements to be sure that a particle didn't change its velocity.

Example
1, 3, 5, 7, 9 is stable (velocity is 2)
7, 7, 7, 7 is stable (velocity is 0)
1, 1, 2, 5, 7 is not stable

Input: [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
Output: 5
The five periods during which particle is stable is (0, 2), (2, 4), (6, 8), (7, 9), (6, 9)

Ideas
- iterate through the input array and keep track of the current velocity and the number of times the velocity remains
  the same
- if the velocity remains the same t times, then the number of periods during which movement is stable is
  [t * (t - 1) / 2] - t from the summation formula
  - 2 times like in [1, 1, 1] gives you 1
  - 3 times like in [1, 1, 1, 1] gives you 1 + 2
  - 4 times like in [1, 1, 1, 1, 1] gives you 1 + 2 + 3
  - summation of i from i = 1 to i = n is n * (n + 1) / 2
"""


def particle_velocity(arr):
    """
    Runtime: O(N), Space: O(1)
    """
    if len(arr) < 3:
        return 0

    count = 0
    vel_count = 1
    prev_vel = arr[1] - arr[0]
    for i in range(2, len(arr)):
        curr_vel = arr[i] - arr[i - 1]
        if curr_vel == prev_vel:
            vel_count += 1
        if (vel_count >= 2 and curr_vel != prev_vel) or i == len(arr) - 1:
            count += vel_count * (vel_count + 1) // 2 - vel_count
            vel_count = 1
        prev_vel = curr_vel
    if count > 10**9:
        return -1
    return count


assert particle_velocity([1, 3, 5, 7, 9]) == 6
assert particle_velocity([-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]) == 5
assert particle_velocity([1, 1, 2, 5, 7]) == 0
assert particle_velocity([3, -1, -5, -9]) == 3
assert particle_velocity([0, 1]) == 0
assert particle_velocity([1, 1, 1]) == 1
