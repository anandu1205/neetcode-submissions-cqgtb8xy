from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        # stop -> buses
        stop_to_buses = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                stop_to_buses[stop].append(i)
        
        visited_buses = set()
        visited_stops = set([source])
        
        q = deque([(source, 0)])  # (current_stop, buses_taken)
        
        while q:
            stop, buses = q.popleft()
            
            for bus in stop_to_buses[stop]:
                if bus in visited_buses:
                    continue
                
                visited_buses.add(bus)
                
                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses + 1
                    
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, buses + 1))
        
        return -1
        