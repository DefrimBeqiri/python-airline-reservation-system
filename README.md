# python-airline-reservation-system
In this implementation:

    Passenger class represents a passenger with a name and passport number.
    Flight class represents a flight with a flight number, origin, destination, capacity, and list of passengers.
    AirlineReservationSystem class manages flights and bookings, allowing flights to be added and seats to be booked.
    Seat class represents individual seats on a flight, including seat number and class.
    Flight class now tracks a list of Seat objects instead of just the number of available seats. It also includes methods to book seats, cancel bookings, and add passengers to a waitlist when the flight is full.
    AirlineReservationSystem class includes methods to book flights, cancel bookings, and add passengers to waitlists.
