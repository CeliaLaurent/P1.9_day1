# P1.9_day1
## Assignments P1.9 - Part 1
### Python Function Tabulation/Plot Project

##### basics

The first steps of this exercises were developed inside a `basics` branch of the repository.

- [x] the git repository contains `script.py` which is compatible with python2 and python3; it creates a lists`xval` and populates xval with evenly spaced numbers between -5.0 and 5.0 (inclusive, 0.1 apart) 

- [x] a `yval` list first set to be empty, that will be lated populated with the corresponding y=f(x) values. 

- [x] The resulting two lists shall be visualized with matplotlib as a plot with x and y values. 

- [x] The program shall take a number as command line argument and depending on that number, yval will be filled from a different function. 
- [x] Implement this basic program with support for only f(x) = x as function number 1. 

Write this program in stages (handle command line, fill lists, plot lists) and commit after each step is complete and the program is working this far.

At this point, the banch `basics` contains the python script implementing these basic functions, it was tested with both python2 and 3 and documentation was included, I can merge it into master.

##### polynomial

- [x] Now create a branch “polynomial” off the trunk (aka “master”) and implement two additional functions: 
  - [x] $f(x) = x^2$ as function number 2
  - [x] $ f(x) = x^3$ as function number 3. 

##### trigonometric

- Then create a second branch “trigonometric” off the trunk and implement three additional functions: 
- f(x) = sin(x), 
- f(x) = cos(x),
- f(x) = tan(x) as number 2, 3 and 4.

##### development

- [x] Finally, create a branch “development” off of “master” and add support for printing a “Usage: ...“ message with a list of the supported functions and the corresponding numbers, if no arguments are given.

##### irrational

- [x] Create a third branch “irrational” off this “development” branch and implement the functions: exp(x), and sqrt(|x|) and update the usage message accordingly.

##### mergings

- [x] Switch to branch “polynomial” and merge in the changes from “development”. Then update the usage message as needed. 
- Now switch to “trigonometric”, also merge from “development”, and update the usage message as well. 
- Now switch back to “development” and and change the plot interval from [-5.0; 5.0] to [-3.0; 3.0]. Merge this change to the three branches “polynomial”, “trigonometric”, and “irrational”.
- Create a branch “release_candidate” from “development” and merge in “polynomial”,
“trigonometric”, and then “irrational” and resolve any conflicts in between.
- Update the usage message as needed. 
- Test this version thoroughly, make corrections as needed and finally merge “release_candidate” to “development” and “master”. 
- Delete all branches except “development” and “master”. 
- Add a tag “release_v1” to “master” when done.
