class Solution:
    def reverse(self, stack): 
        if len(stack) <= 1:
            return
        top = stack.pop()
        self.reverse(stack)
        stack.insert(0, top)