
# Python Class Variables and Class Methods Lab

## Introduction
In this lab, we are going to put our skills to the test by creating class methods and class variables that will help our program remember instance objects and allow us to operate on these objects in interesting ways. We will be working with a Driver class, which we can define in our file, `driver.py`.

## Objectives
* Use class variables to keep track of data pertaining to a class
* Define class methods that expose data pertaining to a class

## Instructions

Okay, so, we have a fleet of drivers and we want to be able to make queries to get details about all of these drivers. Our Driver class should have two class variables; `_all` and `_count`. The `_all` class variable should be assigned to a list that keeps track of all instance objects for the Driver class. The `_count` class variable should keep track of the number of drivers in our fleet. Initially, we wont have any drivers, so it should be set to `0`.

> **Note:** remember to re-load code from another file, we need to re-run the cell that imports it in our jupyter notebook



```python
from driver import Driver
```

We want our drivers to have the following attributes; `name`, `car_make`, and `car_model`. Again, by convention these attributes should have a leading underscore and be snakecased where appropriate. We will also want to define instance methods using the appropriate decorator to read (get) all of these attributes.


```python
Driver("Helga Pataki", "Toyota", "Camry")
Driver("Arnold Shortman", "Toyota", "Highlander")
Driver("Gerald Johanssen", "Toyota", "Camry")
Driver("Robert 'Big Bob' Pataki", "Honda", "Pilot")
Driver("Grandpa Phil", "Jeep", "Grand Cherokee")
Driver("Rhonda Wellington Lloyd", "Kia", "Sonata")
Driver("Phoebe Heyerdahl", "Honda", "Civic")
```

Great! Now, onto the more fun stuff. Let's create a few different instance methods that will help us answer questions like how many drivers do we currently have in our fleet? What percent of drivers drive a Toyota and of that, how many drive a Camry? Or more generally, which car make/models do our drivers drive?

To do this, our class will need to have the two class variables we mentioned earlier, `_all` and `_count`, as well as the class methods listed below:

> **Note:** although it is not necessary, feel free to use more class variables such as `_car_makes` or `_car_models`. Also, consider when is the best time to increment our `_count` class variable or add a new instance object to our `_all` list? It should be the last two lines in our `__init__` method after we have instantiated our instance object and instance variables.

```python
class Person:

    _all = []
    _count = 0

    def __init__(self, cls, name, age):
        self.name = name
        self.age = age
        # call class method to append `self` to _all
        # call class method to increment _count by 1

```


```python
Driver.fleet_size() # returns the number of drivers in the fleet
# example: 7
```


```python
Driver.driver_names() # returns a list of driver names as strings
# example: ['Helga Pataki', 'Arnold Shortman','Gerald Johanssen',
# "Robert 'Big Bob' Pataki", 'Grandpa Phil', 'Rhonda Wellington Lloyd',
# 'Phoebe Heyerdahl']
```


```python
Driver.fleet_makes() # returns a list of car makes in the fleet
# example: ['Toyota', 'Toyota', 'Toyota', 'Honda', 'Jeep', 'Kia', 'Honda']
```


```python
Driver.fleet_models() # returns a list of car models in the fleet
# example: ['Camry', 'Highlander', 'Camry', 'Pilot', 'Grand Cherokee', 'Sonata', 'Civic']
```


```python
Driver.fleet_makes_count()
# returns a dictionary containing a histogram with the key of a car make
# pointing to the number of cars of that make in the fleet
# example: {'Honda': 2, 'Jeep': 1, 'Kia': 1, 'Toyota': 3}
```


```python
Driver.fleet_models_count()
# returns a list of dictionaries as histograms with the key of a car model
# pointing to the number of cars of that model in the fleet
# example: {'Camry': 2, 'Civic': 1, 'Grand Cherokee': 1, 'Highlander': 1, 'Pilot': 1, 'Sonata': 1}
```


```python
Driver.percent_of_fleet("Toyota")
# returns the percentage of Toyotas in the fleet
# example: 45.857%
```

> **Hint:** for the last method, `percent_of_fleet`, you will need to return a string that represents the percentage  as a float with the percent sign at the end of the string. We can use the `float()` and `str()` functions to accomplish this as well as concating strings to add the `%` sign:


```python
num = float((2/10)*100)
num_string = str(num)
percent = num_string + "%"
percent
```

## Summary
In this lab we practiced using class methods and class variables to both store our class's instance objects and operate on them in order to provide answers to our questions about the fleet. We might have noticed that the Driver class is getting pretty inflated with these querying methods. Perhaps there is a way we can structure our code to make this a bit cleaner for us? Maybe we could have another class that has these query methods that we use in our other classes? Let's find out!
