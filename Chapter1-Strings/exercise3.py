'''
Exercise 3 - Run Timing
For this exercise:

Write a function (run_timing) that tracks and calculates the average time for a 10 km run.
The function should repeatedly prompt the user to enter the time (in minutes) it took to complete a 10 km run.
The user can stop entering data by pressing Enter without typing a number.
Once the user stops entering data, the function should:
Calculate the average time of all entered run times.
Display the average as a floating-point number and the total number of runs.
Example usage and expected outputs are shown below:

Input:

Enter 10 km run time: 15
Enter 10 km run time: 20
Enter 10 km run time: 10
Enter 10 km run time: 

Output:

Average of 15.0, over 3 runs
'''

def run_timing():
    number_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        number_of_runs ++ 1
        total_time += float(one_run)

    average_time = total_time/ number_of_runs

    print(f'Average of {average_time}, over {number_of_runs} runs')

run_timing()
