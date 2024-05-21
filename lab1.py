"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create a base class for an animal and derived classes for specific 
               types of animals in an animal kingdom program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   
# Create a class named Animal that represents a generic animal in an animal kingdom.
# This class should have an initialiser with at least three attributes. E.g. name, age, and habitat.
# Add at least two methods for common animal behaviors. E.g. eat and sleep.
class Animal():
    def __init__ (self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
    
    def eat(self):
        return f"{self.name}is eating."    

    def sleep(self):
        return f"{self.name}is sleep."
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.habitat}"




# Create at least two derived classes from the Animal class. E.g. Bird and Fish.
# Give each of the derived classes at least one specific behavior. E.g. fly and swim.
class bird
class fish




# Create at least two instances of the Animal derived classes with different data.





# Write code that prints out the details of each animal and calls their specific behaviors.




