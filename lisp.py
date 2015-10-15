
# primiative play

car = lambda lst: lst[0]
cdr = lambda lst: lst[1:]

class Tester:
    def test(self):
        l = [1,2,3,4,5]
        print car(l)
        print cdr(cdr(l))
       
t = Tester()
t.test()

# source of inspiration and discussion
# http://stackoverflow.com/questions/280243/python-linked-list#280280

#---------------------------------------------------------


# Immutable lists are best represented through two-tuples, with None representing NIL. To allow simple formulation of such lists, you can use this function:

def mklist_idea(*args):
    result = None
    for element in reversed(args):
        result = (element, result)
    return result
# To work with such lists, I'd rather provide the whole collection of LISP functions (i.e. first, second, nth, etc), than introducing methods.


# vizualize the execution: http://pythontutor.com/visualize.html#mode=display

#------------------------------------------------------------


# think: http://greenteapress.com/thinkpython/html/chap17.html

w = sys.stdout.write

cons   = lambda el, lst: (el, lst)
mklist = lambda *args: reduce(lambda lst, el: cons(el, lst), reversed(args), None)
car = lambda lst: lst[0] if lst else lst
cdr = lambda lst: lst[1] if lst else lst
nth = lambda n, lst: nth(n-1, cdr(lst)) if n > 0 else car(lst)
length  = lambda lst, count=0: length(cdr(lst), count+1) if lst else count
begin   = lambda *args: args[-1]
display = lambda lst: begin(w("%s " % car(lst)), display(cdr(lst))) if lst else w("nil\n")



class Node: 
  def __init__(self, cargo=None, next=None): 
    self.car = cargo 
    self.cdr = next    
  def __str__(self): 
    return str(self.car)


def display(lst):
  if lst:
    w("%s " % lst)
    display(lst.cdr)
  else:
    w("nil\n")



#--------------------------------------------------------------


# For some needs, a deque may also be useful. You can add and remove items on both ends of a deque at O(1) cost.

from collections import deque
d = deque([1,2,3,4])

print d
for x in d:
    print x
print d.pop(), d



#--------------------------------------------------------------

import itertools

class LinkedList(object):
    """Immutable linked list class."""

    def __new__(cls, l=[]):
        if isinstance(l, LinkedList): return l # Immutable, so no copy needed.
        i = iter(l)
        try:
            head = i.next()
        except StopIteration:
            return cls.EmptyList   # Return empty list singleton.

        tail = LinkedList(i)

        obj = super(LinkedList, cls).__new__(cls)
        obj._head = head
        obj._tail = tail
        return obj

    @classmethod
    def cons(cls, head, tail):
        ll =  cls([head])
        if not isinstance(tail, cls):
            tail = cls(tail)
        ll._tail = tail
        return ll

    # head and tail are not modifiable
    @property  
    def head(self): return self._head

    @property
    def tail(self): return self._tail

    def __nonzero__(self): return True


    # >>> l = LinkedList([1,2,3,4])
    # >>> l
    # LinkedList([1, 2, 3, 4])
    # >>> l.head, l.tail
    # (1, LinkedList([2, 3, 4]))

    # # Prepending is O(1) and can be done with:
    # LinkedList.cons(0, l)
    # LinkedList([0, 1, 2, 3, 4])
    # # Or prepending arbitrary sequences (Still no copy of l performed):
    # [-1,0] + l
    # LinkedList([-1, 0, 1, 2, 3, 4])

    # # Normal list indexing and slice operations can be performed.
    # # Again, no copy is made unless needed.
    # >>> l[1], l[-1], l[2:]
    # (2, 4, LinkedList([3, 4]))
    # >>> assert l[2:] is l.next.next

    # # For cases where the slice stops before the end, or uses a
    # # non-contiguous range, we do need to create a copy.  However
    # # this should be transparent to the user.
    # >>> LinkedList(range(100))[-10::2]
    # LinkedList([90, 92, 94, 96, 98])
