import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: started", name)
    time.sleep(2)
    logging.info("Thread %s: ended", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # Create multiple threads
    threads = []
    for index in range(5):
        logging.info("Thread created")
        my_thread = threading.Thread(target=thread_function, args=(1,))
        threads.append(my_thread)

        # Start thread
        my_thread.start()

    # use .join to wait for threads to finsih
    for index, thread in enumerate(threads):
        thread.join()
        logging.info("thread %d ended", index)

    logging.info("Main, wait for the thread to finish")



    # # Create thread (but not start)
    # logging.info("Main, before thread created")
    # my_thread = threading.Thread(target=thread_function, args=(9,))
    #
    # # Start thread
    # logging.info("Main, before thread started")
    # my_thread.start()
    #
    # logging.info("Main, wait for the thread to finish")
    # logging.info("Ending thread and program")