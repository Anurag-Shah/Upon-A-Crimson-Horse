### by KJH

import os

provs = [415, 4294, 2211, 2209, 2210, 413, 4289, 414, 4300, 2212, 4338, 2215, 428, 4337, 2213, 2216, 4335, 4171, 2222, 4342, 2217, 430, 4331, 2218, 4329, 4330, 2234, 4345, 2220, 435, 2230, 2229, 447, 448, 451, 2226, 578, 427, 2235, 2214, 4334, 4336, 436, 4326, 2221, 4325, 2350, 445, 4324, 2224, 449, 2225, 2228, 4343, 4344, 1968, 444, 453, 454, 458, 1967, 457, 2356, 2363, 455, 2362, 2370, 440, 1973]

def parse_line(line):
	s = line.strip()
	ss = s.split('"')
	tokens = []
	for i,sss in enumerate(ss):
		if i%2==0:
			sss = sss.replace("="," = ").replace("{"," { ").replace("}"," } ")
			if "#" in sss:
				sss = sss.split("#")[0]
				tokens.extend(sss.split())
				return tokens
			tokens.extend(sss.split())
		else:
			tokens.append('"%s"' % sss)
	return tokens

def parse_file(fn):
	def update(dic, new):
		if isinstance(new, dict):
			new = new.items()
		for key, val in new:
			if key not in dic:
				dic[key] = val
			elif isinstance(dic[key], list):
				dic[key].append(val)
			else:
				dic[key] = [dic[key], val]
	d = {}
	names = []
	stack = [(d,"")]
	tokens = []
	key = ""
	with open(fn,"rb") as f:
		ff = f.read()
		fff = ff.decode("iso-8859-1")
		for line in fff.splitlines():
			tokens += parse_line(line)
		for token in tokens:
			if token == "=":
				key = names.pop()
			elif token == "{":
				dd = {}
				update(stack[-1][0], {key: dd})
				stack.append((dd,key))
				key = ""
			elif token == "}":
				if len(stack[-1][0]):
					update(stack.pop()[0], [(n,n) for n in names])
				else:
					k = stack.pop()[1]
					stack[-1][0][k] = []
					update(stack[-1][0], [(k,n) for n in names])
				names = []
			else:
				names.append(token)
				if key:
					update(stack[-1][0], {key: names.pop()})
					key = ""
	return d

def btree(lst, form, body):
	if not len(lst):
		return ''
	elif len(lst) == 1:
		return body % (f"T{str(lst[0]).rjust(2, '0')}", provs[lst[0]])
	else:
		return form % (lst[int(len(lst)/2)],
					   btree(lst[int(len(lst)/2):], form.replace('\n', '\n\t'), body),
					   btree(lst[:int(len(lst)/2)], form.replace('\n', '\n\t'), body))

if __name__ == "__main__":
		cond = 'check_variable = { which = uach_opm_val value = %s }'
		body = 'uach_spawn_opm = { TAG = %s PROV = %s }'
		form = 'if = {\n\t\tlimit = {\n\t\t\t%s\n\t\t}\n\t\t%s\n\t}\n\telse = {\n\t\t%s\n\t}' % (cond, '%s', '%s')

		with open('output.txt', 'w') as f:
			f.write('uach_spawn_opm_bt = { #var #effect\n\t'+btree([i for i in range(0, 69)], form, body)+'\n}')

