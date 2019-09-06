# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:
    # Base Class
    def __init__(self):
        pass


class FlightVehicle(Vehicle):
    # Vehicle -> FlightVehicle
    def __init__(self):
        pass


class Starship(FlightVehicle):
    # Vehicle -> FlightVehicle -> Starship
    def __init__(self):
        pass


class Airplane(FlightVehicle):
    # Vehicle -> FlightVehicle -> Airplane
    def __init__(self):
        pass


class GroundVehicle(Vehicle):
    # Vehicle -> GroundVehicle
    def __init__(self):
        pass


class Car(GroundVehicle):
    # Vehicle -> GroundVehicle -> Car
    def __init__(self):
        pass


class Motorcycle(GroundVehicle):
    # Vehicle -> GroundVehicle -> Motorcycle
    def __init__(self):
        pass
