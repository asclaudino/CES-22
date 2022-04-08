import abc

class Aluno(object):
    def __init__(self,name,age, course = "COMP") -> None:
        self.name = name
        self.age = age
        self.course = course
    
    def get_age(self) -> int:
        return self.age

    def get_course(self) -> str:
        return self.course
    
## ways of calling class methods    
Ariel = Aluno("Ariel",23)    
print(Aluno.get_age(Ariel))
print(Ariel.get_age())
m = Ariel.get_age
print(m())

## which object this bound method is bound to?
print(m.__self__)

## using get_course() method
print(Ariel.get_course())


##  -- Static Methods ---


class AlunoStatic(object):
    def __init__(self,name,age, course = "COMP") -> None:
        self.name = name
        self.age = age
        self.course = course

    def get_age(self) -> int:
        return self.age

    def get_course(self) -> str:
        return self.course
    
    @staticmethod
    def hash_course(text) -> str:
        sum = 0
        for c in text:
            sum = sum + ord(c)
        return sum % 10
    
   
    

ArielStatic = AlunoStatic("Ariel",23)
print(ArielStatic.hash_course(ArielStatic.get_course()))

print(AlunoStatic("Ariel",23).get_age is AlunoStatic("Ariel",23).get_age)
print(AlunoStatic("Ariel",23).hash_course is AlunoStatic.hash_course)
print(AlunoStatic("Ariel",23).hash_course is AlunoStatic("Ariel",23).hash_course)

## Class & Abstract Methods --------- 

## meta_class

class Faculdade(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def get_ano_faculdade(self) -> str:
        pass

class AlunoStatic_and_Class(Faculdade):
    faculdade = "ITA"
    @classmethod
    def get_faculdade(cls) -> str:
        return cls.faculdade
    def get_ano_termino_faculdade(self) -> str:
        return "2024"
    
    def __init__(self,name,age, course = "COMP") -> None:
        self.name = name
        self.age = age
        self.course = course

    def get_age(self) -> int:
        return self.age

    def get_course(self) -> str:
        return self.course
    
    @staticmethod
    def hash_course(text) -> str:
        sum = 0
        for c in text:
            sum = sum + ord(c)
        return sum % 10
    
  
    


Ariel_Class = AlunoStatic_and_Class("Ariel",23)
print(Ariel_Class.get_faculdade())
print(Ariel_Class.get_ano_termino_faculdade())
