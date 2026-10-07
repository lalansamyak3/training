"""pause a program
inspect variables
execute expressions
move through code line by line
enter functions
leave functions
inspect the call stack
find where an exception occurred
understand logical errors"""

import pdb


def calculate_bill(price, quantity):
    total = price * quantity

    pdb.set_trace()

    discount = total * 0.10
    final_price = total - discount

    return final_price


price = 200
quantity = 3

result = calculate_bill(price, quantity)

print("Final bill:", result)
"""PDB COMMANDS"""
"""set_trace() or breakpoint(): to pause the excecutiom or to enter the debugging"""
"""pdb commands
p:printing 
pp:printing nested list or dictionaryy
n:to excecute a single line works same as the f10 
excecutes current line and movce to the next line without excecuting the function"""
"""s:stepinto to move indide a function works same as f11 """
"""r :works same as f11+shift to stepout come out from function used when you seen the flow of function"""
"""c means continue excecution works same as f5 start debugging and stops only at breakpoint
here we created breakpoint use set_trace()"""
"""q:quit the debugger now """
"""l:list the souce code around current line"""
"""w:where /call stack where am i in the call stack(it tells you who called this function)"""
"""a:argumnet of the current function or use args works same"""
"""p or !:you can excecute python expression using them like ex : p price*quantity"""
"""dir():you are inside python so you can inspect the objects """
"""p type():to check the type here """
"""break or b: to creatye a breakpoint at certain line ex:(pdb) b 4 this means break pouint at line 4"""
"""b: to see all the list of breakpoints use b ex:(pdb) b"""
"""clear:to clear breakppoint number 1 if called one time if twice remove 2 breakpoints """
"""conditional breakpoints: to screate breakpoint or to do pause based on a condition
like ex: for i in range(10):
        result=i*2
        print(result)
        you dont want allthe iteration to complete so you can use it ike 
       (pdb) b 3,i==5   this means break at line 3 when ibecomes 5 
       syntax :b (line) ,condition"""
"""until:allow you to contionue untill a line is reached 
ex: until 6"""
"""help :running this will give you the remianing all the commands (you can see the all the commands you dont need to memorize )"""
"""postmortem debugging: you check wheather xecption is there or not if yes rthen you start debbugging it """
"""once exceptions ahs occured you enter afterward to see what happend"""


def divide(a, b):
    return a / b


try:
    result = divide(10, 0)
except Exception:
    import pdb

    pdb.post_mortem()

divide(10, 0)
"""means if progarm succesfully excecutes then its ok otherwise just start the post_mortem()
with the use of pdb.post_mortem()"""
