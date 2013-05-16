import sys
import argparse

def addStack(op):	# add expression to the stack
	"Take the top two values of the value stack, combine them with the operator in prefix notation, and add it back to the stack"
	valA = valStack.pop()
	valB = valStack.pop()
	if args['r'] and valA.isdigit() and valB.isdigit():
		floatA = float(valA)
		floatB = float(valB)		
		if op == operator[0]:
			f = floatA * floatB
		elif op == operator[1]:
			f = floatA / floatB
		elif op == operator[2]:
			f = floatA + floatB
		elif op == operator[3]:
			f = floatA - floatB
		val = str(int(f))
		valStack.append(val)
	else:
		valStack.append('( ' + op + ' ' + valB + ' ' + valA + ' )')

parser = argparse.ArgumentParser(description='Take arithmetic expression in infix notation and return it in prefix notation.')
parser.add_argument('-r', action='store_true', help='reduces input as much as possible by combining numbers (but not letters)')
parser.add_argument('filename', help='filename containing the infix arithmetic expression, with NO newline')
args = vars( parser.parse_args() )

print args
file = open(args['filename'], 'r')
expression = file.read()
expressionList = expression.split()

operator = ['*', '/', '+', '-']
precedence = ['*', '/', '+', '-', ')', '(']
rightParen = ')'
leftParen = '('

opStack = []
valStack = []

for item in expressionList:
	if len(item) == 1 and not operator.count(item) and item != rightParen and item != leftParen:
		valStack.append(item)

	elif operator.count(item):
		while len(opStack) and operator.index(item) > precedence.index( opStack[len(opStack)-1] ):
			op = opStack.pop()
			addStack(op)
		opStack.append(item)

	elif item == leftParen:
		opStack.append(item)

	elif item == rightParen:
		op = opStack.pop()
		while op is not leftParen:
			addStack(op)
			op = opStack.pop()

while len(opStack):
	op = opStack.pop()
	addStack(op)

print valStack.pop()
