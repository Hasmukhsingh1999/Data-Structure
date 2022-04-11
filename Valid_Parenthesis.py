''' Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true '''


# braces = { '(' , '[' , '{'}

# for bracket in s:
#     if bracket == ')' or bracket == ']' or bracket == '}':
#         stack.append(bracket)
#     elif not  stack:
#         print(False)
#     elif bracket == '(' and stack[-1]=='(':
#         stack.pop()
#     elif bracket == '[' and stack[-1]=='[':
#         stack.pop()
#     elif bracket == '{' and stack[-1]=='{':
#         stack.pop()
#     else:
#         print(False)
brackets = {'(':')' , '[':']' , '{':'}'}
stack= {}
for key in brackets.keys():
    key+=stack
print(stack)




