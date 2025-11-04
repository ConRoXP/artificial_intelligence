import copy

def move_left(state):
    #The vacuum will only move if it is not on the left edge
    if state[0]>1:
        state[0]=state[0]-1
        #Checking for debris on new tile
        if state[state[0]]> 0:
            #If the debris exceeds the available capacity of the trash can
            if state[state[0]]> 3-state[-1]:
                #collect as much as you can hold to fill up
                state[state[0]]= state[state[0]] - (3-state[-1])
                state[-1]= 3
            else:
                #else collect all
                state[-1]= state[-1] + state[state[0]]
                state[state[0]]= 0
    #Return new state
    return state


def move_right(state):
    #Wwill only move if it is not on the right edge
    if state[0]< 8:
        state[0]+= 1
        #Same as above
        if state[state[0]]> 0:
            if state[state[0]]> 3- state[-1]:
                state[state[0]]-= (3- state[-1])
                state[-1]= 3
            else:
                state[-1]+= state[state[0]]
                state[state[0]]= 0
    return state


def empty_robot(state):
    #if the vacuum cleaner is on its base and has a load
    if state[0]== state[-2] and state[-1]> 0:
        state[-1]= 0
    return state


#Final state check
def is_goal_state(state):
    #To finish:

    #1. All tiles 1–8 should have 0 debris.
    clean= all(s== 0 for s in state[1:9])

    #2. The vacuum must be empty and on its base.
    back_to_base= (state[0]== state[-2] and state[-1]== 0)

    return clean and back_to_base


def find_children(state):
    #If final state, no children created.
    if is_goal_state(state):
        return []

    children=[]

    #move_left()
    left_state= copy.deepcopy(state)
    left_child= move_left(left_state)

    if left_child!= None:
        children.append(left_child)

    #move_right()
    right_state= copy.deepcopy(state)
    right_child= move_right(right_state)

    if right_child!= None:
        children.append(right_child)

    #empty_robot()
    empty_state= copy.deepcopy(state)
    empty_child= empty_robot(empty_state)

    if empty_child!= None:
        children.append(empty_child)

    return children