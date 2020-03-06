class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        record, res = {} , []
        for i,val in enumerate(groupSizes):
            record.setdefault(val,[]).append(i)
            if len(record[val]) == val:
                res.append(record[val])
                record[val] = []
        return res