class Solution:
    def solveOp(self, op, values):
        """Evaluates the logical operation based on the operator and values."""
        if op == '!':
            # Negation: return False if value is True, else return True
            return 'f' if values[0] == 't' else 't'
        
        if op == '&':
            # And: return False if any value is False, else return True
            return 'f' if 'f' in values else 't'
        
        if op == '|':
            # Or: return True if any value is True, else return False
            return 't' if 't' in values else 'f'
    
    def parseBoolExpr(self, s: str) -> bool:
        """Parses the boolean expression and returns the result."""
        stack = []
        for char in s:

            if char == ',':
                continue

            elif char == ')':
                values = []

                # Gather all values inside the parentheses
                while stack[-1] != '(':
                    values.append(stack.pop())
                stack.pop()  # Remove '('
                op = stack.pop()  # Remove the operator
                stack.append(self.solveOp(op, values))
            else:
                stack.append(char)
                
        return stack[-1] == 't'