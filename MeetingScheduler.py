class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        OPEN, CLOSE = 0, 1
        events = []

        # we add all intervals from person 1 and person 2, using start/end events
        for start, end in slots1:
            events.append((start, OPEN, 1, end))
            events.append((end, CLOSE, 1, end))

        for start, end in slots2:
            events.append((start, OPEN, 2, end))
            events.append((end, CLOSE, 2, end))

        events.sort()
        seen = {}

        """
            for every event, add and remove any interval, based on the open/close events we set above, to our seen dict
            this will produce a window, where at any given point, we can track if intervals overlap
            since we only have two people, we can hard code the dict keys as seen above
        """
        for time, eventType, person, end in events:
            if (
                eventType is OPEN
            ):  # this is the start of an interval, add the person to the dict
                seen[person] = (person, end)
            else:  # end of a given interval, remove this person
                del seen[person]

            # if we have an overlap, where both persons have intervals that coincide
            if len(seen) > 1:
                # grab the end values for each, since what we care about is whether at any given time point, does time + duration fit?
                person1, person1End = seen.get(1)
                person2, person2End = seen.get(2)

                if time + duration <= person1End and time + duration <= person2End:
                    return [time, time + duration]

        return []


if __name__ == "__main__":
    sol = Solution()
    slots1 = [[10, 50]]
    slots2 = [[1, 15], [17, 60]]
    duration = 15
    res = sol.minAvailableDuration(slots1, slots2, duration)
    print(res)
