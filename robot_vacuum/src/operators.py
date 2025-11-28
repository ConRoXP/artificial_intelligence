import copy

#Τελεστές Μετάβασης
def move_left(state):
    #Η σκούπα θα μετακινηθεί μόνο αν δεν βρίσκεται στο αριστερό άκρο
    #Αν είναι γεμάτη μπλοκάρεται η μετακίνηση της για να τηλεμεταφερθεί στην βάση
    if state[-1]< 3 and state[0]> 1:
        state[0]= state[0]-1
        #Έλεγχος ύπαρξης σκουπιδιών στο νέο πλακάκι
        if state[state[0]]> 0:
            #Αν τα σκουπίδια ξεπερνούν την διαθέσιμη χωρητικότητα της σκούπας
            if state[state[0]]> 3-state[-1]:
                #μαζεύει όσα χωράνε για να γεμίσει
                state[state[0]]= state[state[0]] - (3-state[-1])
                state[-1]= 3
            else:
                #αλλιώς τα μαζεύει όλα
                state[-1]= state[-1] + state[state[0]]
                state[state[0]]= 0
    #Επιστρέφεται η νέα κατάσταση
    return state


def move_right(state):
    #Θα μετακινηθεί μόνο αν δεν βρίσκεται στο δεξί άκρο
    #και άν δεν είναι γεμάτη
    if state[-1]< 3 and state[0]< 8:
        state[0]= state[0]+1
        #Υπόλοιπα βήματα ίδια με παραπάνω
        if state[state[0]]> 0:
            if state[state[0]]> 3- state[-1]:
                state[state[0]]-= (3- state[-1])
                state[-1]= 3
            else:
                state[-1]= state[-1] + state[state[0]]
                state[state[0]]= 0
    return state


#Άδειασμα σκουπιδιών μόνο όταν γεμίζει, με τηλεμεταφορά στην βάση
def full(state):
    load= state[-1]  #φορτίο σκούπας
    tiles_garbage= sum(state[1:9])  #συνολικά σκουπίδια στα πλακάκια (1–8)

    if load== 3 or tiles_garbage== 0:
        #Τηλεμεταφορά στη βάση
        state[0]= state[-2]   #θέση σκούπας= θέση βάσης
        state[-1]= 0      #άδειασμα φορτίου
        return state

    #Σε κάθε άλλη περίπτωση δεν αδειάζει
    else: return None


#Έλεγχος τελικής κατάστασης
def is_goal_state(state):
    #Για να επιλυθεί το πρόβλημα θα πρέπει:

    #1. Όλα τα πλακάκια 1–8 να έχουν 0 σκουπίδια
    clean= all(s== 0 for s in state[1:9])

    #2. Η σκούπα να είναι άδεια και στην βάση της
    back_to_base= (state[0]== state[-2] and state[-1]== 0)

    return clean and back_to_base


#Εύρεση Απογόνων
def find_children(state):
    #Αν η κατάσταση είναι η τελική, δεν δημιουργούνται απόγονοι
    if is_goal_state(state):
        return []

    children=[]

    #Εφαρμογή move_left()
    left_state= copy.deepcopy(state)
    left_child= move_left(left_state)

    if left_child!= None:
        children.append(left_child)

    #Εφαρμογή move_right()
    right_state= copy.deepcopy(state)
    right_child= move_right(right_state)

    if right_child!= None:
        children.append(right_child)

    #Εφαρμογή full()
    empty_state= copy.deepcopy(state)
    empty_child= full(empty_state)

    if empty_child!= None:
        children.append(empty_child)

    return children