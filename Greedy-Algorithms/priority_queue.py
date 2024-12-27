import heapq

# Priority Queue Implementation
class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, priority, item):
        heapq.heappush(self.heap, (priority, item))
    
    def dequeue(self):
        return heapq.heappop(self.heap)[1] if self.heap else None
    
    def is_empty(self):
        return len(self.heap) == 0

# Main function to demonstrate Priority Queue
def priority_queue_demo():
    tasks = PriorityQueue()
    tasks.enqueue(2, "Wash dishes")
    tasks.enqueue(5, "Finish project report")
    tasks.enqueue(3, "Call plumber")
    tasks.enqueue(1, "Pay bills")

    print("Processing tasks based on priority:")
    while not tasks.is_empty():
        task = tasks.dequeue()
        print(f"Processing task: {task}")

if __name__ == "__main__":
    priority_queue_demo()