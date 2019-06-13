'''Linked_list data structure common operatorions in python
Definition for singly-linked list
'''
class linkedListNode(object):
	def __init__(self,value):
		self.val = value
		self.next = None

'''traversing a linked list
when you have a programming question in linked-list, you only get the head node and then you need to get the 
rest of the nodes.
'''
class traverselinkedlist(object):
	"""docstring for traverse"""
	def travese(self,head):
		while head.next is not None:
			print(head.val)
			head = head.next
		print(head.val)
		return head

''' inserting nodes

'''
class tail_insertnode(object):
	def insert(self,head,val2insert):
		cur_node = head
		# normally you just get the headnode in your linkedlist, so travese to the end
		cur_node = traverselinkedlist().travese(cur_node)
		# get the tail node and then point to a new node
		cur_node.next = linkedListNode(val2insert)

		return head




def main():
	# generate the sorted linkedlist 3->4->5
	node1 = linkedListNode(3)
	node2 = linkedListNode(4)
	node3 = linkedListNode(5)

	#link the listnode
	node1.next = node2
	node2.next = node3

	head_node = traverselinkedlist()

	head_node.travese(node1)

	# inserting '6' to the original node '3 -> 4 -> 5' and then becomes a new node
	insert_node = tail_insertnode()

	insert_node.insert(node1, 6)

if __name__ == '__main__':
	main()





