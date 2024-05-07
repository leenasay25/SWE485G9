import numpy as np
import copy
import random
import time

class LocalSearch:

    def __init__(self):
        self.best_solution = None
        self.best_cost = float('inf')

    def generate_initial_solution(self, cost_matrix):
        # Generate an initial solution using a random assignment
        num_agents, num_tasks = cost_matrix.shape
        initial_solution = np.random.permutation(num_tasks)
        return initial_solution

    def calculate_cost(self, cost_matrix, assignment):
        # Calculate the total cost of the assignment
        total_cost = 0
        for agent, task in enumerate(assignment):
            total_cost += cost_matrix[agent, task]
        return total_cost


    def generate_neighborhood(self, current_solution):
        # Generate neighboring solutions by swapping tasks between agents
        neighborhood = []
        num_agents = len(current_solution)
        for i in range(num_agents):
          for j in range(i+1, num_agents):
                neighbor = copy.deepcopy(current_solution)
                neighbor[i], neighbor[j] = neighbor[j], neighbor[i] # Swap tasks
                neighborhood.append(neighbor)
        return neighborhood

    
    def local_search(self, cost_matrix, max_iterations):
        # Perform local search to find the best assignment
        current_solution = self.generate_initial_solution(cost_matrix)
        current_cost = self.calculate_cost(cost_matrix, current_solution)

        for _ in range(max_iterations):
            neighborhood = self.generate_neighborhood(current_solution)
            for neighbor in neighborhood:
                neighbor_cost = self.calculate_cost(cost_matrix, neighbor)
                if neighbor_cost < current_cost:
                    current_solution = neighbor
                    current_cost = neighbor_cost
        # Update the best solution if necessary
            if current_cost < self.best_cost:
                self.best_solution = current_solution
                self.best_cost = current_cost
        return self.best_solution, self.best_cost


    def binary_assignment_matrix(self, assignment, num_agents, num_tasks):
        # Generate the binary assignment matrix
        binary_matrix = np.zeros((num_agents, num_tasks))
        for agent, task in enumerate(assignment):
                 binary_matrix[agent, task] = 1
        return binary_matrix

    @staticmethod
    def generate_random_above_10():
        return random.randint(9, 9)

    # Test the local search algorithm
if __name__ == "__main__":
        np.random.seed(42)
        size = LocalSearch.generate_random_above_10()
        cost_matrix = np.random.randint(0, 100, size=(size, size))
        print("Cost matrix of size", size,"x", size)
        print(cost_matrix)
        
        # Record start time
        start_time = time.time()
        local_search = LocalSearch()
        best_assignment, best_cost = local_search.local_search(cost_matrix, max_iterations=1000)
        
        # Record end time
        end_time = time.time()
        
        # Calculate computational time
        computational_time = end_time - start_time
        print("\nBest assignment found:")
        print(best_assignment)

        binary_matrix = local_search.binary_assignment_matrix(best_assignment, cost_matrix.shape[0], cost_matrix.shape[1])
        print("\nBinary assignment matrix:")
        print(binary_matrix)
        print("Assignment problem best cost result:", best_cost)
        print(f"Computational time: {computational_time} seconds")
