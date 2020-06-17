# working with singly linked lists here 
def find_middle_node_of_linked_list(ll):
    # idea 1:
    # get the length of the linked list 
    # how do we get the length? 
    # traverse the linked list and keep a counter to 
    # count how many jumps we make until we reach the end 
    # once we know the length, we can calculate the midpoint 
    # of that length 
    # use the midpoint formula from binary search 
    # start from the head of the linked list, jump until we
    # reach the midpoint node 

    # idea 2:
    # use two pointers that we'll start at the head of the list
    # the two pointers will run at different speeds:
    # one pointer will run at twice the speed of the other
    fast = ll
    slow = ll 
    # how do we have a pointer run at twice the speed of another? 
    # how do we update the pointers as we're traversing? 
    # if we iterate our slower pointer just as we would a "normal"
    # pointer while traversing a linked list 
    
    # while fast has not reached the end of the list yet 
    # how do we define "the end of the list"? 
    # fast is either on the None or fast is on the tail node 
    while fast and fast.next: 
        fast = fast.next.next 
        slow = slow.next

    # set fast = fast.next.next
    # once the faster pointer reaches the end of the list,
    # where will the slower pointer be? 
    # the slower pointer will be at the middle node 
    # return the node the slower pointer is pointing at 
    return slow 
