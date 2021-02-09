import multiprocessing as mp

#init objects
pool = mp.Pool(4)
jobs = []

def process():
    print("In process")

#create jobs
with open("../data_set/input.txt") as f:
    for line in f:
        jobs.append( pool.apply_async(process,(line)) )

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()
