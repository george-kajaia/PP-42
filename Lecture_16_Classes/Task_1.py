class MovieTicket:
    cinema_name = "Rustaveli Cinema"
    total_tickets_sold = 0

    def __init__(self, movie_title, seat_number, price):
        self.movie_title = movie_title
        self.seat_number = seat_number
        self.price = price

        MovieTicket.total_tickets_sold +=1

ticket1 = MovieTicket("Tsiskara", 15, 1.5)
ticket2 = MovieTicket("Me movedi", 15, 1.5)
ticket3 = MovieTicket("Maia tskneteli", 15, 1.5)

print(f"Moveie title: {ticket1.movie_title}; Seat number: {ticket1.seat_number}; Ticket price: {ticket1.price};")
print(f"Moveie title: {ticket2.movie_title}; Seat number: {ticket2.seat_number}; Ticket price: {ticket2.price};")
print(f"Moveie title: {ticket3.movie_title}; Seat number: {ticket3.seat_number}; Ticket price: {ticket3.price};")
print(f"Sold ticket quantity: {MovieTicket.total_tickets_sold}")