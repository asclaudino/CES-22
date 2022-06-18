import abc 

## implementing the problem using the bridge design pattern


## abstract class for the problem
class Vehicle(object):

    def __init__(self, concreteimplementation):
        self.MotorBridge = concreteimplementation
    
    def build_motor(self):
       self.MotorBridge.build_motor()
    
class Car(Vehicle):

    def __init__(self, concreteimplementation) -> None:
        super().__init__(concreteimplementation)
    
    def build_motor(self):
        return super().build_motor()
    
    def details(self) -> None:
        
       print("I am a car.")
       
class Truck(Vehicle):

    def __init__(self, concreteimplementation) -> None:
        super().__init__(concreteimplementation)
    
    def build_motor(self):
        return super().build_motor()
    
    def details(self) -> None:
        print("I am a truck.")    

class MotorCycle(Vehicle):
    
    def __init__(self, concreteimplementation) -> None:
        super().__init__(concreteimplementation)    
    
    def build_motor(self):
        return super().build_motor()
    
    def details(self) -> None:
        print("I am a motorcycle.")
    
            
## interface for the problem
class MotorBridge():
    
    def __init__(self) -> None:
        pass    
    
    @abc.abstractclassmethod
    def build_motor(self):
        """Should be implemented by the concrete implementation subclass"""

## concrete classes for the problem
class HybridMotor(MotorBridge):
    
    def __init__(self) -> None:
        super().__init__()
    
    @classmethod
    def build_motor(self):
        print("Just build a hibrid motor.")            

class CombustionMotor(MotorBridge):
    
    def __init__(self) -> None:
        super().__init__()
        
    def build_motor(self):
        print("Just build a combustion motor.")        

class EletricMotor(MotorBridge):
    
    def __init__(self) -> None:
        super().__init__()
        
    def build_motor(self):
        print("Just build an eletric motor.")
    
## main function

MyCar = Car(HybridMotor())
MyCar.details()
MyCar.build_motor()

MyMotorCycle = MotorCycle(EletricMotor())
MyMotorCycle.details()
MyMotorCycle.build_motor()