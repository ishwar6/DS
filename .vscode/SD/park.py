from enum import Enum
# from abc import ABC


class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


# Account class: It is parent class
# Admin and Parking Accountant are its two base class

class Account:
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        self.__user_name = user_name
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        None


class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)

    def add_parking_floor(self, floor_name):
        None

    def add_parking_spot(self, floor_name, spot):
        None

    def add_parking_display_board(self, floor_name, display_board):
        None

    def add_entrance_panel(self, entrance_panel):
        None

    def add_exit_panel(self, exit_panel):
        None


class ParkingAttendent(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.ACTIVE):
        super().__init__(user_name, password, person, status)

    def process_ticket(self, ticket_number):
        None

# ParkingSpot: Here is the definition of ParkingSpot and all of its children classes:
# ParkingSpot: Our ParkingLot will have many parking floors and Each parking floor will have many parking spots.
# Our system will support different parking spots
# 1) Handicapped, 2) Compact, 3) Large, 4) Motorcycle, and 5) Electric.


# At a high level, an interface acts as a blueprint for designing classes.
# Like classes, interfaces define methods. Unlike classes, these methods are abstract.
# An abstract method is one that the interface simply defines. It doesn’t implement the methods.
# This is done by classes, which then implement the interface and give concrete meaning to the interface’s abstract methods.
# Python further deviates from other languages in one other aspect.
# It doesn’t require the class that’s implementing the interface to define all of the interface’s abstract methods.

# parking spot can assign vehicle and remove vehicle.
# parking spot will use above class parkingspottype to declare parking_spot_type

class ParkingSpot:
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__free = True
        self.__vehicle = None
        self.__parking_spot_type = parking_spot_type

    def is_free(self):
        return self.__free

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        free = False

    def remove_vehicle(self):
        self.__vehicle = None
        free = True


class HandicappedSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)


# Vehicle: Here is the definition for Vehicle and all of its child classes:
# Vehicle: Vehicles will be parked in the parking spots.
#  Our system will support different types of vehicles
#   1) Car, 2) Truck, 3) Electric, 4) Van and 5) Motorcycle.

class Vehicle(ABC):
    def __init__(self, license_number, vehicle_type, ticket=None):
        self.__license_number = license_number
        self.__type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self, ticket):
        self.__ticket = ticket


class Car(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.CAR, ticket)


class Van(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.VAN, ticket)


class Truck(Vehicle):
    def __init__(self, license_number, ticket=None):
        super().__init__(license_number, VehicleType.TRUCK, ticket)

# ParkingFloor: The parking lot will have many parking floors.
# ParkingFloor: This class encapsulates a parking floor:
# ParkingLot: The central part of the organization for which this software has been designed.
# It has attributes like ‘Name’ to distinguish it from any other parking lots and ‘Address’ to define its location.


class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__display_board = ParkingDisplayBoard()

# ParkingDisplayBoard: Each parking floor will have a display board to show available parking spots
# for each spot type.
# This class will be responsible for displaying the latest availability of free parking spots
# to the customers.

    def add_parking_spot(self, spot):
        switcher = {
            ParkingSpotType.HANDICAPPED: self.__handicapped_spots.put(spot.get_number(), spot),
            ParkingSpotType.COMPACT: self.__compact_spots.put(spot.get_number(), spot),
            ParkingSpotType.LARGE: self.__large_spots.put(spot.get_number(), spot),
            ParkingSpotType.MOTORBIKE: self.__motorbike_spots.put(spot.get_number(), spot),
            ParkingSpotType.ELECTRIC: self.__electric_spots.put(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type')

# ParkingLot: Our system will have only one object of this class.
# This can be enforced by using the Singleton pattern. In software engineering,
#  the singleton pattern is a software design pattern that restricts the instantiation of a class to only one object.
