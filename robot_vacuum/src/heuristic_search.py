import copy
import heapq
from operators import is_goal_state, find_children

#Heuristic value creation
def heuristic(state):
    garbage_sum= sum(state[1:9])
    distance_to_base= abs(state[0]- state[-2])

    return garbage_sum+ distance_to_base


def best_first_search(initial_state):
    queue= []
    #Add the initial state to the queue
    #along with the heuristic value
    heapq.heappush(queue, (heuristic(initial_state), [initial_state]))
    closed= []
    #counter
    states_examined= 0

    while queue:
        #Remove the item with the highest priority from the queue and
        #assign it to the path variable and its heuristic value to h_value
        h_value, path= heapq.heappop(queue)
        current= path[-1] #path[-1] -> most recent state (current)
        path_new= path
        states_examined+= 1

        #If state has been examined again, skip
        if current in closed:
            continue

        closed.append(current)

        print("\nState being examined:")
        print(current)
        print(f"Heuristic value h= {h_value}")  

        for child in find_children(current):
            if child not in closed:
                path_new= path+ [copy.deepcopy(child)]
                h_child= heuristic(child)
                #Adding child to priority queue
                heapq.heappush(queue, (h_child, path_new))
        
        #We check here for the target state and not before children creation
        #because in order to print the solution path, we need the path_new variable
        if is_goal_state(current):
            print("\n_GOAL_FOUND_")
            print(current)
            print(f"\nSolution path ({len(path_new)-1} steps):")
            for step, s in enumerate(path_new):
                print(f"Step {step}: Position {s[0]}, Load {s[-1]}, Garbage {sum(s[1:9])}")
            print(f"\nTotal states examined: {states_examined}")
            print("Method: Heuristic (Best-First Search)\n")

            return path_new


    print("_NO_SOLUTION_FOUND_")
    print("Method: Heuristic (Best-First Search)\n")