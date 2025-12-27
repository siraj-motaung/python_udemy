# In Python, short-circuiting is a fundamental concept where the evaluation of a logical expression stops as soon as the 
# outcome is determined. Interviewers love this topic because it tests whether you understand how Python optimizes code
#  execution and handles potential errors.

def check_me():
    print("Function executed!")
    return True

print(False and check_me())
print(True or check_me())

