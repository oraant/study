from argparse import ArgumentParser
actions = ['open', 'close', 'status']

parser = ArgumentParser()
parser.add_argument('-a', required=True, choices=actions)
parser.add_argument('-t', nargs='*')

args = "-a open -t haha hoho"
print parser.parse_args(args.split())
