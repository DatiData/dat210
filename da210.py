# This is just a quick hack to get the data into graph format
# It is not intended for use by anyone but me, but if you find 
# It useful, more power to you

# This program is in the public domain
# matplotlib is a dependency

# Requires python 2.x
# Not sure if it will work in Python 3.x

import csv
import sys
import matplotlib.pyplot as plt

def getdata(fname):
	# this grabs the data from the csv file using python's built in csv library
    f = open(fname, 'rt')
    q=[]
    reader = csv.reader(f)
    for row in reader:
        q.append(row)
        
    f.close()
    return q




def drawImportancePie(q, tocheck):
	# This function draws a pie chart of importance 
	# It is passed a list that contains the data from the csv file
	# This data is also in list form
	# Note that this can also be used on subsets of the CSV file by passing
	# lists containing subsets of the data.
	
	
    pricecount=0
    featurescount=0
    lookscount=0
    brandcount=0
    compatabilitycount=0

    titles=['Least Important', 'Not Very Important', 'Neutral', 'Somewhat Important', 'Most Important']
    # The following is pretty self explanatory
    for i in q:
        if i[4]==tocheck:
            pricecount=pricecount+1
        if i[5]==tocheck:
            featurescount=featurescount+1
        if i[6]==tocheck:
            lookscount=lookscount+1
        if i[7]==tocheck:
            brandcount=brandcount+1    
        if i[8]==tocheck:
            compatabilitycount=compatabilitycount+1
    
    # This is the MatPlotLib stuff that draws the pie chart
    # First I set the labels for each segment and the count for 
    # each segment in matched order.  MatPlotLib automatically 
    # changes the counts into percentages
    labels= 'Price', 'Features', 'Looks/Aesthetics', 'Brand', 'Compatability with current devices'
    sizes=pricecount, featurescount, lookscount, brandcount, compatabilitycount
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow="True")
    plt.axis('equal')
    plt.title(titles[int(tocheck)-1])
    plt.show()

def drawStreamingBar(q):
    netflix=0
    amazon=0
    hulu=0
    vudu=0
    hboGo=0
    hboNow=0
    nada=0
    other=0
    labels=['Netflix', 'Amazon Prime \nVideo', 'Vudu', "Hulu", "HBO Go", "HBO Now", "Other", "Doesn't use \n streaming service"] 
    defaultAnswers=['Netflix', 'Amazon Prime Video', 'Vudu', "Hulu", "HBO Go", "HBO Now", "Other", "I don't watch Streaming TV"]   

    for i in q:
        if "Netflix" in i[2]:
            netflix=netflix+1
        if "Amazon Prime Video" in i[2]:
            amazon=amazon+1
        if "Vudu" in i[2]:
            vudu=vudu+1
        if "Hulu" in i[2]:
            hulu=hulu+1
        if "HBO Go" in i[2]:
            hboGo=hboGo+1
        if "HBO Now" in i[2]:
            hboNow=hboNow+1
        if "I don't watch Streaming TV" in i[2]:
            nada=nada+1
        j=i[2].split(",")
        
		# the following voodoo finds stuff entered in the "other" category
		# There's probably a more pythonistic way to do this, but it works
		# So I'll use it
        for r in j:
            if r.lstrip() not in defaultAnswers:
                other=other+1    
    

    y=[netflix, amazon, vudu, hulu, hboGo, hboNow, other, nada]
    x=range(1, len(y)+1)
    width=.75
    plt.bar(x,y,width, align="center")
    # ax=plt.subplots()
    plt.xticks(x, labels)
    plt.title("Usage of popular streaming apps")
    # ax.set_title("Usage of popular streaming apps")
    plt.show()

def drawPurchasingPie(q):
    nextMonth=0
    next3Month=0
    next6Month=0
    nextYear=0
    nada=0
    labels=['The Next Month', 'The Next 3 Months', 'The Next 6 Months', 'The Next Year', "Don't plan purchase\n in the next year"]
    title="Plans on Buying a New Streaming Media Device"
        
    for i in q:
        if i[3]=="The next month":
            nextMonth=nextMonth+1
        elif i[3]=="The next 3 months":
            next3Month=next3Month+1
        elif i[3]=="The next 6 months":
            next6Month=next6Month+1
        elif i[3]=="The next year":
            nextYear=nextYear+1
        else:
            nada=nada+1
    
    explode=(0 ,0, 0, 0, .1)        
    sizes= nextMonth, next3Month, next6Month, nextYear, nada
    plt.pie(sizes, explode=explode,labels=labels, autopct='%1.1f%%', shadow="True", startangle=140)
    plt.axis('equal')
    plt.title(title)
    plt.show()  

def drawSourceGraph(q):
    choices=["Cable Box", "Roku", "AppleTV", "Android TV", "Amazon Fire TV or Amazon Fire Stick", "I have a Smart TV", "I have a Media Server PC", "I only watch video content on my computer, not on my TV", "I don't watch video content at all"]
    cableBox=0
    roku=0
    appleTV=0
    androidTV=0
    amazonFire=0
    smartTV=0
    mediaServer=0
    computer=0
    nada=0
    other=0
    
    for i in q:
        if "Cable Box" in i[1]:
            cableBox=cableBox+1
        if "Roku" in i[1]:
            roku=roku+1
        if "AppleTV" in i[1]:
            appleTV=appleTV+1
        if "Android TV" in i[1]:
            androidTV=androidTV+1
        if "Amazon Fire TV or Amazon Fire Stick" in i[1]:
            amazonFire=amazonFire+1
        if "I have a Smart TV" in i[1]:
            smartTV=smartTV+1
        if "I have a Media Server PC" in i[1]:
            mediaServer=mediaServer+1
        if "I only watch video content on my computer, not on my TV" in i[1]:
            computer=computer+1
        if "I don't watch video content at all" in i[1]:
            nada=nada+1
            
        j=i[1].split(",")
        for r in j:
            if r.lstrip() not in choices:
                other=other+1
    
    y=[cableBox, roku, appleTV, androidTV, amazonFire, smartTV, mediaServer, computer, other, nada]
    labels=["Cable Box", "Roku", "AppleTV", "Android TV", "Amazon Fire TV\n or Amazon Fire Stick", "Smart TV", "Media Server \nPC", "Only watch\n video content\n on computer", "Other", "I don't watch \nvideo content"]
    x=range(1, len(y)+1)
    width=.75
    plt.bar(x,y,width, align="center")
    plt.xticks(x, labels)
    plt.title("How Video Content is Delivered")
    plt.show()

print "Grabbing Data from CSV FILE"
print
q=getdata(sys.argv[1])
print "Drawing Graphs"
print
drawImportancePie(q, '5')
drawImportancePie(q, '4')
drawImportancePie(q, '1')
drawStreamingBar(q)
drawPurchasingPie(q)
drawSourceGraph(q)
female=[]
male=[]

print "Finding respondents who chose to provide their gender"
print "and creating sublists for males and females"
print
for i in q:
	# print i[10].upper()
	if i[10].upper()=="M" or i[10].upper()=="MALE":
		male.append(i)
	if i[10].upper()=="F" or i[10].upper()=="FEMALE":	
		female.append(i)

print "Drawing male and female graphs\n"		
# What do Males find Important
drawImportancePie(male, '5')
# What do Females find Important
drawImportancePie(female, '5')
		
print "Data Breakdown:"

print "The Number of Respondents was ",len(q)-1
print len(male)+len(female), "respondents chose to provide their gender"
print len(male), "identified as male and ",len(female)," identified as female"	
