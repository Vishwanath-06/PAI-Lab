import heapq

class AStar:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start_node, goal_node):
        open_list = []
        g_costs = {start_node: 0}
        came_from = {start_node: None}
        initial_f_score = g_costs[start_node] + self.heuristic(start_node, goal_node)
        heapq.heappush(open_list, (initial_f_score, g_costs[start_node], start_node))
        closed_nodes = set()

        while open_list:
            current_f_score, current_g_cost, current_node = heapq.heappop(open_list)

            if current_node in closed_nodes:
                continue

            if current_node == goal_node:
                return self._reconstruct_path(came_from, current_node), g_costs[current_node]

            closed_nodes.add(current_node)

            for neighbor, edge_weight in self.graph.get(current_node, []):
                tentative_g_cost = current_g_cost + edge_weight
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_score = tentative_g_cost + self.heuristic(neighbor, goal_node)
                    heapq.heappush(open_list, (f_score, tentative_g_cost, neighbor))
                    came_from[neighbor] = current_node

        return None, float('inf')

    def _reconstruct_path(self, came_from, current_node):
        path = []
        while current_node is not None:
            path.append(current_node)
            current_node = came_from[current_node]
        path.reverse()
        return path

if __name__ == "__main__":
    graph = {
        'S': [('A', 1), ('B', 4)],
        'A': [('C', 3), ('D', 2)],
        'B': [('D', 5)],
        'C': [('G', 2)],
        'D': [('G', 1)],
        'G': []
    }

    def heuristic(node, goal):
        h_values = {
            'S': 6,
            'A': 5,
            'B': 3,
            'C': 2,
            'D': 1,
            'G': 0
        }
        return h_values.get(node, float('inf'))

    astar = AStar(graph, heuristic)
    path, total_cost = astar.search('S', 'G')

    if path:
        print(f"Path found: {path}")
        print(f"Total cost: {total_cost}")
    else:
        print("No path found from start to goal.")
