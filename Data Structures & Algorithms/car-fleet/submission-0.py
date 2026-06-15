class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        The most streight forward way to do this would be to store a priority queue.

        That priority queue would store the distance of the car to the target (target - position[i])
        multiplied by the recripricol of speed to get the hours.

        We also need to know the slowest car ahead of the current car. The slowest car will be the car
        that limits the speed of the curent car and creates the bottle neck for the queue. 
        """
        pairs: List[Tuple[int, int]] = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack: List[float] = [] # The intuition here is the stack holds the number of fleets
        # We are iterating in asending order, from lowest (p, s) to highest.
        for p, s in pairs:
            hours_to_target: float = (target - p) / s
            stack.append(hours_to_target)
            # This is saying we have two cars in the stack that could form a fleet.
            # If the hours to target in the last poisition is faster or equal to the 
            # hours in the second to last, we pop that item off as part of the fleet. 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
