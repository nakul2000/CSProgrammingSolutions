Rooms = int(input())
Coats = int(input())
Cost = float(input())
subtotalcost = 0
totalcost = 0
roomdict = {}
roomcosts = {}

while Rooms > 0:
    roominfostring = input()
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

HST = round(0.13 * totalcost, 2)
totalcost = round(subtotalcost + HST, 2)
totalcost = round(totalcost,2)


print("PICASSO PAINTERS INVOICE" + "\n" + "ROOM                COST" + "\n" + "-------------------------" + "\n")



for room in roomcosts:
    length = len(room)
    times = 20- length
    print(str(room) + (times * " ") + str(roomcosts[room]))

lengthsub = 17 - len(str(subtotalcost))
lengthtotal = 20 - len(str(totalcost))
lengthHST = 20 - len(str(HST))

print("-------------------------" + "\n" + "SUBTOTAL" + (int(lengthsub) * (" ") + str(subtotalcost) + "\n")
    + "-------------------------" + "\n" + "HST" + (int(lengthHST) * (" ")) + str(HST) + "\n" )


#roomvals = roomdict.pop(roomindex)


