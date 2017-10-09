import os.path
import csv

import json

from pprint import pprint


class BaseCar:
    car_type = ""

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand or ""
        self.photo_file_name = photo_file_name or ""
        self.carrying = carrying or 0.0

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    def get_body_volume(self):
        pass


class Car(BaseCar):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count) or 0


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        if isinstance(body_whl, dict):
            try:
                self.body_width = body_whl.get("width", 0.0)
                self.body_height = body_whl.get("height", 0.0)
                self.body_length = body_whl.get("length", 0.0)
            except IndexError:
                pass
            finally:
                pass
        elif isinstance(body_whl, str):
            # parsing. Seen at https://stackoverflow.com/questions/2175080/sscanf-in-python

            dimensions = body_whl.split(sep="x")
            if dimensions[0]:
                dimensions.extend(["0"]*(3-len(dimensions)))
                (self.body_width, self.body_height, self.body_length) = tuple([x for x in map(float, dimensions)])
            else:
                (self.body_width, self.body_height, self.body_length) = (0.0, 0.0, 0.0)
    def get_body_volume(self):
        return self.body_height * self.body_width * self.body_length


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    dict_list = []
    car_list = []

    try:
        f = open(csv_filename)
        for line in csv.DictReader(f, delimiter=";"):
            dict_list.append(line)
    finally:
        pass

    for d in dict_list:
        car_type = d.get("car_type")
        if car_type == "car":
            car = Car(brand=d.get("brand", ""),
                      photo_file_name = d.get("photo_file_name", ""),
                      carrying = d.get("carrying", 0.0),
                      passenger_seats_count=d.get("passenger_seats_count", 0))
        elif car_type == "truck":
            car = Truck(brand=d.get("brand", ""),
                        photo_file_name=d.get("photo_file_name", ""),
                        carrying=d.get("carrying", 0.0),
                        body_whl=d.get("body_whl", "0.0x0.0x0.0"))

        elif car_type == "spec_machine":
            car = SpecMachine(brand=d.get("brand", ""),
                               photo_file_name=d.get("photo_file_name", ""),
                               carrying=d.get("carrying", 0.0),
                               extra=d.get("extra", ""))
        else:
            car = None
        if car:
            car_list.append(car)

    return car_list




if (__name__=="__main__"):
    cars = get_car_list("coursera_week3_cars.csv")
    pprint(cars)
