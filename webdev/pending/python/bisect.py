import bisect
import sys
Hay = [1,4,5,6,8,12,15,20,21,23,26,29,30]
needles = [0,1,2,5,8,10,22,23,29,30,31]

def demo(bisect_fn):row_fmt = '{0:2d} @ {1:2d} {2}{0:<2d}'
    for needle in reversed(needles):
        position = bisect_fn(Hay, needle)
        offset = position * ' '
        print(row_fmt.format(needle,position,offset))

if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    demo(bisect_fn)
    print('DEMO: ', bisect_fn.__name__)
    print('haystack ->',' '.join('%2d' % n for n in Hay))
    #  List comprehensions, generator expressions, and their siblings set and dict comprehensions now have their own local scope, like functions. Variables assigned within the
# expression are local, but variables in the surrounding scope can still be referenced. Even better, the local variables do not mask the variables from the surrounding scope