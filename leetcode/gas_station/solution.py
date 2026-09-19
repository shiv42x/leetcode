class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        num_gas_stations = len(gas) 
        for i in range(num_gas_stations):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res