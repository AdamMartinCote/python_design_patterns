#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

"""The prototype pattern allows to specify the kinds of objects to create using a prototypical
instance. Then you can create other objects by **copying** the prototype

This becomes useful when an object creation is costly, for exemple if you have to fetch a lot of
data to create an object, but you know those data change unfrequently

The copying is done through a 'clone()' methode. Note that this method can allow apply modifications
to the object

"""

from copy import deepcopy 

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body   = None

        
    def setBody(self, body):
        self.__body = body

        
    def attachWheels(self, wheel):
        self.__wheels.append(wheel)

        
    def setEngine(self, engine):
        self.__engine = engine


    def specification(self):
	print("body: %s" % self.__body.shape)        
	print("engine horsepower: %d" % self.__engine.horsepower)
	print("tire size: %d\'" % self.__wheels[0].size)

    def clone(self):
        return deepcopy(self)
# === Car parts ===

class Wheel:
    pass


class Body:
    pass


class Engine:
    pass
