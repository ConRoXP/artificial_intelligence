import copy
from operators import is_goal_state
from DFS_BFS import expand_front, extend_queue

#Εύρεση Λύσης
def find_solution(front, queue, closed, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND_')
        print(f"Μέθοδος: {method}\n")
    
    #Αν η κατάσταση έχει ξαναεξεταστεί, παραλείπεται
    elif front[0] in closed:
        new_front= copy.deepcopy(front)
        new_front.pop(0)
        new_queue= copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, method)
    
    #Μορφοποίηση εξόδου για να τυπώνουμε το μονοπάτι της λύσης
    #και άλλες πληροφορίες με ευανάγνωστο τρόπο
    elif is_goal_state(front[0]):
        print("\n_GOAL_FOUND_")
        print(front[0])
        print(f"\nΜονοπάτι λύσης ({len(queue[0])-1} βήματα):")
        for step, s in enumerate(queue[0]):
            print(f"Βήμα {step}: Θέση {s[0]}, Φορτίο {s[-1]}, Σκουπίδια {sum(s[1:9])}")
        print(f"\nΣυνολικές καταστάσεις που εξετάστηκαν: {len(closed)}")
        print(f"Μέθοδος: {method}\n")
        
    else:
        closed.append(front[0])
        print("\nΚατάσταση που εξετάζεται:") # <-
        print(front[0])
        front_copy= copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy= copy.deepcopy(queue)
        queue_children= extend_queue(queue_copy, method)
        closed_copy= copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, method)