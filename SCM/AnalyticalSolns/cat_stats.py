# Run some tests to see channel dynamics for T-type channels 
# 
# 
# 

import numpy as np

# initialize variables
FARADAY = 96520 
R = 8.3134 
KTOMV = 0.0853 

tBase = 23.5  
celsius = 22  
gcatbar = 0   
cai = 5.e-5   
cao = 2       
tfa = 1       
tfi = 0.68    
eca = 140
dt = 0.025


def h2(cal): 
	ki = 0.001    
	h2 = ki/(ki + cal)
	return h2

def ghk(v, ci, co):
	f = KTF(celsius)/2
	nu = v/f
	ghk=-f*(1. - (ci/co)*np.exp(nu))*efun(nu)
	return ghk 

def KTF(celsius):
	KTF = ((25./293.15)*(celsius + 273.15))
	return KTF

def efun(z):
	if abs(z) < 1e-4:
		efun = 1 - z/2
	else:
		efun = z/(np.exp(z) - 1)
	return efun

def alph(v): 
	alph = 1.6e-4*np.exp(-(v+57)/19)
	return alph

def beth(v):
	beth = 1/(np.exp((-v+15)/10)+1.0)
	return beth

def alpm(v): 
	alpm = 0.1967*(-1.0*v+19.88)/(np.exp((-1.0*v+19.88)/10.0)-1.0)
	return alpm

def betm(v):
	betm = 0.046*np.exp(-v/22.73)
	return betm


def states(v, m, h): 
	taum, minf, facm, tauh, hinf, fach = rates(v)
	m += facm*(minf - m) 
	h += fach*(hinf - h)
	return m, h

def rates(v):
	a = alpm(v)
	taum = 1/(tfa*(a + betm(v)))
	minf =  a/(a+betm(v))       
	facm = (1 - np.exp(-dt/taum))
	
	a = alph(v)
	tauh = 1/(tfi*(a + beth(v)))
	hinf = a/(a+beth(v))
	fach = (1 - np.exp(-dt/tauh))
	return taum, minf, facm, tauh, hinf, fach

# initialize 
init_v = -65
taum, minf, facm, tauh, hinf, fach = rates(init_v)
m = minf
h = hinf
gcat = gcatbar*m*m*h*h2(cai)

# compute at different voltages
# store variables
volts = np.linspace(-100, 100, 2000)

rates_store = []

gates_store = []
gcat_store = []
current_store = []


for i in range(len(volts)):
	if i == 0:
		m, h = states(volts[i], minf, hinf)
	else: 
		m, h = states(volts[i], gates_store[i-1][0], gates_store[i-1][1])

	gcat = gcatbar*m*m*h*h2(cai)
	ica = gcat*ghk(volts[i],cai,cao)

	gates_store.append((m,h))
	gcat_store.append(gcat)
	current_store.append(ica)