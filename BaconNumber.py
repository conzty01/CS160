from pythonds import Graph, Vertex, Queue


def initGraph():
    g = Graph()

    with open("movie_actors.csv", "r") as f:

        movie = ""
        actorList = []
        for line in f:
            spli = line.split("|")
            #print(spli)

            if spli[0] == movie:                                    # If line has another actor from movie
                actorList.append(spli[1][:-1])
                #print(actorList)

            elif spli[0] != movie:                                  # If line is beginning of new movie
                while actorList:                                    # Create vertices for old movie actors
                    actor1 = actorList.pop()

                    for actor2 in actorList:
                        g.addEdge(actor1, actor2, movie)
                        g.addEdge(actor2, actor1, movie)

                movie = spli[0]                                     # Set movie to new movie
                actorList.append(spli[1][:-1])                      # Append first actor to actorList

        while actorList:                                            # Add final movie actors to graph
            actor1 = actorList.pop()

            for actor2 in actorList:
                g.addEdge(actor1, actor2, movie)
                g.addEdge(actor2, actor1, movie)

        #print(g.getVertex("Kevin Bacon").getConnections())

    return g
def bfs(kevinBacon):
    kevinBacon.setDistance(0)
    kevinBacon.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(kevinBacon)

    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()

        for neighbor in currentVert.getConnections():
            if (neighbor.getColor() == 'white'):
                neighbor.setColor('gray')
                neighbor.setDistance(currentVert.getDistance() + 1)
                neighbor.setPred(currentVert)
                vertQueue.enqueue(neighbor)

        currentVert.setColor('black')
def retrieve(actorVert):
    predList = []
    curVert = actorVert

    while curVert.getId() != "Kevin Bacon":
        #print(curVert.getId())
        predList.append((curVert.getId(), curVert.getPred().getId(), curVert.getWeight(curVert.getPred())))
        curVert = curVert.getPred()

    return predList
# Tang Pui:color black:disc 0:fin 0:dist 8:pred
# 	[Hok Sing Wong:color black:disc 0:fin 0:dist 7:pred
# 	[Chiu-Mo Wong:color black:disc 0:fin 0:dist 6:pred
# 	[Kwun Ling Chow:color black:disc 0:fin 0:dist 5:pred
# 	[Sze Tsang Sun-Ma:color black:disc 0:fin 0:dist 4:pred
# 	[Fung Woo:color black:disc 0:fin 0:dist 3:pred
# 	[Wing-Chung Leung:color black:disc 0:fin 0:dist 2:pred
# 	[Robert Patrick:color black:disc 0:fin 0:dist 1:pred
# 	[Kevin Bacon:color black:disc 0:fin 0:dist 0:pred
# 	[None]

def main():
    print("Initializing...")
    g = initGraph()
    print("Almost Complete...")
    bfs(g.getVertex("Kevin Bacon"))
    print("Initializing Complete\n")

    exit = False
    while exit != True:
        actor = input("Enter the name of an actor. (Enter 'exit' to quit)\n")
        if actor.lower() == "exit":
            exit = True

        elif actor not in g.getVertices():
            print("INVALID ACTOR: Actor '{}' is not in our records\n".format(actor))

        else:
            baconLadder = retrieve(g.getVertex(actor))
            print("{} has a Bacon Number of {}".format(actor, g.getVertex(actor).getDistance()))
            for rung in baconLadder:
                print("{} acted with {} in {}".format(rung[0], rung[1], rung[2]))
            print("")
main()

# large bacon numbers:  Tang Pui, Hristo (II) Hristov, Wagle Sandow, Kazuya Taguchi

