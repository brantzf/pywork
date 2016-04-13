import sys

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
        for item in the_list:
                if isinstance(item, list):
                        print_lol(item, indent, level+1, fh)
                else:
                        if indent:    
                                for num in range(level):
                                        print('\t', end='', file=fh)
                        print(item, file=fh)
