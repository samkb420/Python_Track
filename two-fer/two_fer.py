def two_fer(name=None):
	if name == None:
		return "One for you, one for me."
	else:
		return f"One for {name}, one for me."
	


print(two_fer()) 
# print(two_fer("Alice"))


