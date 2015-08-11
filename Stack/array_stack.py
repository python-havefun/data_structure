__author__ = 'aditya'


class Empty(Exception):
    #raise empty execption when stack is empty
    pass

class ArrayStack():
    '''stack is working on First In First Out principle'''

    def __init__(self):
        '''create a constructor which initialize private empty list variable'''
        self._data=[]

    def __len__(self):
        '''Return length of list'''
        return len(self._data)

    def is_empty(self):
        '''return true if stack is empty'''
        return len(self._data)==0

    def push(self,e):
        '''push element at top of stack'''
        self._data.append(e)

    def top(self):
        '''raise empty execption if stack is empty
        or return top element of stack'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        '''raise empty execption if stack is empty
                or remove top element and return it'''
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

s= ArrayStack()
print(len(s))
print(s.is_empty())
s.push(5)
print(s.top())
print(len(s))
s.push(6)
print(s.top())
print(s.pop())


