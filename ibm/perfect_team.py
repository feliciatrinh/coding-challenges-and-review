"""
Input: string skills
Output: total number of different teams satisfying the following: a team consists of 5 students, each student is skilled
in different subject, a student may be on one team

Each student is skilled in one subject. There are 5 subjects represented by the letters p, c, m, b, z.

5 <= n <= 5 * 10^5
skills[i] in set {p, c, m, b, z}

Example
Input: "pcmbzpcmbz"
Output: 2

Ideas
- create a counter dictionary mapping skill to number of students with that skill
- after iterating through the skills string and building the counter, iterate through the counter and keep track of the
  minimum num_students_with_skills
"""


def perfect_teams(skills):
    """
    Runtime: O(N), Space: O(N)
    """
    freq = {}
    for skill in skills:
        if skill in freq:
            freq[skill] += 1
        else:
            freq[skill] = 1

    # we don't have all 5 skills so we cannot form a team
    if len(freq) < 5:
        return 0

    num_teams = len(skills)
    for count in freq.values():
        num_teams = min(num_teams, count)
    return num_teams


assert perfect_teams("pcmbzpcmbz") == 2
assert perfect_teams("mppzbmbpzcbmpbmczcz") == 3
assert perfect_teams("pcmpp") == 0
assert perfect_teams("pcmbz") == 1
assert perfect_teams("pcmpcmbbbzz") == 2
