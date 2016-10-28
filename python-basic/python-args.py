import argparse

parser = argparse.ArgumentParser(
    
)

# name of action
parser.add_argument(
    'action',
    metavar='action',
    choices=['insert', 'clear', 'show', 'reset'],
    help='Actions is < insert | clear | show | reset >'
)

# name of ORM tables in models
parser.add_argument(
    'tables',
    metavar='tables',
    nargs='*',
    choices=['a', 'b', 'c', 'd', 'all'],
    default=[['a','b']],
    help='ORM tables you want to handle,blank means ALL'
)

print parser.parse_args()
