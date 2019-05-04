# this will import tqdm and enable progress bar for pandas operations
# source: https://stackoverflow.com/questions/18603270/progress-indicator-during-pandas-operations-python
from tqdm import tqdm
tqdm.pandas()

import time
def start_timer():
    return time.time()
    
def stop_timer(timer):
    return time.time() - timer
    
def elapsed_time(msg, elapsed):
    return msg + ": " + '{0:.3f}'.format(elapsed*1000.0) + " ms"
    
def elapsed_time_ext(msg, elapsed, item_desc, item_count):
    # throughput is measured in item per second
    throughput = item_count / elapsed
    # processing time is measured in ms per item (more useful)
    proc_per_item = elapsed * 1000.0 / item_count
    return msg + ": " + '{0:.3f}'.format(elapsed*1000.0) + " ms for " + str(item_count) + " " + item_desc + "s (" + '{0:.3f}'.format(throughput) + " " + item_desc + "/s, " + '{0:.3f}'.format(proc_per_item) + " ms/" + item_desc + ")"
