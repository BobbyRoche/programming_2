#Robert Roche
#CS172 Lecture: A Lab: 062

#imports the Socialite class from the socialite file
#comments are easier to see if the page is full screen

from socialite import Socialite                 

                                                                                #method used to create a string used for the html code for the index file
def createIndexfile(socialite_list):                                            #takes in a list of socialites and places the string into an html file to create the page
    html_str = ""
    html_str+=('<html>\n')
    html_str+=('\t\t<head>\n')
    html_str+=('\t\t\t\t<title>List of Socialite Profiles</title>\n')
    html_str+=('\t\t</head>\n')
    html_str+=('\t\t<body>\n')
    html_str+=('\t\t\t\t<h2>List of Socialite Profiles</h2>\n')                 #for loop that creates a link for each socialite
    for socialites in socialite_list:
        html_str+=('\t\t\t\t<p><a href=\"%s.html\">%s %s</a></p>\n'%(socialites.getUserID(),socialites.getFirstName(),socialites.getLastName()))
    html_str+=('\t\t</body>\n')
    html_str+=('</html>')
    return html_str                                                             #html string is returned

def getSocialite(num):                                                          #method used to recieve input from the user, and create a socialite object
    try:                                                                        #try makes sure the user enters an integer.
        socialite_list = []
        num = int(num)
        i=0
        while i<num:
            socialite = Socialite()
            socialite.setFirstName(input("What is the first name?\n"))
            socialite.setLastName(input("What is the last name?\n"))
            socialite.setPicture(input("What is the url for the picture?\n"))
            socialite.setWebsite(input("What is the url of the website?\n"))
            socialite.setDescription(input("What is the website's description?\n"))
            socialite.setUserID(input("What is the userId you would like to use?\n"))
            print("Socialite created\n")
            print(socialite)                                                    #prints the information of the socialite after it is created
            html_file = open(socialite.getUserID()+".html","w")                 #creates an html file for each socialite
            html_file.write(socialite.html())
            html_file.close()
            
            socialite_list.append(socialite)                                    #adds a socialite to the list used for the index
            
            i+=1                                                                #adds one to counter to ensure correct amount of socialites are made
            
        html_file = open("index.html", "w")
        html_file.write(createIndexfile(socialite_list))
        html_file.close()
    except ValueError:                                                          #if it is not an integer, the user recieves an error and is asked to input again until it is correct.
        num = int(input("Incorrect input!\nHow many socialites would you like to create?"))
        getSocialite(num)


num = input("Welcome to the socialite creator!\nHow many socialites would you like to create?") #welcome message, gets input from the user
getSocialite(num)                                                                               #call to method to create socialite
