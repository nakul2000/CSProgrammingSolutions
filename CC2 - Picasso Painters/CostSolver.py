f = open("rooms.txt")
g = open("outputme.txt", 'w')

Rooms = int(f.readline())
Coats = int(f.readline())
Cost = float(f.readline())


subtotalcost = 0
totalcost = 0
roomdict = {}
roomcosts = {}

while Rooms > 0:
    roominfostring = f.readline()
    roomlist = roominfostring.split(",")
    roomlist = list(roomlist)
    roomname = roomlist.pop(0)
    roomlist = list(map(int,roomlist))


    roomdict[roomname] = roomlist

    Rooms -= 1

for room in roomdict:
    roomvals = roomdict[room]
    l = roomvals[0]
    w = roomvals[1]
    h = roomvals[2]
    roomcost = ((2*l*h) + (w*h*2)) * Coats * Cost
    roomcosts[room] = roomcost
    subtotalcost += roomcost

HST = round(0.13 * subtotalcost, 2)
totalcost = round(subtotalcost + HST, 2)
totalcost = round(totalcost,2)



g.write("PICASSO PAINTERS INVOICE" + "\n" + "---------------------------" + "\n" +"ROOM                  COST" + "\n" + "---------------------------" + "\n")



for room in roomcosts:
    length = len(room)
    times = 21 - length
    g.write(str(room) + (times * " ") + "$" + str(roomcosts[room]) + "\n")

lengthsub = 18 - len(str(subtotalcost))
lengthtotal = 16 - len(str(totalcost))
lengthHST = 23 - len(str(HST))

g.writelines("---------------------------" + "\n" + "SUBTOTAL" + (int(lengthsub) * (" ") + "$" + str(subtotalcost) + "\n")
    + "---------------------------" + "\n" + "HST" + (int(lengthHST) * (" ")) + "$" + str(HST) + "\n"
    + "---------------------------" + "\n" + "Total Cost" + (int(lengthtotal) * (" ")) + "$" + str(totalcost))


#roomvals = roomdict.pop(roomindex)


