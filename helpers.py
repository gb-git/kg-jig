# --------------------------------------------------------------------------------------
# Timing
# --------------------------------------------------------------------------------------

# Operating system functions
import os
# Time measurement and processing time
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

# --------------------------------------------------------------------------------------
# Import Needed Resources
# --------------------------------------------------------------------------------------

print ("Import libraries...")
timer = start_timer()
# this will import tqdm and enable progress bar for pandas operations
# source: https://stackoverflow.com/questions/18603270/progress-indicator-during-pandas-operations-python
# Allows progress bars to be displayed when loading dataframes in Pandas
from tqdm import tqdm
tqdm.pandas()
# Random generators
import random
# Data frames and data manipulation
import pandas as pd
# Numerical library
import numpy as np
# TQDM: progress bar (https://github.com/tqdm/tqdm)
import tqdm
# Plotting library
import matplotlib.pyplot as plt
# Statistical data visualization
import seaborn as sns
# Natural language toolkit
import nltk
import spacy
# Various operations on collections
import operator
print (elapsed_time("Loaded libraries", stop_timer(timer)))

# --------------------------------------------------------------------------------------
# Initialization of random seeds to ensure reproducibility
# --------------------------------------------------------------------------------------

def set_seed(seed=0):
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

# --------------------------------------------------------------------------------------	
# Set of functions to load the data properly
# --------------------------------------------------------------------------------------

def load_data(file_path, title=""):
	timer = start_timer()
	train_df = pd.read_csv(file_path)
	print(elapsed_time_ext(title + " load time", stop_timer(timer), "record", len(train_df)))
	return train_df
