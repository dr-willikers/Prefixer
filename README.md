Prefixer
========

Instructions
------------
To run the program, simply navigate to the appropriate directory, and type

    python prefixer.py filename

Where `filename` is the name of the file containing an infix expression (with no newline, where the expression begins at the start of the file). Use the flag `-r` between `python` and `prefixer.py` to indicate that the program should reduce the input.

Algorithm
---------
I maintain two stacks, one holding the operators and the other the current value. I move through the infix expression, adding values to the value stack, and operations to the operator stack. When operators are encountered, depending on a number of conditions (including the precedence of the operator) we will do different things to take care of various cases. Generally, however, take two values off the value stack, and one operator of the operator stack, put them in prefix notation, and put them back on the value stack.

Analysis
--------
Linear time in the number of operators (O) and values (V), so a computational complexity O(O + V) in both time and space. The algorithm also does not check for correct input, so we do not guarantee results for non-standard input.
