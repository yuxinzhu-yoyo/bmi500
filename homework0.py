import os
import sys

# task 1
for i in range(0,101):
    if i % 3 == 0 and i % 5 == 0:
        print('ab')
    elif i % 3 == 0:
        print('a')
    elif i % 5 == 0:
        print('b')
    else:
        print(i)


# task 2
import numpy as np

# create a 3x3 2d array with random int between 1 and 10 inclusive
a = np.random.randint(1, 11, (3, 3))

# find and print the max and min value with pos
max_val = np.max(a)
min_val = np.min(a)
max_pos = np.where(a == max_val)
min_pos = np.where(a == min_val)
print(f'Max value: {max_val} at position {max_pos}')
print(f'Min value: {min_val} at position {min_pos}')

# task 3
# Write a code that checks whether a given number x is part of the Fibonacci sequence.
# The program should output True if x is in the sequence and False otherwise.

def is_fibonacci(x):
    a, b = 0, 1
    while a < x:
        a, b = b, a + b
    return a == x

def check_fibonacci(x):
    if is_fibonacci(x):
        print(True)
    else:
        print(False)

# task 4
import shutil
import glob
def copy_file_task(args):
    try:
        src_dir = args[1]
        dest_dir = args[2]
        prefix = args[3]
        # copy all files from src_dir to dest_dir with prefix
        # get all files in src_dir
        files = sorted(glob.glob(os.path.join(src_dir, '*')))
        for file in files:
            # get the filename
            filename = os.path.basename(file)
            if filename.startswith(prefix):
                shutil.copy(file, os.path.join(dest_dir, filename))
    except Exception as e:
        print(f'Error: {e}')


            