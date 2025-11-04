import copy
from operators import is_goal_state
from DFS_BFS import expand_front, extend_queue

def find_solution(front, queue, closed, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND_')
        print(f"Method: {method}\n")
    
    #If state has been examined again, skip
    elif front[0] in closed:
        new_front= copy.deepcopy(front)
        new_front.pop(0)
        new_queue= copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, method)
    
    elif is_goal_state(front[0]):
        print("\n_GOAL_FOUND_")
        print(front[0])
        print(f"\nSolution path ({len(queue[0])-1} steps):")
        for step, s in enumerate(queue[0]):
            print(f"Step {step}: Pos {s[0]}, Load {s[-1]}, Garbage {sum(s[1:9])}")
        print(f"\nTotal states examined: {len(closed)}")
        print(f"Method: {method}\n")
        
    else:
        closed.append(front[0])
        print("\nState being examined:") # <-
        print(front[0])
        front_copy= copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy= copy.deepcopy(queue)
        queue_children= extend_queue(queue_copy, method)
        closed_copy= copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, method)