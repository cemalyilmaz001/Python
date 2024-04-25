class xx1(object):
	"""docstring for ClassName"""
	def __init__(self,):
		super(xx1, self).__init__()

	def test(self):
		print("xx1 erişim")
		

class xx2(xx1):
	"""docstring for ClassName"""
	def __init__(self,):
		super(xx2, self).__init__()

	def demo(self):
		print("xx2 erişim")
		

class xx3(xx2):
	"""docstring for ClassName"""
	def __init__(self,):
		super(xx3, self).__init__()

	def start(self):
		print("xx3 erişim son")
		self.demo()
		self.test()

		
if __name__ == '__main__':
	start = xx3()
	start.start()