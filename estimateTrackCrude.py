import numpy as np
from math import atan2 as atan2
from math import pi
from math import log as log

def estimateRTrackCrude(hits):
	numHits = len(hits)
	firstHit = hits[0]
	lastHit = hits[numHits-1]

	b = np.array([firstHit[0],firstHit[1]])
	f = np.array([lastHit[0],lastHit[1]])
	twoL = f - b
	twoLnorm = np.linalg.norm(twoL)
	L = twoLnorm/2

	listOfS = list()
	for hit in hits:
		v = np.array([hit[0],hit[1]])
		d = v - b
		p = d*twoL/twoLnorm
		s = np.linalg.norm(d - p)
		listOfS.append(s)

	sagitta1 = np.max(listOfS)

	curvRadius = sagitta/2.0 + L*L/(2.0*sagitta)

	print(sagitta)
	print(curvRadius)

def estimateEtaTrackCrude(hits):
	numHits = len(hits)
	firstHit = hits[0]
	lastHit = hits[numHits-1]
	rhoFirst =  np.sqrt(firstHit[0]*firstHit[0] + firstHit[1]*firstHit[1])
	rhoLast =  np.sqrt(lastHit[0]*lastHit[0] + lastHit[1]*lastHit[1])
	deltaRho = rhoLast - rhoFirst
	deltaZ = lastHit[2] - firstHit[2]
	### Instead of converting to theta and back, why don't we just use a formula?
	theta = np.arctan2(deltaRho,deltaZ)
	eta = -np.log(np.tan(theta/2))

	print(eta)

def estimatePhiTrackCrude(hits)
	numHits = len(hits)
	firstHit = hits[0]
	lastHit = hits[numHits-1]
	firstHit = hits[0]
	secondHit = hits[1]
	deltaX = secondHit[0] - firstHit[0]
	deltaY = secondHit[1] - firstHit[1]
	phi = 0.0
	if deltaX is not 0.0 or deltaY is not 0.0:
		phi = np.arctan2(deltaY, deltaX)

	print phi