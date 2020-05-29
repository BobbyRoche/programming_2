#Robert Roche
#CS172-Lecture-A, Lab-062


from complex import complex     #imports the complex class from the complex file, also imports sys for program termination
import sys

def z(n,c):                     #method that recursively uses the mandlebrot set formula given
    if(n==0):
        return 0
    elif(n>0):
        return c + (z(n-1,c)*z(n-1,c)) #recursive statement that follows the formula


def accept_c(c):                #checks if the absolute value of the result of z is greater than 2, if it is it returns false
    result = True               #otherwise, it is true
    for n in range(11):
        if(abs(z(n,c))>2):
            result = False
            return result
    return result

def ask_number(question):       #prints the questions and gets the users input as answers. If the response is exit, the exit function is called
    resp = input((question) + '(or exit):\n')
    if(resp =='exit'):
        exit()
    else:                       #if the response is not exit, the response is cinverted to a float and returned
        resp = float(resp)
        return resp

def display(x,a,y,b,step):      #displays the X's and -'s. This is the visual part of the mandelbrot set.
    if (x <= a and y <= b and step > 0):    #starts must be greater than stops, and step must be greater than 0
        y1 = b                              #variables used to create the complex object
        while (y1 >= y):
            x1 = x
            line = ""
            while (x1 <= a):
                cnum = complex(x1, y1)      #instance of complex number object
                if (accept_c(cnum)):        #calls the function to do all the necessary calculations to for the mandelbrot set, and if true is returned
                    line += "X"             #X is printed, if not - is printed
                else:
                    line += "-"
                x1 += step                  #adds the step to x1 and prints the line, when all are printed x1 adds the step to get to the next line
            print(line)
            y1 = y1-step
    else:
        print('Bad Inputs. Could not render.')  #if the result doesnt fit the requirement of the mandelbrot set, the set will not be rendered

def exit():                                 #exit method which will print exit and end the program
    print("Exit")
    sys.exit()

################-MAIN-########################

print('Welcome to the Mandelbrot Set\nEnter exit at any time to quit.')#welcome message
loop = True
while(loop):                                  #technically an infinite loop, must enter exit to end the program
    x = ask_number('Enter the X start point') #displays questions, and gets the input from the user
    a = ask_number('Enter the X stop point')
    y = ask_number('Enter the Y start point')
    b = ask_number('Enter the Y stop point')
    step = ask_number('Enter the step size')
    display(x,a,y,b,step)                       #calls the function to display the mandelbrot set