import snap
import matplotlib.pyplot as plt
import time


# Facebook
G1 = snap.LoadEdgeList(snap.PUNGraph, "facebook/0.edges", 0, 1)
DegToCntV1 = snap.TIntPrV()
snap.GetDegCnt(G1, DegToCntV1)
facebook_hist={}
for item in DegToCntV1:
    facebook_hist[item.GetVal2()] = item.GetVal1()
    


plt.title("Node degrees of the different sets", fontsize=14)
plt.ylabel('Number of nodes', fontsize=14)
plt.xlabel('Degree', fontsize=14)
plt.bar(range(len(twitter_hist)), twitter_hist.values(), align='center', label='Twitter')
plt.bar(range(len(gplus_hist)), gplus_hist.values(), align='center', label='G+')
plt.bar(range(len(facebook_hist)), facebook_hist.values(), align='center', label='Facebook')
plt.bar(range(len(slashdot_hist)), slashdot_hist.values(), align='center', label='slashdot')
plt.legend()
plt.show()

def getNeighbors(graph, nodeid):
    neighbors=[]
    print (graph.GetNI(nodeid).GetOutDeg())
    for i in range(0,graph.GetNI(nodeid).GetOutDeg()):
        neighbors.append(graph.GetNI(nodeid).GetNbrNId(i))
    return neighbors

def bfs(graph, nodeid):
    count = 0
    for NI in graph.Nodes():
        count+=1
        if nodeid == NI.GetId():
            return NI.GetId(), count
    return "nope"

def ex5(graph):
    Rnd = snap.TRnd(42)
    Rnd.Randomize() 
    start = graph.GetRndNId(Rnd)
    deptharray = []
    starttime = time.time()

    for i in range(0, 1000):
        Rnd.Randomize() 
        start = graph.GetRndNId(Rnd)
        ID, depth = bfs(graph, start)
        deptharray.append(depth)
    timing = time.time()- starttime
    diameter = sum(deptharray)/len(deptharray)
    return timing, diameter

print ("\nFacebook:\nTime needed: %f\nEstimated Diameter:%i\n" % ex5(G1))
print ("Google Plus:\nTime needed: %f\nEstimated Diameter:%i\n" % ex5(G2))
print ("Twitter:\nTime needed: %f\nEstimated Diameter:%i\n" % ex5(G3))
print ("Slashdot:\nTime needed: %f\nEstimated Diameter:%i\n" % ex5(G4))
