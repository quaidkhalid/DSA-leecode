class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for val in asteroids:
            if val>0:
                st.append(val)
            else:
                while len(st)>0 and abs(val)>st[-1] and st[-1]>0:
                    st.pop()
                if len(st)==0 or st[-1]<0:
                    st.append(val)
                if len(st)>0 and st[-1]==abs(val):
                    st.pop()
        reversed(st)
        return st
        # stack = []
        # for val in asteroids:
        #     if val > 0:
        #         stack.append(val)
        #     else:
        #         while stack and stack[-1] < abs(val) and stack[-1] > 0:
        #             stack.pop()
        #             if len(stack) == 0 or stack[-1] < 0:
        #                 stack.append(val)
        #             if len(stack) > 0 and stack[-1] == abs(val):
        #                 stack.pop()
        # reversed(stack)
        # return stack
        