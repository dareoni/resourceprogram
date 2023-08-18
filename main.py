# Test case
resources = {
    'Task1': [10],
    'Task2': [10],
    'Task3': [5],
    'Task4': [12]
}


def is_valid_move(resources, task, load_balancer_capacity):
    """
    Check if the move is valid, i.e., the task's resource usage does not exceed the load balancer's capacity.
    """
    return sum(resources[task]) <= load_balancer_capacity

def resource_allocation_backtrack(resources, task_list, current_allocation, load_balancer_capacity, best_allocation):
    """
    Recursive function to find resource allocation using backtracking.
    """
    if len(current_allocation) == len(task_list):
        # Check if the current allocation is better than the best allocation found so far
        if sum(resources[task][0] for task in current_allocation) > sum(resources[task][0] for task in best_allocation):
            best_allocation.clear()
            best_allocation.extend(current_allocation)
        return

    for task in task_list:
        if task not in current_allocation and is_valid_move(resources, task, load_balancer_capacity):
            current_allocation.append(task)
            resource_allocation_backtrack(resources, task_list, current_allocation, load_balancer_capacity, best_allocation)
            current_allocation.pop()

def allocate_resources(resources, load_balancer_capacity):
    """
    Main function to allocate resources using backtracking.
    """
    task_list = list(resources.keys())
    best_allocation = []
    resource_allocation_backtrack(resources, task_list, [], load_balancer_capacity, best_allocation)

    return best_allocation

if __name__ == "__main__":

    load_balancer_capacity = 20
    best_allocation = allocate_resources(resources, load_balancer_capacity)

    if best_allocation:
        print("Best resource allocation:")
        for task in best_allocation:
            print(f"{task}: {resources[task][0]}")
    else:
        print("No valid resource allocation found.")
