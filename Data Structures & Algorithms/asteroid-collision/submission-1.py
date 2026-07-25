class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        rules:
        the each astroid is a vector with
        indicies: position, sign: direction, value: size

        two astroids with the same sign never meed
        if two astroids collide the smaller one dissapears
        if both are the same size then they both dissapear

        note: an astroid moving won't stop until it is either destroyed or has nothing else to hit

        we want to use a stack to store the output but we have to consdier that we only handle 
        the processing logic if the stack has something and the top of the stack and 
        the the top of stack + astroid are moving towards each other. 
        we will do this for every astroid in the list
        """
        stack = []
        for asteroid in asteroids:
            destroyed = False

            while stack and (stack[-1] > 0 and asteroid < 0): #checks that they are moving towwards each other
                # collision logic
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    destroyed = True
                    break #both astroids busted
                elif abs(stack[-1]) < abs(asteroid):
                    stack.pop() # smaller astroid was the one on the stack
                else:
                    destroyed = True
                    break #means the incoming astroid busted
                
            if not destroyed:
                stack.append(asteroid)

        return stack
            