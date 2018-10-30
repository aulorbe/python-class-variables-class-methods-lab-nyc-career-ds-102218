class Driver():
    _all = [] # keeps track of all instance objects for the Driver class
    # _all is a list of driver objects

    _count = len(_all) or 0  # keeps track of the # of drivers in our fleet

    def __init__(self,name,car_make,car_model):
        self._name = name
        self._car_make = car_make
        self._car_model = car_model
        Driver._all.append(self)
        Driver._count = len(Driver._all) or 0

    @property
    def name(self):
        return self._name

    @property
    def car_make(self):
        return self._car_make

    @property
    def car_model(self):
        return self._car_model

##### CLASS METHODS BELOW #####

    @classmethod
    def fleet_size(cls):
        return Driver._count # returns the number of drivers in the fleet

    @classmethod
    def driver_names(cls):
        return list(map(lambda i:  i.name, Driver._all))

    @classmethod
    def fleet_makes(cls):
        return list(map(lambda i:  i.car_make, Driver._all)) # returns a list of car makes in the fleet

    @classmethod
    def fleet_models(cls):
        return list(map(lambda i:  i.car_model, Driver._all)) # returns a list of car models in the fleet

    @classmethod
    def fleet_makes_count(cls): # returns a dictionary containing a histogram with the key of a car make pointing to the number of cars of that make in the fleet ex: {'Honda': 2, 'Jeep': 1, 'Kia': 1, 'Toyota': 3}
        hist = {}
        for i in Driver.fleet_makes():
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        return hist

    @classmethod
    def fleet_models_count(cls):   # returns a list of dictionaries as histograms with the key of a car model pointing to the number of cars of that model in the fleet
        hist = {}
        for i in Driver.fleet_models():
            if i in hist:
                hist[i] += 1
            else:
                hist[i] = 1
        return hist

    @classmethod
    def percent_of_fleet(cls,car_make):
        total_num_makes = len(Driver.fleet_makes())
        num_toyotas = Driver.fleet_makes_count()[car_make]
        output = (num_toyotas / total_num_makes)*100
        return str(round(output))+'%'

        # returns the percentage of Toyotas in the fleet
        # return a string that represents the percentage as a float with the percent sign at the end of the string.
        # We can use the float() and str() functions to accomplish this as well as concating strings to add the % sign:
