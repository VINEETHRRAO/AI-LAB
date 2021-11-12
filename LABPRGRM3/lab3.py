def dfs(src,target,limit,visited_states):
   
    if src == target:
        print(src)
        print("FOUND!!")
        return True
    if limit <= 0:
        print(src)
        return False
   
    visited_states.append(src)
    moves = possible_moves(src,visited_states)   
    for move in moves:
        if dfs(move, target, limit-1, visited_states):
            
            return True
    return False

def possible_moves(state,visited_states): 
    b = state.index(-1)  
    d = []
    if b not in [0,1,2]: 
        d += 'u'
    if b not in [6,7,8]:
        d += 'd'
    if b not in [2,5,8]: 
        d += 'r'
    if b not in [0,3,6]: 
        d += 'l'
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state,move,b))
    return [move for move in pos_moves if move not in visited_states]
def gen(state, move, blank): 
    temp = state.copy()                              
    if move == 'u':
        temp[blank-3], temp[blank] = temp[blank], temp[blank-3]
    if move == 'd':
        temp[blank+3], temp[blank] = temp[blank], temp[blank+3]
    if move == 'r':
        temp[blank+1], temp[blank] = temp[blank], temp[blank+1]
    if move == 'l':
        temp[blank-1], temp[blank] = temp[blank], temp[blank-1]
    return temp
def iddfs(src,target,depth):
    for i in range(depth):
        visited_states = []
        if dfs(src,target,i+1,visited_states):
            return True
    return False

src = [] 
target=[]    
print("Enter source array ")
for i in range(0, 9):
    ele1 = int(input())
 
    src.append(ele1)

print("Enter target array ")
for i in range(0, 9):
    ele2 = int(input())
 
    target.append(ele2)



depthmax = int(input("ENTER THE DEPTH: "))

for i in range(1, depthmax):
    val = iddfs(src,target,i)
    print(i, val)
    if val == True:
        break