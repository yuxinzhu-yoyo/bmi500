### Commented by Yuxin Zhu, for BMI 500

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
###YZHU: functional and correct. The logic is straightforward and easy to understand. There's no unnecessary complexity. 
###Consider adding a unit test to validate that the output is as expected for a range of numbers.

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

###YZHU: The code correctly generates a 3x3 matrix of random integers and finds the max and min values with their positions. The code is concise and uses NumPy effectively. There’s no unnecessary complexity.
###The variable a could be more descriptive (e.g., matrix).The comment could be more detailed .

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

###YZHU:The logic for checking if a number is in the Fibonacci sequence is correct. 
###The logic is simple and efficient for the task. However, you could combine check_fibonacci and is_fibonacci into one function for simplicity.
###A comment could be added to explain the purpose of each function, particularly explaining the mathematical approach used.
###Consider adding unit tests to check a variety of numbers, both in and out of the Fibonacci sequence. Also, it might be better to return True or False from check_fibonacci instead of printing the result.

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

###YZHU:The function copies files from a source directory to a destination directory based on a prefix, which seems appropriate for the task.
###The code could be simplified by handling arguments more gracefully, and possibly using argparse for better argument parsing.
###The function and variable names are clear, but args could be improved to something more specific (e.g., command_line_args).
###The comments are minimal. A better comment could describe the purpose of the function and its parameters in more detail.
###Catching a general exception is not recommended because it can hide bugs. Consider catching specific exceptions (e.g., FileNotFoundError, PermissionError).


            
