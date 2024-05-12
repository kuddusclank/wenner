SurveyName="New Untitled Survey"
Longitude=""
Lattitude=""
Intervals=0
Elevation=""
global c1
c1=0
global p1
p1=Intervals
global p2
p2= p1 + Intervals
global c2
c2= p2 + Intervals
dataset={"C1":[],"P1":[],"C2":[],"P2":[],"Resistance":[],"K Factor":[],"Resistivity":[],"Lattitude":[],"Longitude":[]}

def add_data(resistance):
	global c1
	dataset["C1"]+=[c1]
	c1 = c1 + Intervals
	global p1
	dataset["P1"]+=[p1]
	p1 = p1 + Intervals
	global p2
	dataset["P2"]+=[p2]
	p2 = p2 + Intervals
	global c2
	dataset["C2"]+=[c2]
	c2 =c2+Intervals
	dataset["Resistance"]+=[resistance]
	K= 2*3.141593*Intervals
	dataset["K Factor"]+=[K]
	R = resistance * K
	dataset["Resistivity"]+=[R]
	dataset["Lattitude"]+=[Lattitude]
	dataset["Longitude"]+=[Longitude]

def config():
	dataset={"C1":[],"P1":[],"C2":[],"P2":[],"Resistance":[],"K Factor":[],"Resistivity":[],"Lattitude":[],"Longitude":[]}



