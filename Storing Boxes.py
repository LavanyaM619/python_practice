length = 11 
width = 13 
print(length * width)
print(2*(length + width))

#replace the _ with the updated value. Update the width from 13 to 15
width = 15 
print(length * width)
print(2*(length + width))



""""Recall our favourite rectangle from Module 1: Output and Math operators.
Suppose we now want to find the area and perimeter of the rectangle again which has

Length = 11
Width = 13. But now the width has changed from 13 to 15.
So we'll have to change that number in both the equation of area, and in the equation of perimeter.
Instead of changing it in two places each time we change the width, won’t it be easier if we can change it just once?
For that, let's consider doing something like this:

Let’s take a box, call it width and assign the integer 
13
13 to it.
Similarly let’s also take a box called length and assign the integer 
11
11 to it.
Now, to find the area, we just take the numbers inside these two boxes and multiply them.
That is, print(length * width).
Similarly, to print perimeter, we just do print(2 * (length + width)).
Now, if we want to change the width from 13 to 15, we just have to update the variable.
Both the formulae will now be correct, since they take the value from the box."""
