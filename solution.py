import copy
#constant
CONSECUTIVE_DAYS = 4
CONSECUTIVE_DAYS_CONSTANT = CONSECUTIVE_DAYS * "A"

class Solution:
    def __init__(self, days):
        self.days = days
        self.ways_to_attend = self._ways_to_attend_classes()

    def _ways_to_attend_classes(self):
        arr = []
        pattern = ""
        self._recursion(self.days, pattern, arr)
        return arr
    def _recursion(self, days, pattern, arr):
        if days == 0:
            arr.append(pattern)
        else:
            # At any given day there are only two possibilities
            self._recursion(days - 1, pattern + 'A', arr)  # absent in class
            self._recursion(days - 1, pattern + 'P', arr)  # present in class

    def _valid_number_of_days(self):
        return len(self.ways_to_attend) - len(self._ineligible_ways_to_attend_classes())
    def _ineligible_ways_to_attend_classes(self):
        # Filter out ways where 4 or more consecutive days classes are missed
        ineligible_list = list(filter(lambda way: CONSECUTIVE_DAYS_CONSTANT in way, self.ways_to_attend))
        return ineligible_list

    def _remove_common(self):
        a = self._ways_to_attend_classes()
        b = self._ineligible_ways_to_attend_classes()
        for i in a[:]:
            if i in b or i[-1] != 'A':
                a.remove(i)
        return len(a)


