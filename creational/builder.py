#!/usr/bin/env python3

"""The idea of the builder pattern is to separate the construction of a complexe object from its
representation

We can then use the same construction process to create different representations. 

We end up with a class that holds the recipe to create the class and than different
classes that understands the parts needed for each subclasses

Director class: 
this is the class that understands the recipe or construction process. you have an attribute builder
on it.

Builder:
understands the different parts

"""

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


# === Car parts ===

class Wheel:
    size = None

class Body:
    horsepower = None

class Engine:
    shape = None

    
class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
        print("the builder has been set to " + str(self.__builder))


    # The algorithm for assembling a Car
    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # The engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheels(wheel)
            i += 1

        return car

class BuilderInterface:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass

    
class JeepBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel
    
    def get(self):
        engine = Engine()
        engine.horsepower = 400
        return engine
    
    def get(self):
        body = Body()
        body.shape = "SUV"
        return body
    
class NissanBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel
    
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 87
        return engine
    
    def getBody(self):
        body = Body()
        body.shape = "shrimp"
        return body
    
