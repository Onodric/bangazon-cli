class Customer():
	"""
	This is the customer class
	methods:
	get_currenct_customer
	"""

	def __init__(self, name, address, city, state, postal, phone):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.postal = postal
		self.phone = phone
		self.active = 0

	def get_current_customer(self):
		"""
		returns all atributes of this instance of customer
		"""
		return[(self.name, self.address, self.city, self.state, self.postal, self.phone, self.active)]



