import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('--date', help="something show up in help")

args = parser.parse_args()

def f(foo=None, date=None):
    print(foo)
    print(date)

f(**args.__dict__)

print(args.foo)

# call the parameters in the argument
print(args.date)
