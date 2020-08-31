"""
Input: list of Message objects containing a type and an owner
Output: One possible assignment of client-IDs to B-type messages which will make the sequence valid.

- For each client, messages can't be sent out of order; it must be A then B then C
- log contains messages from several clients
- messages in log are in chronologically order
- A-type and C-type are signed with the client-ID, B-type messages are not signed
- For every A-type message, there is a corresponding B-type and C-Type message

Example
Input: "A2 B A1 B C1 C2"
Output: "A2 B2 A1 B1 C1 C2"

Input: "A1 B A2 B C1 C2"
Output: "A1 B1 A2 B2 C1 C2"

Input: "A1 A2 B C2 B C1"
Output: "A1 A2 B2 C2 B1 C1"

Input: "A2 A1 B B C2 C1"
Output: "A2 A1 B1 B2 C2 C1" or "A2 A1 B2 B1 C2 C1"

Input: "A2 A1 B C2 B C1"
Output: "A2 A1 B2 C2 B1 C1"

Input: "A1 B C1 A2 B C2"
Output: "A1 B1 C1 A2 B2 C2"

Input: "A2 B A1 C2 B C1"
Output: "A2 B2 A1 C2 B1 C1"

Input: "A1 A2 B C2 B A3 B C3 C1"
Output: "A1 A2 B2 C2 B1 A3 B3 C3 C1"

Input: "A3 A1 B B C3 A2 C1 B A1 C2 B C1"
Output: "A3 A1 B3 B1 C3 A2 C1 B2 A1 C2 B1 C1" or "A3 A1 B1 B3 C3 A2 C1 B2 A1 C2 B1 C1"
"""


class Message:
    def __init__(self, m_type, client_id=None):
        self.m_type = m_type
        self.client_id = client_id

    def __str__(self):
        return "{}{}".format(self.m_type, self.client_id)


def assign(messages):
    """
    Runtime: O(N), Space: O(N)
    """
    A_stack = []
    B_stack = []
    C_stack = []
    for message in messages:
        if message.m_type == "A":
            A_stack.append(message)
        elif message.m_type == "B":
            B_stack.append(message)
        else:
            C_stack.append(message)
            while C_stack and A_stack and C_stack[-1].client_id == A_stack[-1].client_id:
                B_stack.pop().client_id = C_stack.pop().client_id
                A_stack.pop()

    result = ''
    for message in messages:
        result += str(message) + ' '
    return result.strip()


assert assign([Message("A", 2), Message("B"), Message("A", 1), Message("B"), Message("C", 1), Message("C", 2)])\
       == 'A2 B2 A1 B1 C1 C2'
assert assign([Message("A", 1), Message("B"), Message("A", 2), Message("B"), Message("C", 1), Message("C", 2)])\
       == 'A1 B1 A2 B2 C1 C2'
assert assign([Message("A", 1), Message("A", 2), Message("B"), Message("C", 2), Message("B"), Message("C", 1)])\
       == 'A1 A2 B2 C2 B1 C1'
assert assign([Message("A", 2), Message("A", 1), Message("B"), Message("B"), Message("C", 2), Message("C", 1)])\
       == 'A2 A1 B2 B1 C2 C1'
assert assign([Message("A", 2), Message("A", 1), Message("B"), Message("C", 2), Message("B"), Message("C", 1)])\
       == 'A2 A1 B2 C2 B1 C1'
assert assign([Message("A", 1), Message("B"), Message("C", 1), Message("A", 2), Message("B"), Message("C", 2)])\
       == "A1 B1 C1 A2 B2 C2"
assert assign([Message("A", 2), Message("B"), Message("A", 1), Message("C", 2), Message("B"), Message("C", 1)])\
       == "A2 B2 A1 C2 B1 C1"
assert assign([Message("A", 1), Message("A", 2), Message("B"), Message("C", 2), Message("B"), Message("A", 3),
               Message("B"), Message("C", 3), Message("C", 1)]) == "A1 A2 B2 C2 B1 A3 B3 C3 C1"
assert assign([Message("A", 3), Message("A", 1), Message("B"), Message("B"), Message("C", 3), Message("A", 2),
               Message("C", 1), Message("B"), Message("A", 1), Message("C", 2), Message("B"), Message("C", 1)])\
       == "A3 A1 B3 B1 C3 A2 C1 B2 A1 C2 B1 C1"
