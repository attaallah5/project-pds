import multiprocessing
import pandas as pd 
import numpy as np  
import time
import requests


ds = pd.read_csv("mobile_usage_behavioral_analysis.csv")

def count_ages(ds, queue):
    ages = []
    for i in range(10):
        print(f"Age[{i+1}]: {ds['Age'][i]}")
        ages.append(ds['Age'][i])
        time.sleep(0.3)
    queue.put(ages)

if __name__ == "__main__":

    queue = multiprocessing.Queue()

    worker = multiprocessing.Process(target=count_ages, args=(ds, queue,))

    worker.start()
    worker.join()
    ages_result = queue.get()
    print("The first 10 ages:", ages_result)
    print("Done!")
    
# def count_numbers(ds):
#     for i in range(0,10):
#         print(ds['Age'][i])
#         time.sleep(0.3)
# if __name__ == "__main__":
    
#     worker = multiprocessing.Process(target=count_numbers,args=(ds,))
#     worker.start()
#     print("the first 10 ages: ")
#     worker.join()
#     print("Done!") # i cant use two processes