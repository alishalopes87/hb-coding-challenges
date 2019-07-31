class Node(object):
	def __init__(self,key,val):
	self.key = key
	self.val = val
	self.prev = None
	self.next = None

class DLinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

		self.head.next = self.tail
		self.tail.prev = self.head

	def insert(self,node):
		node.next = self.head
		self.head.next.prev = node.next 
		self.head = node 

	def remove_node(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev 

	def remove_tail(self):
		pop = self.tail
		if pop is self.head:
			return None

		self.remove_node(pop)
		return pop 

	def move_to_head(self,node):
		self.remove_node(node)
		self.insert_to_head(node)

class LRUCache(object):
	cache_limit = 3

	def __init__(self):
		self.dll = DLinkedList()
		self.d = dict()
		self.len = 0


	def get(self,key):
		if key not in self.d:
			return -1

		node = self.d[key]
		self.dll.move_to_head(node)
		return node.val

	def add(self, key, value):
		if key not in self.d:
			new_node = Node()
			self.d.key = val
			self.d.val value 
			self.d[key] = new_node
			self.dll.insert()

			if self.len + 1 > cache_limit:
				node = self.dll.pop_tail()
				self.d.pop(pop_node.key)
			else:
				self.len += 1
		else:
			node = self.d[key]
			node.val = value
			self.dll.move_to_head(node)







