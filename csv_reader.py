class Reader:
	def __init__(self):
		pass
	
	def get_data(self,filename):
		f=open(filename,'r')
		matrix=[]
		for g in f:
			values = g.split(sep=';')
			row=[]
			for i in values:
				row.append(i)
			matrix.append(row)
		return matrix
			