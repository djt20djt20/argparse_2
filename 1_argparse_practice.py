import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--message', type=str, help='type message here', required=True)
# the  '--' means that you must type '--message' to make it work in the command line. If you don't put that in, it becomes a positional variable

parser.add_argument('number', type=int, help='put in number here', required=False, default=1)
#default means that you don't have to put it in

#create a variable that lets you access the inputs
args = parser.parse_args()

#arg.message lets you access the message argument
print(args.message+str(args.number))

# from the command line, type: python script.py test 1