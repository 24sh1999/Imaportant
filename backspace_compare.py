class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        for i in range(len(S)):
            if S[i] != '#':
                stack1.append(S[i])
            elif len(stack1) > 0:
                stack1.pop()
        
        stack2 = []
        for i in range(len(T)):
            if T[i] != '#':
                stack2.append(T[i])
            elif len(stack2) > 0:
                stack2.pop()
        
        return stack1 == stack2
