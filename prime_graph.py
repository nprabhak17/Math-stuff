import math
import copy 
from collections import defaultdict
def create_list_of_primes(n):
    primes = []
    for num in range(3,n,2):
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            primes.append(num)
    return primes

def primeFactors(n): 
    if(n == 1):
        return {1}
    prime_factors = set()
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            prime_factors.add(int(i))
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        prime_factors.add(int(n))
    return prime_factors

ans = [" "]
class Graph: 
   
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    # A function used by DFS 
    def DFSUtil(self,v,visited): 
        # Mark the current node as visited and print it 
        visited[v]= True
        ans.append(v)
        #print(v), 
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.DFSUtil(i,visited) 
  
  
    def fillOrder(self,v,visited, stack): 
        # Mark the current node as visited  
        visited[v]= True
        #Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
        stack = stack.append(v) 
      
  
    # Function that returns reverse (or transpose) of this graph 
    def getTranspose(self): 
        g = Graph(self.V) 
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph: 
            for j in self.graph[i]: 
                g.addEdge(j,i) 
        return g 
    
    def printSCCs(self): 
          
        stack = [] 
        # Mark all the vertices as not visited (For first DFS) 
        visited =[False]*(self.V) 
        # Fill vertices in stack according to their finishing 
        # times 
        for i in range(0,self.V): 
            if visited[i]==False: 
                self.fillOrder(i, visited, stack) 
  
        # Create a reversed graph 
        gr = self.getTranspose() 
           
         # Mark all the vertices as not visited (For second DFS) 
        visited =[False]*(self.V) 
  
         # Now process all vertices in order defined by Stack 
        while stack: 
            i = stack.pop() 
            if visited[i]==False: 
                gr.DFSUtil(i, visited) 
                ans.append(" ")
                #print("") 

def create_graph(n):
    g = Graph(n)
    primes = create_list_of_primes(n)
    prime_adjacency_list = {}
    a = 1
    edges = 0
    for i in create_list_of_primes(n):
        for nums in primeFactors(n-i):
            print(a,i,nums)
            edges += 1
            a += 1
            g.addEdge(i,nums)
        prime_adjacency_list[i] = primeFactors(n-i)
    #print(len(primes),edges)
    return g

print("_________________________")
g = create_graph(1000)

g.printSCCs() 
#print(ans)
ans_string = ""
for i in range(0,len(ans)):
    ans_string += str(ans[i])

#print(ans_string)