import threading

# Example function to process an order
def process_order(order_id, lock):
    # Implement processing logic here
    with lock:
        print(f"Processing order: {order_id}")
        # Simulate processing without sleep
        import random
        processing_time = random.uniform(0.1, 0.5)  # Simulate quick processing
        import time
        time.sleep(processing_time)
        print(f"Order processed: {order_id}")

# Example of handling multiple orders using threads with a lock
def handle_orders(order_list):
    lock = threading.Lock()
    threads = []
    for order_id in order_list:
        thread = threading.Thread(target=process_order, args=(order_id, lock))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Example usage
if __name__ == "__main__":
    orders = [1, 2, 3, 2, 4, 1]  # Example list of orders (with potential duplicates)
    
    handle_orders(orders)
    def dfdf():
       cursor , connd = connect_co()
       thecountforeb.clear()
       exel.code(int(float(use)))
       thetempss.append(int(float(use)))
       thecountforeb.append(testmet.increment_count(cursor , connd))
      