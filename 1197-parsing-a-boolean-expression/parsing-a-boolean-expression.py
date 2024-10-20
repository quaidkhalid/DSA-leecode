class Solution:
    def solveOp(self, op, values):
        if op == '!':
            return 'f' if values[0] == 't' else 't'
        
        if op == '&':
            return 'f' if 'f' in values else 't'
        
        if op == '|':
            return 't' if 't' in values else 'f'
    
    def parseBoolExpr(self, s: str) -> bool:
        stack = []
        for char in s:

            if char == ',':
                continue

            elif char == ')':
                values = []
                while stack[-1] != '(':
                    values.append(stack.pop())
                stack.pop()  # Remove '('
                op = stack.pop()  # Remove the operator

                stack.append(self.solveOp(op, values))

            else:
                stack.append(char)

        return stack[-1] == 't'