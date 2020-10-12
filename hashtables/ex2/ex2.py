#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# sort through the tickets
# set a "route" as an array with a max length of the amount of tickets
# make a location dict to store?
# loop thru tickets, set ticket sources/destinations
# tickets are stored in an array [tickets]
#Loop through the ticekets and set the ticket's source key to a destination value


#Basically want it to be like --> does a ticket have this as a destination? 
# Does this destination match a tickets departure(source)?
# smack that depature that matches a destination after the destination 

def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = [None] * length
    location = {}

    for ticket in tickets:
        location[ticket.source] = ticket.destination
    next = location["NONE"]

    for i in range(0, length):
        route[i] = next
        next = location[next]

    return route
