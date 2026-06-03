# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
def isValid(s: str) -> bool:
    stack = []
    mapping = {'(': ')', '{': '}', '[': ']'}
    open_paren = list(mapping.keys())
    closed_paren = list(mapping.values())
    for c in s:
        if c in open_paren:
            stack.append(c)
        elif c in closed_paren:
            if len(stack) == 0:
                return False
            last = stack.pop()
            if mapping[last] != c:
                return False
    return len(stack) == 0