def empty(mylist, r):
	if r==0:
		return [[]]
	L=[]
	for i in range (0,len(mylist)):
		first=mylist [i]
		rem=mylist
		comblist=empty(rem,r-1)
		for x in comblist:
			L.append((first,)+tuple(x))
	return L

def diff(mylist, r):
	if r==0:
		return [[]]
	L=[]
	for i in range(0,len(mylist)):
		first=mylist [i]
		rem=[]
		for j in mylist:
			if j!=mylist [i]:
				rem.append(j)
		comblist=diff(rem,r-1)
		for x in comblist:
			L.append([first]+x)
	return L

#def cross (mylist):
#	main=[]
#	c=[]
#	for i in range(len(mylist)):
#		c=[]
#		length=len(mylist [i])
#		for j in range (length-1, -1,-1):
#			c.append(mylist [i][j])
#		main.append(mylist [i]+c)
#	return main

def divider(mylist, d):
	a=len(mylist[0])
	l=[]
	for j in mylist:
		lst=[]
		for i in range(0, a, d):
			lst.append(tuple(j[i:i+d]))
		l.append(tuple(lst))
	return l

def vrect (mylist,d):
	main=[]
	for i in range(len(mylist)):
		c=[]
		for i in range(d):
			c+=mylist [i]
		main.append(c)
	return main

def hrect(rem,d):
	wrong=False
	iminus1=256
	c=[]
	for j in range (len(rem)):
		iminus1=256
		for i in range(len(rem[j])):
			if rem[j][i]==iminus1:
				wrong=True
				break
			iminus1=rem[j][i]
		if wrong==False:
			c.append(rem[j])
		else:
			wrong=False
	final=[]
	r=[]
	for i in range (len(c)):
		r=[]
		for j in range (len(c[i])):
			pixel=[]
			for k in range (d):
				pixel.append(c[i][j])
			r.append(tuple(pixel))
		final.append(tuple (r))
	return final

def vrect(rem,d):
	wrong=False
	iminus1=256
	c=[]
	for j in range (len(rem)):
		iminus1=256
		for i in range(len(rem[j])):
			if rem[j][i]==iminus1:
				wrong=True
				break
			iminus1=rem[j][i]
		if wrong==False:
			c.append(rem[j])
		else:
			wrong=False
	final=[]
	r=[]
	for i in range (len(c)):
		r=[]
		for j in range (d):
			r.append(tuple (c[i]))
		
		final.append(tuple (r))
	return final

def cross (rem2, d):
	final=[]
	for i in range (len(rem2)):
			r=[]
			n=0
			for j in range (d):
				r.append(rem2[i][n])
				if n==0:
					n=1
				else:
					n=0
			final.append(tuple (r))
	final2=[]
	for i in range (len(rem2)):
			r=[]
			n=1
			for j in range (d):
				r.append(rem2[i][n])
				if n==1:
					n=0
				else:
					n=1
			final2.append(tuple (r))
	
	final3=[]
	for i in range(len(final)):
		r=[]
		n=0
		for j in range (d):
			if n==0:
				r.append(tuple (final[i]))
				n=1
			else:
				r.append(tuple (final2[i]))
				n=0
		final3.append(tuple (r))
	return final3

def remove (mylist):
	rem2=[]
	w=False
	for i in mylist:
		i1=256
		for j in i:
			if j==i1:
				w=True
			i1=j
		if w==False:
			rem2.append(i)
		else:
			w=False
	return rem2

def diff_b(rem,d):
	rem2=[]
	w=False
	for i in rem:
		i1=256
		for j in i:
			if j==i1:
				w=True
				break
			i1=j
		if w==False:
			rem2.append(i)
		else:
			w=False
	#print (rem2)
	#print (len(rem2))
	final=[]
	finals=[]
	w=False
	for i in rem2:
		r=[]
		for j in rem2:
			if i==j:
				continue
			for k in range (d-1):
				lis=i[k:k+2]+j[k:k+2]
				#print ("lis = ",lis)
				if(len(set(lis)) == 4):
					continue
				else:
					w=True
					break
			r2=[]
			if w==False:
				r.append(j)
				r2.append(i)
				r2.append(j)
				finals.append(r2)
			else:
				w=False
		final.append(tuple (r))
	#print (final)
	#print (len(rem2))
	#print (len(final))
	final3=[]
	for i in finals:
		n=0
		r=[]
		for j in range (d):
			if n==0:
				r.append(i[n])
				n=1
			else:
				r.append(i[n])
				n=0
		final3.append(tuple (r))
	for i in range (len(final)):
		if len(final[i])!=d-1:
			continue
		else:
			three=[]
			l=list(final[i])
			for m in range (len(l)):
				if m%2!=0 and m!=0:
					three.append(rem2[i])
				three.append(l[m])
			#print (three)
			final3.append(tuple(three))
			threefour=[]
			for m in range (len(l)-1,-1,-1):
				if m%2==0:
					threefour.append(rem2[i])
				threefour.append(l[m])
			#print ("threefour",threefour)
			final3.append(tuple(threefour))
	
	#print (final3)
	#print (len(final3))
	return final3


def ex(colors, D, img_properties):
    print (img_properties)
    if img_properties=="":
    	mylist=empty(colors, D**2)
    	return divider(mylist, D)
    elif img_properties=="pattern_diff_":
     	if D==2:
     		mylist=diff(colors, D*D)
     		return divider(mylist, D)
     	else:
     		mylist=empty(colors, D)
     		return diff_b(mylist,D)
    elif img_properties=="pattern_cross_":
    	mylist=empty(colors, 2)
    	rem2=remove (mylist)
    	return cross(rem2,D)
    elif img_properties=="pattern_hrect_":
    	mylist=empty(colors, D)
    	return hrect(mylist,D)
    elif img_properties=="pattern_vrect_":
    	mylist=empty(colors, D)
    	return vrect(mylist,D)

if __name__ == '__main__':
    # add here your test cases
    pass
