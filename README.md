# Python_PYQT5_SoundsFineMusicApplication

Brief Description Of The Main Functionalities: 

SoundsFine Music Application allows the user to interact and control a list of songs separated by genre, such as Jazz, Country, Rock, Pop. Choosing to buy ticket for a concert of a singer that pleases you is a feature among the others described below:

Play/Pause Song
Increase/Decrease Sound Volume 
Previous/Next Song
Mark your favourite Song
Stop Application
Add New Genre
Exit Application
Check Singer Concert as Available/Unavailable
Buy Concert Ticket
Pay Concert Ticket
Automatic Updating Of The Ticket Price Status When It Is Payed

Classes: Genre, Singer, Jazz, Country,  Pop, Rock, Concert, and PYQT5GUI.

Data Will Include:  

Genre
Song Title
Song Track Time
Singer Name
Singer Nationality
Concert Availability
Ticket Price
Concert Details


-------------------------------------------------//-------------------------------------------------

Object Oriented Programming Paradigm:

Introduction:

Object-oriented programming brings a very interesting idea, which is the representation of each element in terms of an object, or class. This type of representation seeks to bring the system being created closer to what is observed in the real world. 

An object contains characteristics (attributes) and actions (methods/functions), just as we see in reality. And to extract information from real life and take it to the software context, the practice of abstraction is used.

One of the main objectives of this paradigm is code reuse and to make this possible there are some very important pillars that we will talk about below, such as encapsulation, inheritance and polymorphism.

------------------------//------------------------

Description of the Object Oriented Design Features in Python: 


Encapsulation:

It is one of the main techniques that define object-oriented programming. This is one of the elements that adds security to the application, due to the fact that it makes some properties of the class private, and can only be accessed by instantiating the class and then call the getters and setters methods. With this layer of security, direct access to the class attributes and its functionalities are prevented.


Encapsulation example of private variables of my project:

![image](https://github.com/FE7R7/PYTHON_PYQT5_SoundsFineMusicApplication/assets/147453330/1862fef2-b581-4057-8d9b-13441c26bdf7)


------------------------//-----------------------

Inheritance:

Specifically about optimisation of written code. We have the following scenario, the child class extends from the parent class, it means, it inherits characteristics and functionalities that will be reused thanks to this relationship between the classes, which ends up also contributing to the easier reading and maintenance of the code, which is more concise.


Inheritance example of Jazz class that inherits from Singer of my project:

![image](https://github.com/FE7R7/PYTHON_PYQT5_SoundsFineMusicApplication/assets/147453330/274e2ec8-af62-4dd3-a11d-3715c8ba4f66)


------------------------//-----------------------

polymorphism:

This is another essential point in object oriented programming paradigma. In nature, we see animals for example, or even human beings changing, adapting their actions according to need. People with the same name, but with different approaches to the same situation. So, it is from this idea that polymorphism in object orientation comes from. As we know, child objects inherit the characteristics and actions of their “parents”. However, in some cases, it is necessary that the actions for the same method or function are different. In other words, polymorphism consists of changing the internal body instructions code of a function inherited from a parent object.

Polymorphism example of two functions that override the two functions in the Super class Singer of my project:

![image](https://github.com/FE7R7/PYTHON_PYQT5_SoundsFineMusicApplication/assets/147453330/72ac0ad7-77a3-4a76-9e77-ab1866a00066)


------------------------//-----------------------

Relationships between classes:

Within the object orientation paradigm, we also have association, aggregation and composition.


Association: The object USES another object, which means that the classes interact with each other, are associated with each other, but do not depend on each other to perform.


Aggregation: The object HAS another object, this means that a class A uses another class B as part of itself, accessing and using its characteristics and functionalities. Both can also be instantiated alone and used with other classes in the program.


Composition: The object belongs to another object, basically so that class A that has a class B implemented within it depends on this class B to perform.


Aggregation example of Concert class being aggregated inside the Singer class of my project:


![image](https://github.com/FE7R7/PYTHON_PYQT5_SoundsFineMusicApplication/assets/147453330/0a54f779-2030-4728-b853-41adf37f9848)



------------------------//-----------------------

Summary and Conclusion:


Object Oriented Programming offers a series of advantages that contribute to the development of more robust, flexible and easy to maintain software. In addition to the points already described, we could also mention that objects are independent units that facilitate the division of the code into smaller and more manageable modules, which ends up allowing developers to work in parallel on different parts of the program, increasing team collaboration and productivity.

What I conclude from the experience of developing my project is the power that object-oriented programming provides you through its pillars already mentioned. What particularly catches my attention is the reuse of code, communication between classes whether through inheritance or aggregation and I could not fail to mention the security of being able to make elements private when they require restricted access.

Another point I would like to highlight is that although inheritance allows the override of methods and especially the Python language that allows the developer to do multiple inheritance, which is very useful, I personally found aggregation to be a very interesting way of composing classes and which I intend to use more in new projects.

Since I mentioned the override of inheritance methods, I take the opportunity to highlight how functional it is to be able to standardise method signatures that can have different and appropriate behaviours for each situation and at the same time establish a relationship, connection between classes, thus favouring abstraction logic, organisation and construction of the code and software of the system as a whole according to the needs and different requirements of the real world.


-------------------------------------------------//-------------------------------------------------

Description of the files involved in the project:

Assignment_StartWindow.py: Python file responsible for initializing the Main Window such as its geometry.

Assignment_Classes.py: In this python file we find all the classes involved in the project as well as the relationships between each one.

Assignment_PyQT5.py: It is a file converted from .ui to .py, where we bring all the configurations made for the Graphical User Interface using PyQT5 library (QTDesigner as an exeternal tool for the PyCharm IDE).

Assignment_PyQT5.ui: File that we can use to add or remove graphical functionalities from the application and then convert it back to a .py file and can thus be integrated into the project that is made up of the python files mentioned above.

Ps: To perform the conversion mentioned above, we use an external tool called UI Converter. (PyCharm IDE)

Thank You for your time...


<img width="392" alt="12" src="https://github.com/FE7R7/PYTHON_PYQT5_SoundsFineMusicApplication/assets/147453330/40f5ef8b-1399-42f4-b1f0-81f5031bc861">







