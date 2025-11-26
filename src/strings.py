from datastructures import Stack

def is_balanced_parentheses(s):
    """ Takes a string s containing characters like ()[]{} (and maybe others mixed in).
            Returns:True if all brackets are properly opened/closed and nested.
            False otherwise."""
    my_stack = Stack()

    matching = {
        ')':'(', 
        ']':'[',
        '}':'{',
    }

    # Check for opening brackets
    for ch in s:
        if ch in "([{": 
            my_stack.push(ch)
   # Check for closing brackets
        elif ch in ")]}":
            # 1) if stack is empty -> False
            if my_stack.is_empty():
                return False
            # 2) pop top opening
            top = my_stack.pop()
            # 3) check if it matches
            if matching[ch] != top: 
                return False
     
    return my_stack.is_empty()
    
if __name__== "__main__":
    # Test Cases
    print(is_balanced_parentheses("()"))        # True
    print(is_balanced_parentheses("([])"))      # True
    print(is_balanced_parentheses("([)]"))      # False
    print(is_balanced_parentheses("((("))       # False
    print(is_balanced_parentheses("([{}])"))    # True
    print(is_balanced_parentheses(")("))        # False  
