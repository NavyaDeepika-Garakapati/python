String validation program:

a. string_validation.py python script will take a string as input.
b. The script will validate the string’s syntax based on the balanced paranthesis assumptions
c. If the syntax is correct, the script will convert the string to json and print the same
based on the below assumptions
	1. The operator used is always “=” like in “A=2”
	2. There will only be 2 terms in both inner and outer expressions.
	   For example, (A=2 && B=3) consists of two terms A=2 and B=3. Likewise, the outer expression
	   also consists of only two terms, one is (A=2 && B=3) and other is (C=4 && D=5)
	3. Outer brackets are not mandatory. (A=2 && B=3) || (C=4 && D=5) expression is
	   also valid and would produce the same output as for expression ((A=2 && B=3) || (C=4&& D=5))