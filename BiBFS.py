from methods import *
#Bi-Directional BFS

def BiBFS(maze):
#initialized state is set to false
#i,j-->row,column from start m,n-->row,column from end
    maze_final=np.copy(maze)
    solved=False
    i,j=0,0
    m,n=len(maze)-1,len(maze[0])-1
    prev={}
    prev2={}
    
#initialize fringe for starting point and fringe from ending point
    fringeStart=queue.Queue()
    fringeStart.put([i,j])
    fringeEnd=queue.Queue()
    fringeEnd.put([m,n])
    
    #run loop until start and end meet or no solution
    while solved==False:
        #if maze is still unsolved and there are no more children left in fringe, maze is unsolvable
        if (queue.Queue.qsize(fringeStart)==0 or queue.Queue.qsize(fringeEnd)==0):
            #update state of maze, display result, then break loop
            update(maze,i,j)
            update(maze,m,n)
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)
            print("UNSOLVABLE")
            break
            
        #gets current node and updates i,j and m,n
        currentStart=fringeStart.get()
        currentEnd=fringeEnd.get()
        i,j=currentStart[0],currentStart[1]
        m,n=currentEnd[0],currentEnd[1]
        
        #check if start and end meet in middle,display result, then break loop
        if (i+1,j) in prev2:
            m, n = i+1, j
            solved = True
            
        if (i,j+1) in prev2:
            m, n = i, j+1
            solved = True
            
        if (i-1,j) in prev2:
            m, n = i-1, j
            solved = True
            
        if (i,j-1) in prev2:
            m,n = i, j-1
            solved = True
        
        if solved == True:
            update(maze,i,j)
            update(maze,m,n)
            plt.imshow(maze, cmap=plt.cm.binary)
            plt.pause(0.05)
            print("SOLVED")

            update(maze_final,i,j)
            update(maze_final,m,n)
            plt.imshow(maze_final, cmap=plt.cm.binary)
            plt.pause(0.05)

            while True:
                if i==0 and j==0 and m==len(maze)-1 and n==len(maze[0])-1:
                    break
                    
                print("i =",i)
                print("j =",j)
                print("m =",m)
                print("n =",n)
                if (i,j) == (0,0):
                    y=prev2[(m,n)]
                    m,n=y[0],y[1]
                    update(maze_final,m,n)
                    plt.imshow(maze_final, cmap=plt.cm.binary)
                    plt.pause(0.05)
                elif (m,n) == (len(maze)-1, len(maze[0])-1):
                    x=prev[(i,j)]
                    i,j=x[0],x[1]
                    update(maze_final,i,j)
                    update(maze_final,m,n)
                    plt.imshow(maze_final, cmap=plt.cm.binary)
                    plt.pause(0.05)
                    
                else:
                    x=prev[(i,j)]
                    y=prev2[(m,n)]
                    i,j=x[0],x[1]
                    m,n=y[0],y[1]
                    update(maze_final,i,j)
                    update(maze_final,m,n)
                    plt.imshow(maze_final, cmap=plt.cm.binary)
                    plt.pause(0.05)

            update(maze_final,0,0)
            update(maze_final,len(maze)-1,len(maze[0])-1)
            plt.imshow(maze_final, cmap=plt.cm.binary)
            plt.pause(0.05)

            break
            
        #check down position of i,j
        if i + 1 >= len(maze):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i + 1][j] == 1 or maze[i + 1][j] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i + 1, j] in fringeStart.queue:
                    pass
                else:
                    prev[(i + 1, j)] = (i, j)
                    fringeStart.put([i + 1, j])
                    
        #check up position of m,n
        if m - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m - 1][n] == 1 or maze[m - 1][n] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m - 1, n] in fringeEnd.queue:
                    pass
                else:
                    prev2[(m - 1, n)] = (m, n)
                    fringeEnd.put([m - 1, n])
                    
        #check right position of i,j
        if j + 1 >= len(maze[i]):
            pass
        else:
            #is the next position occupied or iously visited?
            if maze[i][j + 1] == 1 or maze[i][j + 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j + 1] in fringeStart.queue:
                    pass
                else:
                    prev[(i, j + 1)] = (i, j)
                    fringeStart.put([i, j + 1])
                    
        #check left position of m,n
        if n - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m][n - 1] == 1 or maze[m][n - 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m, n - 1] in fringeEnd.queue:
                    pass
                else:
                    prev2[(m, n - 1)] = (m, n)
                    fringeEnd.put([m, n - 1])
                    
        #check up position of i,j
        if i - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i - 1][j] == 1 or maze[i - 1][j] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i - 1, j] in fringeStart.queue:
                    pass
                else:
                    prev[(i - 1, j)] = (i, j)
                    fringeStart.put([i - 1, j])
                    
        #check down position of m,n
        if m + 1 >= len(maze):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m + 1][n] == 1 or maze[m + 1][n] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m + 1, n] in fringeEnd.queue:
                    pass
                else:
                    prev2[(m + 1, n)] = (m, n)
                    fringeEnd.put([m + 1, n])
                    
        #check left position of i,j
        if j - 1 < 0:
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[i][j - 1] == 1 or maze[i][j - 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [i, j - 1] in fringeStart.queue:
                    pass
                else:
                    prev[(i, j - 1)] = (i, j)
                    fringeStart.put([i, j - 1])
                    
        #check right position of m,n
        if n + 1 >= len(maze[m]):
            pass
        else:
            #is the next position occupied or previously visited?
            if maze[m][n + 1] == 1 or maze[m][n + 1] == 0.5:
                pass
            else:
                #add to fringe if valid and is not already in fringe
                if [m, n + 1] in fringeEnd.queue:
                    pass
                else:
                    prev2[(m, n + 1)] = (m, n)
                    fringeEnd.put([m, n + 1])
                    
        #after done checking, update maze and start over
        update(maze, i, j)
        update(maze,m,n)
        plt.imshow(maze, cmap=plt.cm.binary)
        plt.pause(0.05)
    plt.show()
    
BiBFS(grid(10,0.2))
