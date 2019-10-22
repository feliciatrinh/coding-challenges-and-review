/*
Input: read lines from std input l; each line contains a msg sent from John.
Output: print "YES" or "NO" stating whether it's possible msg had balanced parentheses.
Runtime O(n)

From Facebook 2013 Hackathon challenge

A msg has balanced parentheses if it has one or more of the following:
1. an empty string
2. one or more of the characters 'a' to 'z', ' ' (a space), or ':' (a colon)
3. an open parenthesis '(' followed by a msg with balanced parentheses followed by a close parenthesis ')'
4. a msg with balanced parentheses followed by another msg with balanced parentheses
5. a smiley face ':)' or a sad face ':('

Method 1: Use a stack. Runtime O(n). Would need a lot of if conditions to distinguish between balanced parentheses and emoticons in (:) 
Method 2: Keep track of the number of open parentheses you have left by the end of the expression. 0 indicates balanced.
Doesn't work because of expressions like '(:)' where a part of it can be interpreted as balanced parentheses or an emoticon.
Method 3: Keep track of the number of allowable parentheses (prioritized emoticons)
and the minimum number of open parentheses possible (prioritized balanced '()' expressions). Print YES if allowable >= 0 and minimum == 0.
*/
import java.io.*;
import java.nio.charset.StandardCharsets;

public class Solution {
	public static void main(String[] args) throws IOException {
		InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
		BufferedReader in = new BufferedReader(reader);
		String line;
		while ((line = in.readLine()) != null) {
			int allowableOpenCount = 0; // count prioritizes emoticons
			int leastOpenCount = 0; // count prioritizes traditional balanced parentheses
			for (int i = 0; i < line.length(); i++) {
				allowableOpenCount += 1;
				if (((Character) line.charAt(i)).equals('(')) {
					if (i == 0 || !(((Character) line.charAt(i - 1)).equals(':'))) {
						leastOpenCount += 1; // doesn't count ':('
					}
				} else if (((Character) line.charAt(i)).equals(')')) {
					leastOpenCount = (leastOpenCount - 1 < 0) ? 0: leastOpenCount - 1; 
					if (i == 0 || !(((Character) line.charAt(i - 1)).equals(':'))) {
						allowableOpenCount -= 1; // doesn't count ':)'
					}
					if (allowableOpenCount < 0) { // allowable must be >= 0
						break;
					}
				}
			}
			if (leastOpenCount == 0 && allowableOpenCount >= 0) {
				System.out.println("YES");
			} else {
				System.out.println("NO");
			}
		}
	}	
}
