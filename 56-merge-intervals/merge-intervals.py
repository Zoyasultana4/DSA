class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

    # Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
        # If the merged list is empty or the current interval does not overlap
        # with the last merged interval, add it directly.
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
            # If there is an overlap, merge the current interval with the last
            # merged interval by updating the end time of the last merged interval.
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged