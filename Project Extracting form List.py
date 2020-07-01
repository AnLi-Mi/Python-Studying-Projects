# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list
#that are less than 5.
#Extras:
#Instead of printing the elements one by one,
#make a new list that has all the elements less than 5 from this list in it
#and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains
#only elements from the original list a that are smaller
#than that number given by the user.

# ------------------------------- solution ----------------------------------

#defining the list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#asking user to input the number the program comares the list's elements to

num = int(input(f'Proszę podać dowolną liczbę: '))

print('solution 1----------------------')

for i in a:
    if i<num:
        print (i)

print('solution 2----------------------')

i=0
while i <len(a):
    if a[i]<num:
        print (a[i])
    i+=1

print('solution 3----------------------')

#prepearing empty list to fill it out with extracted elements of list a
b=[]

for i in a:
    if i<num:
        b.append(i)

print (b)
