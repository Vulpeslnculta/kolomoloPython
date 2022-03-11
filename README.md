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
##### 
