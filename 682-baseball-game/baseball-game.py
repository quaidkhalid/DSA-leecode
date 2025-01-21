class Solution:
    def calPoints(self, operations: List[str]) -> int:
        answer = []
        for i in operations:
            if i == "+":
                answer.append(answer[-1] + answer[-2])
            elif i == "D":
                answer.append(answer[-1] * 2)
            elif i == "C":
                answer.pop()
            else:
                answer.append(int(i))
        return sum(answer)
        