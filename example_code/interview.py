"""This module is meant as a series of python bits to demonstrate awareness of various python concepts."""

MODULE_SCOPE='module'

def do_it():
    local_scope = 1


def reverse_case_string(s: str)->str: 
    """Reverse the case of the string."""
    return s.swapcase()


def get_both_types_of_division(dividend: int, divisor: int)->tuple:
    """Perform both precise and imprecise division and return a tuple with the imprecise, precise result."""
    return dividend//divisor, dividend/divisor


def print_numbers_from_input_up_to_five(input: int):
    """Function to show the use of a while loop and the break statement."""
    while input < 100:
        print(input)
        input = input+1
        if input == 5:
            break

    

def print_ten_times():
    """Prints the numbers from 0-9 on separate lines."""
    for i in range(10):
        print(i)

def print_inputs(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)
 
print_inputs('Jed', 'Programmer', first="Jed", mid="S", last="Pittman")


def print_info_about_datatypes():
    print("""
List vs Tuples

Lists are Mutable datatype.
Lists consume more memory
The list is better for performing operations, such as insertion and deletion.
The implication of iterations is Time-consuming
Tuple

Tuples are Immutable datatype.
Tuple consumes less memory as compared to the list
A Tuple data type is appropriate for accessing the elements
The implication of iterations is comparatively Faster
          """)


def return_deepcopy(item):
    """Use deepcopy to return an independent value."""
    from copy import deepcopy
    return deepcopy(item)

def show_new_python311_exception_handling():
    """Show new python 3.11 exception handling."""
    try: 
        raise ExceptionGroup('Example ExceptionGroup', ( 
        TypeError('Example TypeError'), 
        ValueError('Example ValueError'), 
        KeyError('Example KeyError'), 
        AttributeError('Example AttributeError') 
        )) 
    except* TypeError: 
        print("failed")
    except* ValueError as e: 
        print("really failed, see ex")
    except* (KeyError, AttributeError) as e: 
        print("info for the information", e)


def show_new_case_statement():
    """Show the python 3.10+ option to do case statements."""
    user = "jed"
    access = False
    # match statement starts here .
    match user:
        case "Om":
            print("Om do not have access  to the database \
            only for the api code.")
        case "Vishal":
            print(
                "Vishal do not have access to the database , \
                only for the frontend code.")
 
        case "Rishabh":
            print("Rishabh has the access to the database")
            access = True
        case _:
            print("You do not have any access to the code")
 
# How does python garbage collection work?
"""In general, python garbage collection works by using the sys.getrefcount(<variable>).
So, when the count reaches zero, it can be removed. 
https://devguide.python.org/internals/garbage-collector/
"""

# Is python statically or dynamically typed?
def write_python_language_overview():
    """Output content about python."""
    print("""
    When comparing python to other languages like C# or Java, we think about it as being dynamically typed. 
          That is, we don't know the pre-defined type of a variable before we run the code. 

          The truth is slightly more complex. The python code is in fact compiled, but it is perfectly acceptable to change types. This is because underneath, python is storing the variables as references to objects and includes type information with the objects themselves. So if you change x=1 to x='February' both would be valid.

          """)
    

def generate_numbers():
    for r in range(10):
        yield 1+r

# See the Google Python Style Guide
# https://google.github.io/styleguide/pyguide.html#383-functions-and-methods
# Code generated for the function below was written by copilot/AI:
import random

def make_my_string_jumbled(clean_string):
    """
    Return a string where all characters except the first and last are shuffled.

    The shuffling is deterministic, meaning it will produce the same output for the same input.

    Parameters
    ----------
    clean_string : str
        The input string to be jumbled.

    Returns
    -------
    str
        The jumbled string with all characters except the first and last shuffled.

    Examples
    --------
    >>> make_my_string_jumbled('hello')
    'hlelo'
    """
    # Seed the random number generator to make the shuffling deterministic
    random.seed(clean_string)

    # Extract the middle part of the string
    middle = list(clean_string[1:-1])

    # Shuffle the middle part
    random.shuffle(middle)

    # Join the first character, shuffled middle part, and last character
    jumbled_string = clean_string[0] + ''.join(middle) + clean_string[-1]

    return jumbled_string

def show_slices(input_str="default"):
    print("0:0", input[0:0]) # returns ''
    print("1:1", input[1:1]) # returns ''
    print(":-1", input[:-1]) # all but the last letter
    print("-1:", input[-1:]) # returns the last letter only.
    print(":1", input[:1]) # returns the first letter.
    print("1:", input[1:]) # returns the whole thing but without the first letter. 


#Lists are mutable while tuples are immutable.


# Show that the scope of the global variable is global, module, and locals. There are also builtins
# which you could consider to be outermost scope.
if __name__ == "__main__":
    global_variable_scope='global'
    for e in generate_numbers():
        print(e)