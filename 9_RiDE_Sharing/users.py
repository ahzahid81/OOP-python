from abc import ABC, abstractmethod
from datetime import datetime

class Ride_sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_drivers(self, driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'

class User(ABC):
    def __init__(self, name, email, nId) -> None:
        self.name = name
        self.email = email
        #TODO: set user id dynamically
        self.__id = 0
        self.__nid = nId
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    

class Rider(User):
    def __init__(self, name, email, nId, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nId)

    def display_profile(self):
        print(f'Rider: {self.name} and email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            # TODO: set ride properly
            ride_request = Ride_Request(self, destination)
            ride_matcher = Ride_Matching(ride_sharing.drivers)
            self.current_ride = ride_matcher.find_drivers(ride_request)

    def show_current_ride(self):
        print(self.current_ride)



class Driver(User):
    def __init__(self, name, email, nId, current_location) -> None:
        super().__init__(name, email, nId)
        self.current_location = current_location

    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')
    
    def accept_ride(self, ride):
        ride.set_driver(self)


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimate_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self, rider, amount):
        self.end_time = datetime.now()
        self.rider.wallet -=self.estimate_fare
        self.driver.wallet += self.estimate_fare

    def __repr__(self) -> str:
        return f'Ride deatails. Started: {self.start_location} to {self.end_location}'


class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_Matching:
    def __init__(self, driver) -> None:
        self.available_drivers = driver

    def find_drivers(self, ride_request):
        if len(self.available_drivers) > 0:
            #TODO: find the closet driver of the rider
            Driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            Driver.accept_ride(ride)
            return ride
        
class vehicle(ABC):

    speed = {
        'car' : 50,
        'bike' : 60,
        'cng' : 15
    }
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass

class car(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)

    def start_drive(self):
        self.status = 'unavailable'



# check the class intregration

niye_jao = Ride_sharing('Niye jao')
sakib = Rider("sakib khan", "sakib@khan.com", 1254, 'mohakhali', 1200)
niye_jao.add_rider(sakib)
kala_pakhi = Driver('Kala Pakhi', "kala@sada.com", 5648, 'gulshan 1')
niye_jao.add_drivers(kala_pakhi)

print(niye_jao)
sakib.request_ride(niye_jao, 'uttara')
sakib.show_current_ride()