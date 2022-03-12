# kolomolo Python task

*Basic Knowledge Questions:*
  > What is \_\_main__.py used for?
##### We should use \_\_main__.py because it helps with maintaining clarity of code by having entry point at one line, and also 
##### makes possible for python to execute code more clearly 

  > How to prevent python module code from executing when the module is imported? 
##### Simple answer is that you can't. To be more prescise, you can import just specific parts of module with comination:
##### import \[part] from \[module], but still the module will be started.
##### As stands in documentation here: https://docs.python.org/3/tutorial/modules.html
##### But I've found a pretty obscure solution on StackOverflow here: https://stackoverflow.com/a/26392791

  > What's the name of method that represents a class constructor in Python?
##### Class constructor in Python is called by \_\_init__ method.

  > What options do you have when you need to insert value of a variable into string? Name at least three.
##### 1. ('string {} string').format(inserted_value)
##### 2. (f'string {inserted_value} string')
##### 3. 'string %s string' % (inserted_value)

  > How can you truly restrict access to a private method of a class in Python?
##### There is any truly secure method to make a private class in python, but the closest thing to do it is to put __ (double underscore) before name of class
##### According to this question on TutorialsTeacher :  https://www.tutorialsteacher.com/python/public-private-protected-modifiers

  > What Python feature would you use to add some functionalities to an existing function without interfering into its code?
##### The most obvious way is to use inner function just by indenting it into existing function, in this way we aren't modyfying existing code, just adding a new one.

  > How is @staticmethod different from @classmethod?
##### Most notable diffrence is that a static method doesn't require specific parameters where class method takes cls as first parameter,
##### second diffrence is that a static method cannot access nor modify class state, where class method have no problem with doing so.
##### Another difference that emerge from second one, static methods 'know' nothing about class state, they just work with given parameters, where class method is the opposite,
##### it takes class as parameter.

  > What is the advantage of using with keyword when reading/writing a file in Python?

##### The 'with' statement helps with clearer syntax (for example, by using that statement we don't have to worry about writing file.close() at the end of code, it is done
##### automaticly), and also it helps with Exeption Handling according to this answer on StackOverflow: https://stackoverflow.com/a/713814

* Problem Solving *

  > Fixed code is added to this repository

* Create something whilst learning something new *
