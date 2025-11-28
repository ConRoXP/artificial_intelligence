from find_sol import find_solution
from DFS_BFS import make_front, make_queue
from heuristic_search import best_first_search

def main():

    #[θέση σκούπας, σκουπίδια Ν πλακιδίου (1-8), θέση βάσης, φορτίο σκούπας]
    initial_state = [3, 2, 3, 0, 0, 2, 0, 1, 2, 3, 0]
    #goal = [3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0]
    #Ο καθορισμός της τελικής κατάστασης δεν είναι απαραίτητος

    #initial_state= [4, 1, 0, 2, 0, 3, 3, 0, 1, 4, 0]
    #initial_state= [1, 0, 3, 0, 1, 1, 0, 2, 3, 1, 0]
    #initial_state= [7, 1, 3, 0, 1, 1, 2, 0, 2, 7, 0]
    #initial_state= [5, 1, 1, 2, 1, 0, 2, 0, 3, 5, 0]

    while True:
        print("\nΕπιλέξτε μέθοδο αναζήτησης ή 0 για έξοδο.")
        print("1 - DFS\n2 - BFS\n3 - Ευριστική (Best-First)")
        search= input("Επιλογή: ")

        if search== '1':
            method= 'DFS'
            print('\n____BEGIN__SEARCHING____')
            find_solution(make_front(initial_state), make_queue(initial_state), [], method)
        elif search== '2':
            method= 'BFS'
            print('\n____BEGIN__SEARCHING____')
            find_solution(make_front(initial_state), make_queue(initial_state), [], method)
        elif search== '3':
            print('\n____BEGIN__SEARCHING____')
            best_first_search(initial_state)
        elif search== '0':
            break
        else:
            print("Μη έγκυρη επιλογή")
    

if __name__ == "__main__":
    main()