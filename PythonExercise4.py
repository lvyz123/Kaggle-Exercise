# SETUP. You don't need to worry for now about what this code does or how it works. If you're ever curious about the 
# code behind these exercises, it's available under an open source license here: https://github.com/Kaggle/learntools/
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *
print('Setup complete.')

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    lucky_list=False
    for num in nums:
        if num % 7 == 0:
            lucky_list=True
    return licky_list

q1.check()

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    bool_list=[]
    for num in L:
        if num > thresh:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return bool_list            

q2.check()

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(1,len(meals)):
        if meals[i]==meals[i-1]:
            return True
    return False

q3.check()

play_slot_machine()

def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    total_earn = 0
    for i in range(n_runs):
        total_earn += play_slot_machine() - 1
    return total_earn/n_runs
    
def slots_survival_probability(start_balance, n_spins, n_simulations):
    """Return the approximate probability (as a number between 0 and 1) that we can complete the 
    given number of spins of the slot machine before running out of money, assuming we start 
    with the given balance. Estimate the probability by running the scenario the specified number of times.
    
    >>> slots_survival_probability(10.00, 10, 1000)
    1.0
    >>> slots_survival_probability(1.00, 2, 1000)
    .25
    """
    success_count=0
    for sim in range(n_simulations):
        current_balance=start_balance;spin_count=0
        while spin_count < n_spins and current_balance > 0:
            current_balance += play_slot_machine() - 1
            spin_count += 1
        if spin_count == n_spins:
            success_count+=1
    return success_count/n_simulations

q5.check()

