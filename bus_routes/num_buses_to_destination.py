from collections import defaultdict, deque


class Solution:
    def num_buses_to_destination(self, routes: list[list[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        
        # Map each stop to the set of bus routes that pass through it
        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_stops = set()      # Set of stops we've already visited
        visited_routes = set()     # Set of bus routes we've already used
        queue = deque([(source, 0)])  # Queue holds (current_stop, buses_taken_so_far)

        while queue:
            current_stop, buses_taken = queue.popleft()

            # If we reach the target stop, return the number of buses taken
            if current_stop == target:
                return buses_taken

            visited_stops.add(current_stop)

            # Explore all routes available from this stop
            for route_index in stop_to_routes[current_stop]:
                if route_index in visited_routes:
                    continue  # Skip if we’ve already used this route
                visited_routes.add(route_index)

                # Add all stops from this route to the queue
                for next_stop in routes[route_index]:
                    if next_stop not in visited_stops:
                        queue.append((next_stop, buses_taken + 1))

        # If we exhaust the queue without reaching the target, it's unreachable
        return -1


# Example usage
obj = Solution()
# routes = [[1,7],[3,5]]
# source = 1
# target = 1

routes = [[1,2,7],[3,6,7]]
source = 1
target = 6

# routes = [[3,6,5],[1,2,7],[3,7,5]]
# source = 1
# target = 6

# routes = [[24],[3,6,11,14,22],[1,23,24],[0,6,14],[1,3,8,11,20]]
# source = 20
# target = 8

# routes = [[3,6,5],[15,16,41,47],[1,2,7],[7, 18, 23, 24], [3,7,5],[7,14,33]]
# source = 7
# target = 47

# routes = [[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]]
# source = 7
# target = 47

# routes = [[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,14,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]]
# source = 7
# target = 5

routes = [[3,16,33,45,59,79,103,135],[3,35,39,54,56,78,96,101,120,132,146,148],[13,72,98],[37,70,107],[0,12,31,37,41,68,78,94,100,101,113,123],[11,32,52,85,135],[43,50,128],[0,13,49,51,53,55,60,65,66,80,82,87,92,99,112,118,120,125,128,131,137],[15,19,34,37,45,52,56,97,108,123,142],[7,9,20,28,29,33,34,38,43,46,47,48,53,59,65,72,74,80,88,92,110,111,113,119,135,140],[15,41,64,83],[7,13,26,31,57,85,101,108,110,115,119,124,149],[47,61,67,70,74,75,77,84,92,101,124,132,133,142,147],[0,2,5,6,12,18,34,37,47,58,77,98,99,109,112,131,135,149],[6,7,8,9,14,17,21,25,33,40,45,50,56,57,58,60,68,92,93,100,108,114,130,149],[7],[5,16,22,48,77,82,108,114,124],[34,71],[8,16,32,48,104,108,116,134,145],[3,10,16,19,35,45,64,74,89,101,116,149],[1,5,7,10,11,18,40,45,50,51,52,54,55,69,71,81,82,83,85,89,96,100,114,115,124,134,138,148],[0,2,3,5,6,9,15,52,64,103,108,114,146],[5,33,39,40,44,45,66,67,68,69,84,102,106,115,120,128,133],[17,26,49,50,55,58,60,65,88,90,102,121,126,130,137,139,144],[6,12,13,37,41,42,48,50,51,55,64,65,68,70,73,102,106,108,120,123,126,127,129,135,136,149],[6,7,12,33,37,41,47,53,54,80,107,121,126],[15,75,91,103,107,110,125,139,142,149],[18,24,30,52,61,64,75,79,85,95,100,103,105,111,128,129,142],[3,14,18,32,45,52,57,63,68,78,85,91,100,104,111,114,142],[4,7,11,20,21,31,32,33,48,61,62,65,66,73,80,92,93,97,99,108,112,116,136,139]]
source = 85
target = 112

print(obj.num_buses_to_destination(routes, source, target))





 