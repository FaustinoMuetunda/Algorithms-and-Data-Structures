# importing "heapq" to implement heap queue
import heapq
# using heapify() to convert list into heap
def hearpsort(h):
    heap = [] #definir 0 array e percorrer
    for value in h:
        heapq.heappush(heap, value)
    return [heapq.heappop(heap) for i in range(len(heap))]

print(hearpsort([10,15,48,50,13,2,1,0,8,4,5]))


















#https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-data-structure-exercise-22.php