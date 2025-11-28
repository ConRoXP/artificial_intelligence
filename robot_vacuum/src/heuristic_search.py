import copy
from operators import is_goal_state, find_children

#Heuristic value creation
def heuristic(state):
    #Heauristic value= garbage sum
    return sum(state[1:9])

#Heuristic search - Best-First
def best_first_search(initial_state):
    queue= []
    #Adding initial state to queue
    #along with the heuristic value
    queue.append((heuristic(initial_state), [initial_state]))
    closed= []
    states_examined= 0

    while queue:
        #Searching for the state with the lowest heuristic value
        #(highest priority)
        min_index= 0
        min_h= queue[0][0]
        for i in range(1, len(queue)):
            if queue[i][0]< min_h:
                min_h= queue[i][0]
                min_index= i

        #Popping state with the highest priority
        #h_value -> heuristic value
        #path -> path to latest/ current state
        h_value, path= queue.pop(min_index)
        current= path[-1]   #path[-1] -> current state

        path_new= path

        if current in closed:
            continue

        closed.append(current)

        print("\nState being examined:")
        print(current)
        print(f"Heuristic value h= {h_value}") 
        states_examined+= 1 

        for child in find_children(current):
            if child not in closed:
                path_new= path+ [copy.deepcopy(child)]
                h_child= heuristic(child)
                #Adding child to queue
                queue.append((h_child, path_new))
        
        #Path_new is used to print the entire solution path
        if is_goal_state(current):
            print("\n_GOAL_FOUND_")
            print(current)
            print(f"\nSolution path ({len(path_new)-1} steps):")
            for step, s in enumerate(path_new):
                print(f"Step {step}: Pos {s[0]}, Load {s[-1]}, Garbage {sum(s[1:9])}")
            print(f"\nTotal states examined: {states_examined}")
            print("Method: Heuristic (Best-First Search)\n")

            return path_new


    print("_NO_SOLUTION_FOUND_")
    print("Method: Heuristic (Best-First Search)\n")