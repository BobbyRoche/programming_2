#Robert Roche
#CS172 Lecture: A Lab: 062

#start of the socialite class
class Socialite:
    def __init__(self):     #initializes attributes to be empty strings
        self.last_name = ""
        self.first_name = ""
        self.picture = ""
        self.website = ""
        self.description = ""
        self.userID = ""

    def __str__(self):  #string method used to print out the socialites by getting the proper strings from the get methods
        return("Name: " + self.getFirstName() +  " " + self.getLastName()+
               "\nUser ID: " + self.getUserID()+
               "\nPicture: " + self.getPicture() +
               "\nWebsite: " + self.getWebsite() +
               "\nWebsite Description: "+self.getDescription())

    def html(self):     #this method creates html code for the html files by putting the code into a string along with the proper variables placed in the correct positions
        html_str = '<html>'
        html_str += '\n\t<head>'
        html_str += '\n\t\t<title>' + self.getFirstName() + ' ' + self.getLastName()+ '\'s Socialite Page</title>'
        html_str += '\n\t</head>'
        html_str += '\n\t<body>'
        html_str += '\n\t\t<img width=\"400px\" src=\"' + self.picture + '\"'
        html_str += '\nalt=\"' + self.getFirstName() + ' ' + self.getLastName() + '\' Picture\" align=\"RIGHT\" />'
        html_str += '\n\t\t<h1>' + self.userID + '</h1>'
        html_str += '\n\t\t<h2>' + self.getFirstName() + ' ' + self.getLastName() + '</h2>'
        html_str += '\n\t\t<hr />'
        html_str += '\n\t\t<p>'
        html_str += '\n\t\t\t' + self.getFirstName() + ' wants to share'
        html_str += '\n\t\t\t<a href=\"' + self.getWebsite() + '\" target=\"_blank\"'
        html_str += '\n\t\t\t</a>'
        html_str += '\n\t\t\t'+self.description+'</a>  with you:<br />'
        html_str += '\n\t\t\t' + self.getWebsite()
        html_str += '\n\t\t</p>'
        html_str += '\n\t</body>'
        html_str += '\n</html>'
        return html_str

#the set methods allow the user to set each attribute of the socialite to their liking
    def setLastName(self,l):
        self.last_name = l

    def setFirstName(self,f):
        self.first_name = f

    def setPicture(self,p):
        self.picture = p

    def setWebsite(self,w):
        self.website = w

    def setDescription(self,d):
        self.description = d

    def setUserID(self,u):
        self.userID = u
        
#the get methods are used to get the data the variables hold for writing the html code and printing the socialites.
    def getLastName(self):
        return self.last_name

    def getFirstName(self):
        return self.first_name

    def getPicture(self):
        return self.picture

    def getWebsite(self):
        return self.website

    def getDescription(self):
        return self.description

    def getUserID(self):
        return self.userID

