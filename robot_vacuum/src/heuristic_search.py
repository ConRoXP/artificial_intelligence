import copy
from operators import is_goal_state, find_children

#Δημιουργία ευριστικής τιμής για μία κατάσταση
def heuristic(state):
    #Ευριστική τιμή= άθροισμα σκουπιδιών στον χώρο
    return sum(state[1:9])

#Σώμα ευριστικής αναζήτησης
def best_first_search(initial_state):
    queue= []
    #Προσθήκη της αρχικής κατάστασης στην ουρά
    #μαζί με την ευριστική τιμή
    queue.append((heuristic(initial_state), [initial_state]))
    closed= []
    #Μετρητής καταστάσεων που εξετάστηκαν
    states_examined= 0

    while queue:
        #Βρίσκουμε την κατάσταση με την μικρότερη ευριστική τιμή
        #(μεγαλύτερη προτεραιότητα)
        min_index= 0
        min_h= queue[0][0]
        for i in range(1, len(queue)):
            if queue[i][0]< min_h:
                min_h= queue[i][0]
                min_index= i

        #Εξάγουμε την κατάσταση με την μεγαλύτερη προτεραιότητα
        #Αναθέτουμε την ευριστική τιμή της στην μεταβλητή h_value
        #και την ίδια την κατάσταση (μονοπάτι μέχρι την τρέχουσα) στην path
        h_value, path= queue.pop(min_index)
        current= path[-1]   #path[-1] -> η πιο πρόσφατη κατάσταση (τρέχουσα)

        #στην path_new θα αποθηκεύεται σταδιακά ολόκληρο το μονοπάτι της λύσης
        #για να τυπωθεί στο τέλος
        path_new= path

        #Αν η κατάσταση έχει εξεταστεί ξανά, παραλείπεται
        if current in closed:
            continue

        closed.append(current)

        print("\nΚατάσταση που εξετάζεται:")
        print(current)
        print(f"Ευριστική τιμή h= {h_value}") 
        states_examined+= 1 

        for child in find_children(current):
            if child not in closed:
                path_new= path+ [copy.deepcopy(child)]
                h_child= heuristic(child)
                #Προσθήκη παιδιού στην ουρά
                queue.append((h_child, path_new))
        
        #Ο έλεγχος του στόχου γίνεται εδώ και όχι πριν την δημιουργία απογόνων
        #γιατί για να τυπωθεί το μονοπάτι της λύσης χρειαζόμαστε ολοκληρωμένη την path_new
        if is_goal_state(current):
            print("\n_GOAL_FOUND_")
            print(current)
            print(f"\nΜονοπάτι λύσης ({len(path_new)-1} βήματα):")
            for step, s in enumerate(path_new):
                print(f"Βήμα {step}: Θέση {s[0]}, Φορτίο {s[-1]}, Σκουπίδια {sum(s[1:9])}")
            print(f"\nΣυνολικές καταστάσεις που εξετάστηκαν: {states_examined}")
            print("Μέθοδος: Ευριστική (Best-First Search)\n")

            return path_new


    print("_NO_SOLUTION_FOUND_")
    print("Μέθοδος: Ευριστική (Best-First Search)\n")