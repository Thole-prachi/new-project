from sys import argv    #from sys module impoting argv 

script , filename = argv    #passing 1 arguement(file name) to run the code 

txt = open(filename)    #saying python to open file which we have passed through command line in line no. 3

print (f"Here's your file {filename}:")   #printing file name
print(txt.read())   #file containt showing on display to read
txt.close()

print("Type the filename again: ")    # Now we are passing file name as an Inpupt
file_again = input("> ")   #new variable created file _again

txt_again = open(file_again) # new variable created and called old variable which we created at line no. 11

print(txt_again.read())  # again prinitng file contain on display
txt_again.close()