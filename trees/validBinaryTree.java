/*
Input: binary tree as a sequence of parent-child pairs
Output: highest priority error or nothing if there're no errors

Input format: 
- one line
- no leading or trailing white spaces
- pairs are formatted as (A,B)
- only uppercase letters
- parent-child pairs are separated by a single whitespace
- sequeunce of pairs not in any particular order

Example: (A,B) (B,C) (A,E) (B,D)

Errors:
E1: invalid input format
E2: duplicate pair
E3: parent has more than two children
E4: multiple roots
E5: tree contains cycle
*/


import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String args[] ) throws Exception {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        // Invalid input formats: more than one line of input, leading or trailing whitespaces
        if (sc.hasNextLine()
                || ((Character) input.charAt(0)).equals(' ')
                || ((Character) input.charAt(input.length() - 1)).equals(' ')) {
            System.out.print("E1");
            return;
        }
        // Use a hashmap to hold parents as keys and the set of children as values.
        HashMap<Character, Set<Character>> tree = new HashMap<>();
        // Use Hashsets to keep track of the number of distinct vertices.
        // I previously used tree.containsValue() to keep track of distinct vertices, but it always returned false 
        // because I was modifying the values while building the hashmap.
        Set<Character> parentSet = new HashSet<>();
        Set<Character> childSet = new HashSet<>();
        // Keep track of the number of edges and nodes to check for multiple roots. 
        // I could have also just merged the parentSet and childSet together to get the number of distinct vertices.
        int edges = 0;
        int nodes = 0;
        // Need a flag for if there is a cycle if E5 appears before a potential E4, given interpretation 1,
        // because I can't check for if |E| == |V| - 1 until all pairs are put into the tree.
        boolean isCycle = false;
        // Could convert the string to a char array instead to iterate through the string
        // a character at a time unless the extra space is undesired.
        // Check for proper parent-child pair formatting
        for (int i = 0; i < input.length(); i++) {
            char parent = 0;
            char child = 0;
            if ((input.length() >= i + 5)
                    && ((Character) input.charAt(i)).equals('(')
                    && Character.isUpperCase(input.charAt(i + 1))
                    && ((Character) input.charAt(i + 2)).equals(',')
                    && Character.isUpperCase(input.charAt(i + 3))
                    && ((Character) input.charAt(i + 4)).equals(')')) {
                parent = input.charAt(i + 1);
                child = input.charAt(i + 3);
            } else {
                System.out.print("E1");
                return;
            }
            i += 5;
            if (parentSet.contains(parent)) {
                Set<Character> children = tree.get(parent);
                if (children.contains(child)) {
                    System.out.print("E2"); // Duplicate pair
                    return;
                }
                if (children.size() >= 2) {
                    System.out.print("E3"); // Parent will have more than 2 children.
                    return;
                }                   
                if (!(parentSet.contains(child) || childSet.contains(child))) {
                    nodes += 1;
                }
                children.add(child);
                edges += 1;
            } else if (childSet.contains(child) && !childSet.contains(parent)) { // Multiple roots
                System.out.print("E4");
                return;
            } else if (childSet.contains(parent) && (childSet.contains(child) || parentSet.contains(child))){
                isCycle = true; // Tree contains a cycle
            } else {
                Set<Character> children = new HashSet<>();
                children.add(child);
                // check if parent is already in the tree.
                if (!(childSet.contains(parent))) {
                    nodes += 1;
                }
                // check if child is already in the tree.
                if (!(childSet.contains(child) || parentSet.contains(child))) {
                    nodes += 1;
                }
                tree.put(parent, children);
                edges += 1;
            }
            parentSet.add(parent);
            childSet.add(child);
        }
        if (edges < nodes - 1) {
            System.out.print("E4");
        } else if (isCycle) {
            System.out.print("E5");
        }
        // Interpretation 1
        // A tree has multiple roots if there is more than one connected component.
        // If there is less than |V| - 1 edges, then there is more than one connected comp and therefore multiple roots.
        // However, if there are cycles within individual connected components, there could be more than
        // |V| - 1 edges but have more than one connected component.

        // Interpretation 2
        // A tree has multiple roots if there is more than one parent with at
        // least one child in common and said parent is not yet already in the tree.
        // In other words, a child has more than one parent.

        // A tree contains a cycle when there is a back edge, an edge from
        // a descendant to an ancestor.
        // I could use the hashmap for O(1) lookup if the extra space isn't an issue.
        // There will be a cycle if a child in a parent-child pairing
        // is already in the tree (as either a leaf or non-leaf) and the parent is already in the tree.
        // Or there is a cycle if the parent of a child is itself.
    }
}