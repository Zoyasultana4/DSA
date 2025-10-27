class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
      
        # Initialize count of intervals to remove (start with total count)
        intervals_to_remove = len(intervals)
      
        # Track the end point of the last non-overlapping interval kept
        previous_end = -inf
      
        # Iterate through sorted intervals
        for start, end in intervals:
            # If current interval doesn't overlap with the previous kept interval
            if previous_end <= start:
                # We can keep this interval, so decrement the removal count
                intervals_to_remove -= 1
                # Update the end point of the last kept interval
                previous_end = end
      
        return intervals_to_remove
