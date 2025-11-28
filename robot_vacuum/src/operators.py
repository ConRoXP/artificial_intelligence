import copy

def move_left(state):
    #The vacuum moves left only if it is not going out of bounds
    #If it's fully loaded, movement is blocked because it goes straight to base to unload
    if state[-1]< 3 and state[0]> 1:
        state[0]= state[0]-1
        #Checking for garbage on new tile
        if state[state[0]]> 0:
            #If garbage greater than capacity
            if state[state[0]]> 3-state[-1]:
                #vacuum gathers enough to fill up
                state[state[0]]= state[state[0]] - (3-state[-1])
                state[-1]= 3
            else:
                #else it gathers all
                state[-1]= state[-1] + state[state[0]]
                state[state[0]]= 0
    #Returns new state
    return state


def move_right(state):
    #Will move right only if it is not going out of bounds
    #and if it's not full
    if state[-1]< 3 and state[0]< 8:
        state[0]= state[0]+1
        #Same as above
        if state[state[0]]> 0:
            if state[state[0]]> 3- state[-1]:
                state[state[0]]-= (3- state[-1])
                state[-1]= 3
            else:
                state[-1]= state[-1] + state[state[0]]
                state[state[0]]= 0
    return state


#Emptying load when full by teleporting to base
def full(state):
    load= state[-1]
    tiles_garbage= sum(state[1:9])

    if load== 3 or tiles_garbage== 0:
        state[0]= state[-2]   #vacuum pos= base pos
        state[-1]= 0      #unloading
        return state
    
    else: return None


def is_goal_state(state):
    #The goal state is defined by:

    #1. No more garbage available on tiles
    clean= all(s== 0 for s in state[1:9])

    #2. Vacuum empty and on base
    back_to_base= (state[0]== state[-2] and state[-1]== 0)

    return clean and back_to_base


def find_children(state):
    #If goal state, no children created
    if is_goal_state(state):
        return []

    children=[]

    #Applying move_left()
    left_state= copy.deepcopy(state)
    left_child= move_left(left_state)

    if left_child!= None:
        children.append(left_child)

    #Applying move_right()
    right_state= copy.deepcopy(state)
    right_child= move_right(right_state)

    if right_child!= None:
        children.append(right_child)

    #Applying full()
    empty_state= copy.deepcopy(state)
    empty_child= full(empty_state)

    if empty_child!= None:
        children.append(empty_child)

    return children