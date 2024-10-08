import threading
import time
import random
class GroceryStore:
def __init__(self, num_counters):
# Semaphore to represent each checkout counter
self.counters = [threading.Semaphore(1) for _ in

range(num_counters)]
def checkout(self, customer_id, counter_id):

print(f"Customer {customer_id} is waiting for counter {counter_id

+ 1}") # Display counter as 1-indexed
with self.counters[counter_id]:
print(f"Customer {customer_id} is being served at counter

{counter_id + 1}") # Display counter as 1-indexed

time.sleep(random.uniform(0.5, 1.5)) # Simulate checkout time
print(f"Customer {customer_id} finished checking out at counter
{counter_id + 1}") # Display counter as 1-indexed
class Customer(threading.Thread):
def __init__(self, customer_id, store):
super().__init__()
self.customer_id = customer_id
self.store = store
def run(self):
# Simulate arrival at store and preparation for checkout
time.sleep(random.uniform(0.5, 2.0)) # Time taken to shop
# Try to checkout at an available counter
counter_id = random.randint(0, len(self.store.counters) - 1)
self.store.checkout(self.customer_id, counter_id)

if __name__ == "__main__":
num_counters = 3 # 3 checkout counters available
store = GroceryStore(num_counters)
# Create customers (threads) starting from 1
customers = [Customer(i + 1, store) for i in range(5)] # 5 customers
in the store (IDs 1 to 5)
# Start all customers (threads)
for customer in customers:
customer.start()
# Let the simulation run for a while to see interactions
for customer in customers:
customer.join() # Wait for all customers to finish
# To Terminate the program after the simulation
print("Simulation ended")

