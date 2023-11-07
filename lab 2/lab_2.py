class Flight:
    def __init__(self, flight_number, destination, passengers):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = passengers

    def board_passenger(self, passenger):
        self.passengers.append(passenger)

    def get_info(self):
        return f"Flight {self.flight_number} to {self.destination} with {len(self.passengers)} passengers"

class DomesticFlight(Flight):
    def __init__(self, flight_number, destination, passengers, is_economy_class):
        super().__init__(flight_number, destination, passengers)
        self.is_economy_class = is_economy_class

    def get_info(self):
        return super().get_info() + f", Economy class: {self.is_economy_class}"

class InternationalFlight(Flight):
    def __init__(self, flight_number, destination, passengers, has_business_class):
        super().__init__(flight_number, destination, passengers)
        self.has_business_class = has_business_class

    def get_info(self):
        return super().get_info() + f", Business class: {self.has_business_class}"

class Airport:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def get_flights_info(self):
        for flight in self.flights:
            print(flight.get_info())

# Создаем новый аэропорт
airport = Airport()

# Добавляем в аэропорт несколько рейсов
airport.add_flight(DomesticFlight("SU123", "Moscow", ["Ivan", "Maria"], True))
airport.add_flight(InternationalFlight("DL456", "New York", ["John", "Jane"], False))

# Выводим информацию о всех рейсах
airport.get_flights_info()
