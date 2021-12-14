class Score:
	def __init__(self, hole=[[]], flop=[[],[],[]], turn=[[]], river=[[]], points=0):
		self.cards = hole + flop + turn + river
		self.points = points

	def scores(self):
		print(self.cards,"cards in the hand")
		print(self.cards[0],"first card in hand")
		self.check()
		
	def check(self):
		H,S,C,D = 0,0,0,0
		for i in self.cards:
			if i[1] == "S": S += 1
			if i[1] == "H": H += 1
			if i[1] == "C": C += 1
			if i[1] == "D": D += 1
		if S > 5 or H > 5 or C > 5 or D > 5:
			Flush = True
		nums = []
		for i in self.cards:
			try:
				nums.append(i[0])
			except:
				break
		if len(nums)>5:
			nums = sorted(nums)
			print(nums)
			centre = nums[len(nums)//2]
			print(centre)


