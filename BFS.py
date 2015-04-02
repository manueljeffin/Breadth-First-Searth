queue=[]
bad_guys=[]
print'Enter the number of vertices'
number=input()
Matrix = [[0 for x in range(number+1)] for x in range(number+1)] 
print 'Enter the adjacecy matrix'
for i in range(1,number+1):
    for j in range(1,number+1):
        Matrix[i][j]=input()
print 'enter the source vertex'
queue.append(input())

while(len(bad_guys)!=number):
    
    for i in range(1,number+1):
        if(Matrix[queue[0]][i]==1 and i not in bad_guys and i not in queue):
        
            queue.append(i)
            
    bad_guys.append(queue.pop(0))
    
print bad_guys





    
        







