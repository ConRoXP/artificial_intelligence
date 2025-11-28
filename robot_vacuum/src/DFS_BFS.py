import copy
from operators import find_children

#Front
def make_front(state):
    return [state]

def expand_front(front, method):  
    if method== 'DFS':
        if front:
            #Printing front
            print("\nFront:")
            for i, state in enumerate(front):
                print(f"  {i+1}: {state}")
            ##
            node= front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)

    elif method== 'BFS':
        if front:
            #Printing front
            print("\nFront:")
            for i, state in enumerate(front):
                print(f"  {i+1}: {state}")
            ##
            node= front.pop(0)
            for child in find_children(node):
                front.append(child)

    return front

#Queue
def make_queue(state):
    return [[state]]

def extend_queue(queue, method):

    if method== 'DFS':
        #Printing queue
        print("\nPath queue:")
        for i, path in enumerate(queue):
            print(f"  {i+1}: {path}\n")
        print("=======================================")
        ##
        node=queue.pop(0)
        queue_copy= copy.deepcopy(queue)
        children= find_children(node[-1])
        for child in children:
            path= copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    
    elif method== 'BFS':
        #Printing queue
        print("\nPath queue:")
        for i, path in enumerate(queue):
                print(f"  {i+1}: {path}\n")
        print("=======================================")
        ##
        node= queue.pop(0)
        queue_copy= copy.deepcopy(queue)
        children= find_children(node[-1])
        for child in children:
            path= copy.deepcopy(node)
            path.append(child)
            queue_copy.append(path)

    return queue_copy