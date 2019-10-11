"""
Input: Array with integer lengths pieces of bamboo
Output: Array of integers each the number of pieces of bamboo at the start of a turn.

Repeatedly performs the following:
1. Count the number of pieces of bamboo
2. Find the shortest length piece(s)
3. Discard any piece of that length
4. Cut that shortest length from each of the longer pieces.
5. Repeat until there are no more pieces.

Examples

lengths 	cut length 		pieces
1 1 3 4			1				4
    2 3   		2				2
      1			1				1
Output: [4, 2, 1]

lengths		cut length   	pieces
2 2 8 8			2				4
    6 6			6				2
Output: [4, 2]

"""

def cut_bamboo(lengths):
	pieces = [] # number of pieces at the start of each turn
	numPieces = len(lengths)
	while numPieces > 0:
		piecesRemoved = 0
		minLength = min(lengths)
		pieces.append(len(lengths))
		for i in range(len(lengths)):
			if lengths[i] == minLength:
				numPieces -= 1
				piecesRemoved += 1
			lengths[i] -= minLength
		for j in range(piecesRemoved):
			lengths.remove(0)
	return pieces
