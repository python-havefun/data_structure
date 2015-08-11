__author__ = 'aditya'

from Stack.array_stack import Empty

class ArrayQueue():
    '''Queue follow First In First Out principle'''
    '''We create a default capacity empty list'''
    d_c=10

    def __init__(self):
        '''create an empty queue with default capacity, size and front pointing reference'''
        self._data=[None]*ArrayQueue.d_c
        self._size=0
        self._front=0

    def __len__(self):
        '''return length of queue'''
        return self._size

    def is_empty(self):
        '''return true if queue is empty'''
        return len(self._data)==0

    def first(self):
        '''raise empty execption if queue is empty
                either return front element of queue'''
        if self.is_empty():
            raise Empty('queue is empty')
        return self._data[self._front]

    def dequeue(self):
        '''remove first element of queue
                or raise exception if queue is empty'''
        if self.is_empty():
            raise Empty('queue is empty')
        answer=self._data[self._front]                #assign front element to answer variable
        self._data[self._front]=None                  #now set front to None as we removed this element
        self._front=(self._front+1)% len(self._data)  #now we set front of queue to next using cyclic modulus
        self._size-=1                                 #finally we resize the queue size
        return answer                                 # and return variable answer

    def enqueue(self,e):
        '''In this we add element e at end of the queue
        also resize the queue size if queue data size is almost equal to queue size'''
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1

    def _resize(self,cap):
        '''this will resize queue by double when data size is equal to queue size'''
        old= self._data                         #assign data members of queue to old variable
        self._data=[None]*cap                   #Now create a new list with capacity cap have None
        walk=self._front                        #Make new variable which walk through queue
        for k in range(self._size):             #Now reassign the old Queue in new queue with capcity cap
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)              #this is cyclic modulus to set old elements properly in new queue
        self._front=0


q=ArrayQueue()
print(q.is_empty())
print(q.dequeue())
q.enqueue(5)
q.enqueue(6)
print(q.first())



