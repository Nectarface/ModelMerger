
import multiprocessing
from scripts.merge_logic import merge_models

def run_parallel_merges(task_list):
    pool = multiprocessing.Pool(processes=min(len(task_list), multiprocessing.cpu_count()))
    results = pool.starmap(merge_models, task_list)
    pool.close()
    pool.join()
    return results
