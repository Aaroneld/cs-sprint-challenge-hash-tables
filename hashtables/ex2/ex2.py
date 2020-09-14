#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    ticketDict = {}
    tripArr = []

    for ticket in tickets:
        ticketDict[ticket.source] = ticket.destination
    
    currentSource = ticketDict['NONE']

    while currentSource != "NONE":

        tripArr.append(currentSource)

        currentSource = ticketDict[currentSource]
    
    tripArr.append('NONE')


    return tripArr
