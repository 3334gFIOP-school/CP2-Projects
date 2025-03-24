# Jackson Hauley, Debugging Notes

import trace
import sys

def trace_calls(frame,event,arg): # Frame is what is happening, event is like call or type of thing happening, and arg is the information being used
    if event == "call": # When the function is called
        print(f"Calling function: {frame.f_code.co_name}")
    elif event == "line": # When a new line of code happens
        print(f"Executing line: {frame.f_lineno} in {frame.f_code.co_name}")
    elif event == "return": # When we return stuff
        print(f"{frame.f_code.co_name} returned {arg}")
    elif event == "exception": # When there is an exception
        print(f"Exception in {frame.f_code.co_name}: {arg}")
    return trace_calls
sys.settrace(trace_calls)
tracer = trace.Trace(count=False,trace=True)

#What is tracing?
    # A Way to trace your functions in your program

def add(numone,numtwo):
    print(sub(numone,numtwo))
    return numone+numtwo
def sub(numone,numtwo):
    return numone-numtwo

print(add(5,2))

tracer.run('add(8,9)')
# Basic Tracing command: python -m trace --trace <relative path>

"""
    --trace (displays lines as executed)
    --count (displays number of time executed)
    --listfuncs (displays the functions executed by running the program)
    --trackcalls (displays relationships between functions)
"""

#What are some ways we can debug by tracing?
    # See all the functions and find what went wrong
    # lets you observe what the program is doing and how it is doing it

#How do you access the debugger in VS Code?
    # Press F5 and you can get a whole new perspective that you have never seen before!
    # Dropdown menu

#What is testing?
    #Running your code to make sure it works as required

#What are boundary conditions?
    # Check the entries most likely to be wrong
x = 14j

#How do you handle when users give strange inputs?"
    #Try and except code


