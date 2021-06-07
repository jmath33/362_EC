def rev(inp):

	str_list = inp.split()
	rev_list = reversed(str_list)
	rev_sent = " ".join(rev_list)

	print(rev_sent)
	return rev_sent

try: input = raw_input
except NameError: pass
sent = input("Type a sentence you would like reversed: ")
rev(sent)
