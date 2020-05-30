a=0
hexadecimal = range(0, 10) + ["A", "B", "C", "D", "E", "F"]


b = """into Scope label _SB.PCI0.LPCB.H_EC insert\n begin\n"""
while a<5:
	for c in hexadecimal:
		b += """	Method (_Q""" + str(a) + str(c) + """, 0, Serialized)  // _Qxx: EC Query\\n\n
        	{\\n\n
            	\RMDT.P1 ("EC _Q""" + str(a) + str(c) +  """ enter")\\n\n
        	}\\n\n"""
	a+=1

b+= "end\n"

f = open("teste.txt", "w")
f.write(b)
f.close()
