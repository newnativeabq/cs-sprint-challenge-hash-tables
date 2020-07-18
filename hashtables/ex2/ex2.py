class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht_forward = {}
    route = []

    # Load tickets into hashtable and queue
    for ticket in tickets:
        key = ticket.source
        ht_forward.update({key:ticket})

    # Get the starting ticket
    start = ht_forward['NONE']
    route.append(start)


    def get_next(route: list, ht: dict):
        current_ticket = route[-1]
        destination = current_ticket.destination
        if destination != "NONE":
            next_ticket = ht[current_ticket.destination]
            route.append(next_ticket)
            return True
        return False

    while get_next(route=route, ht=ht_forward):
        pass

    locations = [ticket.source for ticket in route]
    return locations[1:]


        


if __name__ == "__main__":
    tickets = [
        Ticket("NONE", "PDX"),
        Ticket("PDX", "DCA"),
        Ticket("DCA", "NONE"),
    ]
    
    locations = reconstruct_trip(tickets, len(tickets))
    print(locations)