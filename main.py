
#FUNCTIONAL PROMPT
# Once a functional solution to this problem has been implemented, answer the following questions.
# Q - How does this solution ensure data immutability?
# A - The data will not change becuase it can only print out data that has been declared in the array. 

# Q - Is this solution a pure function? Why or why not?
# A - It is a pure function becuase it does not rely on global variables and outputs unchanged data as it was declared.  Also, functions always return the same output for the same input and don't rely on external state. 

# Q - Is this solution a higher order function? Why or why not?
# A - No, this function is not a higher order function becuase it does not take functions as arguments or returns a function. 

# Q - Would it have been easier to solve this problem using a different programming style?
# A - No, this is a straight forward way of solving this problem. Using the intertools.chain method, which takes a list or lists and returns an iterator in an order list.  

# Q - Why in particular is functional programming a helpful paradigm when solving this problem?
# A - Becaue you can encapsulate the methods to solve the issue. OOP is not necessary in solving this problem. 

#----------------------------------------------------------------------------------------------



#OBJECT ORIENTED PROMPT
# Once an Object Oriented solution has been implemented, answer the following questions:
# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# Encapsulation
# A - Each class Podracer, AnakinsPod and SebulbasPod encapsulates its own data within. 
# Abstraction
# A - Users can create instances of padracer objects and call methods such as repair(), boost(), and flame_jet(). 
# Inheritance
# A - AnakinsPod and SebulbasPod inherit from Podracer class, they inherit attributes max_speed, condition, price and method repair(). 
# Polymorphism
# A - Not demostrated in this code. None of the methods were overrriden. 
# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# A - Not, I belive OOP was build to solve these type of problems where instaces of an object can be passed on and keeping the code DRY.  We also have the ability to model real-world items as objects and manage relationships between them more effectively.
# How in particular did Object Oriented Programming assist in the solving of this problem?
# A - The fact that we can inherit attributes from base classes and extend the functionality by adding new methods. 



#----------------------------------------------------------------------------------------------



# REFLECTION
# Take some time now to think about the lessons we've just covered. Prompting questions have been provided, but reflections do not need to be limited to only their answers.

# Q - Is one of these coding paradigms "better" than the other? Why or why not?
# A - They both serve a different purpose, i think the approach for both of the is adequate. 

# Q - Given the opportunity to work predominantly using either of these coding paradigms, which seems more appealing? Why?
# A - Functional programming is easier to undertand in my opinion. I think the data is easier to follow, pass and render if necessary. 

# Q - Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best handled using functional programming? Object Oriented Programming?
# A - Functional programming can be used 

# Q - Personally, which of these styles takes more work to understand? What should be done in order to deepen understanding related to this paradigm?
# A - I think OOP takes longer to understand. I would need to breakdown each concept (classes, objects, attributes, methods, inheritance, polymorphism, encapulation, abstraction, constructor and destructor). 