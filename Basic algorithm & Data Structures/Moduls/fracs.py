def add_frac(frac1, frac2):         # frac1 + frac2
	return[(frac1[0]*frac2[1])+(frac2[0]*frac1[1]),(frac1[1]*frac2[1])]

def sub_frac(frac1, frac2):         # frac1 - frac2
	return[(frac1[0]*frac2[1])-(frac2[0]*frac1[1]),(frac1[1]*frac2[1])]

def mul_frac(frac1, frac2):         # frac1 * frac2
	return[(frac1[0]*frac2[0]),(frac1[1]*frac2[1])]

def div_frac(frac1, frac2):         # frac1 / frac2
	return[(frac1[0]*frac2[1]),(frac1[1]*frac2[0])]

def is_positive(frac):              # bool, czy dodatni
	if(frac[0]>=0):
		return 1
	else: 
		return 0

def is_zero(frac):                 # bool, typu [0, x]
	if(frac[0]==0):
		return 1
	else:
		return 0
def cmp_frac(frac1, frac2):        # -1 | 0 | +1
	a=(frac1[0]*frac2[1])
	b=(frac2[0]*frac1[1])
	if(a>b):
		return 1
	if(a<b):
		return -1
	if(a==b):
		return 0
def frac2float(frac):              # konwersja do float
	return float(frac[0]/frac[1])
f1 = [-1, 2]                  # -1/2
f2 = [0, 1]                   # zero
f3 = [3, 1]                   # 3
f4 = [6, 2]                   # 3 (niejednoznacznosc)
f5 = [0, 2]                   # zero (niejednoznacznosc)

