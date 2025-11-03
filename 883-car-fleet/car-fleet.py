class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
       
        stack = [] 

        for p, s in cars:
            # Calculate the time it takes for the current car to reach the target.
            time_to_target = (target - p) / s

            # If the stack is empty, this car forms a new fleet.
            # Or if the current car takes longer to reach the target than the leading car of the last fleet,
            # it also forms a new fleet.
            if not stack or time_to_target > stack[-1]:
                stack.append(time_to_target)
                fleets += 1

        return fleets