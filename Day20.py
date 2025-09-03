class Solution:
    def sortStack(self, stack):
        if len(stack) <= 1:
            return
        
        top = stack.pop()

        self.sortStack(stack)
    
        self.insertInSortedOrder(stack, top)
    
    def insertInSortedOrder(self, stack, element):
        if not stack or element > stack[-1]:
            stack.append(element)
            return
        
        top = stack.pop()
        self.insertInSortedOrder(stack, element)
        stack.append(top)

stack = [3, 1, 4, 2]
sol = Solution()
sol.sortStack(stack)
print(stack)   