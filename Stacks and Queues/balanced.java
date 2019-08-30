// Returns true is a string consisting of '{', '}', '[', ']' is balanced. "{[{}]}" is balanced. 
public statis boolean balanced(String str) {
  Stack<Character> stack = new Stack<Character>(); 
  for (int i = 0; i < str.length(); i++) {
    switch (str.charAt(i)) {
      case '{': 
        stack.push; 
        break; 
      case '[': 
        stack.push; 
        break;
      case '}': 
        if (stack.pop() != '{') {
          return false; 
          break; 
        }
      case ']': 
        if (stack.pop() != '[') {
          return false; 
          break; 
        }
      }
    }
  return stack.isEmpty();   
}
