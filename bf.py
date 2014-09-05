import sys

class Tape(object):
	def __init__(self):
		self.tape = [0 for i in range(2000)]
		self.point = 0
	def inc_p(self):
		self.point += 1
		if not self.point < len(self.tape):
			print "Error: Tape index > %s" % self.point
			sys.exit(-1)
	def dec_p(self):
		self.point -= 1
		if self.point < 0:
			print "Error: Tape index < 0"
			sys.exit(-1)
	def inc(self):
		self.tape[self.point] += 1
	def dec(self):
		self.tape[self.point] -= 1
	def get(self):
		return self.tape[self.point]
	def set(self, val):
		self.tape[self.point] = val

def getbrackets(code):
	brackets = {}
	opening = []
	for i, v in enumerate(code):
		if v == "[":
			opening.append(i)
		elif v == "]":
			if opening:
				o = opening.pop()
				brackets[i] = o
				brackets[o] = i
			else:
				print "Error: Unbalanced brackets"
				sys.exit(-1)
	return brackets

def run(code):
	b = getbrackets(code)
	tape = Tape()
	p = 0
	while p < len(code):
		c = code[p]
		if c == "+":
			tape.inc()
		elif c == "-":
			tape.dec()
		elif c == ">":
			tape.inc_p()
		elif c == "<":
			tape.dec_p()
		elif c == "[":
			if not tape.get():
				p = b[p]
		elif c == "]":
			if tape.get():
				p = b[p]
		elif c == ".":
			sys.stdout.write(chr(tape.get()%256))
		elif c == ",":
			r = raw_input("")
			if r:
				tape.set(ord(r[0]))
			else:
				p = len(code)
		p += 1

if __name__ == "__main__":
	if len(sys.argv) < 2:
		run(raw_input(""))
	else:
		try:
			with open(sys.argv[1]) as f:
				dat = f.read()
		except:
			print "Error: Couldn't open file"
		else:
			run(dat)