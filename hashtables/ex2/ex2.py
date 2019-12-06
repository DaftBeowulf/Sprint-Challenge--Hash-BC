#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        if ticket.source == "NONE":
            route[0] = ticket.destination
    
    curr_ticket = route[0]
    pointer = 1
    while route[-1] is None:
        route[pointer] = hash_table_retrieve(hashtable, curr_ticket)
        curr_ticket = route[pointer]
        pointer += 1
    return route
