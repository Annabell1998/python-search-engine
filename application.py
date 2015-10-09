""" search a word in two URLs"""
import urllib
import sys , os
os.system("reset")
print "***Welcome to Searh engine******"
def words():
	word = raw_input("Enter the word that you want to search: ")
	return word
def search():
	word = words()
	link = raw_input("Enter the first link: ")
	readurl = urllib.urlopen(link)
	lines = readurl.readlines()
	count = 0
	for line in lines:
		if word.lower() or word.capitalize or word.upper() in line:
			line = line.split(".")
			count += 1
	print "contains the word %s times" %(count)
	link2 = raw_input("Enter the second link: ")
	readurl2 = urllib.urlopen(link2)
	lines2 = readurl2.readlines()
	count2 = 0
	for line1 in lines2:
		if word.lower() or word.capitalize() or word.upper() in line1:
			count2 += 1
	print "contains the word %s times" %(count2)
	validation(count, count2, link, link2)

def validation(count1 , count2, link, link2):    
    if count1 > count2:
    	print "The url that has more times the word is: %s" %(link)
    elif count2 > count1:
    	print "The url that has more times the word is: %s" %(link2)
    elif count2 > 0 == count1 > 0:
    	print "both urls have the same number of times the word"
    elif count2 == 0 and count1 == 0:
    	print "the word is not found"
    again()
def again():
	answer = raw_input("Do You want to enter a word again? Y/N: ")
	answer = answer.lower()
	if answer == "y":
		os.system("reset")
		search()
	elif answer == "n":
		os.system("reset")
		print "Good Bye!! have a good day"
		sys.exit()
	else: 
		print "I don't understad, just Y/N"
		again()
search()




          
