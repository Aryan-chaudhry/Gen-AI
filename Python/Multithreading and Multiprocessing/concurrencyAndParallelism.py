# concurrency : means doing multiple task at a once --> (Threading/thread and asyncio)
# parallelism : means doinf multiple task simultaneoulsy --> (multiprocessing/Process/ concurrent.future.ProcessPoolExecutor)

# concurrency threading (mutithreading)

import threading
import time

def takeOrders():
    for i in range(1,4):
        print(f"Taking order for #{i} \n")
        time.sleep(1)

def receiveOrder():
    for i in range(1,4):
        print(f"Receiving order for #{i} \n")
        time.sleep(3)

# creating threads
takeOrderThread = threading.Thread(target=takeOrders)
receiveOrderThread = threading.Thread(target=receiveOrder)

# start the thread
takeOrderThread.start()
receiveOrderThread.start()

# wait for both thread to finish
takeOrderThread.join()
receiveOrderThread.join()

print(f"All orders dispatched and received")

