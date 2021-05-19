from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNodeRec(head, pos) :
	#Your code goes here
    if head is None :
        return head

    if pos == 0 :
        return head.next

    count  = 0
    currHead = head
    while currHead is not None and count < (pos - 1) :
        count += 1
        currHead = currHead.next

    if (currHead is None) or (currHead.next is None) :
        return head
    
    currHead.next = currHead.next.next

    return head
