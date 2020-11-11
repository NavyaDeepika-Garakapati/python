# import all required modules
import json
import sys

# Functions required
def check_syntax(myStr): 
    """function to check the string syntax of opening and closing parenthesis"""
    stack = [] 
    for element in myStr: 
        if element == '(': 
            #if element is '(' push it in to stack
            stack.append(element) 
            
        elif element == ')': 
            #if element is ')' 
            #conditions to check: 1. if stack is not empty, 2.if last value in stack is '('
            #if true pop the stack element '(', if not return unbalanced
            if len(stack) != 0 and (stack[len(stack)-1] == '(') : 
                stack.pop() 
            else: 
                return "Unbalanced"
            
    if len(stack) == 0: 
        #check for empty stack for balanced condition 
        return "Balanced"
    else: 
        return "Unbalanced"
    

def string_validation(string):
    """function for string validation with json formatted output """
    if check_syntax(string) == "Balanced":
        # if syntax of string is valid
        # create a list (result_list) by striping all paranthesis
        result_list = []
		
        for n in (string.split()):
            n = n.strip(')')
            n = n.strip('(')
			
            # assuming the only operators present in given string are '&&' and '||'
            if n == '&&':
                n = 'and'
            elif n == '||':
                n = 'or'
            result_list.append(n)
        
        #convert the list to dictionary and then to required json format
        dictionary = {"query":
             { result_list[3]:
              [
                  {
                      result_list[1]:
                         { 
                             (result_list[0].split("="))[0] : ((result_list[0].split("="))[-1]),
                             (result_list[2].split("="))[0] : ((result_list[2].split("="))[-1])
                         }
                   },
                  {
                      result_list[5]:
                         { 
                             (result_list[4].split("="))[0] : ((result_list[4].split("="))[-1]),
                             (result_list[6].split("="))[0] : ((result_list[6].split("="))[-1])
                         }
                  }
              ]
             }
            }
        string_json = json.dumps(dictionary, indent = 4) 
    
        return string_json
    else:
        return "Syntax invalid"


# s = "(A=2 && B=3) || (C=4 && D=5)"
# Run python script with string as an argument like
# python string_validation.py "(A=2 && B=3) || (C=4 && D=5)"
# main driver code
if len(sys.argv) != 2:
    print("wrong parameters!! please provide one input string for validation")
    sys.exit(1)
else:
    input_str = sys.argv[1]
    print(string_validation(input_str))
	
