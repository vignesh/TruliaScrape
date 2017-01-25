
from bs4 import BeautifulSoup
import urllib2

def truliaScrape(city,state):
	url = "https://www.trulia.com/real_estate/"+city+"-"+state
	try:
		content = urllib2.urlopen(url).read()
	except:
		print city + ',' + state + " not found, please try again."
		return 

	soup = BeautifulSoup(content, "html.parser")
	priceModule = soup.find_all("p", {"class": "h3 typeEmphasize"})
	piteration  = 1
	for price in priceModule:
		if piteration == 1:
			medianPrice = price.get_text().strip()
		if piteration == 2:
			sqaureFeet = price.get_text().strip()
		if piteration == 3:
			medianRent = price.get_text().strip()
		piteration+=1


	demographicModule = soup.find_all("div", {"class": "h3 typeEmphasize mbn"})
	diteration  = 1
	for stat in demographicModule:
		if diteration == 1:
			singleResidents = stat.get_text().strip()
		if diteration == 2:
			homeOwners = stat.get_text().strip()
		if diteration == 3:
			medianAge = stat.get_text().strip()
		if diteration == 4:
			houseIncome = stat.get_text().strip()
		if diteration == 5:
			collegeEducated = stat.get_text().strip()
		diteration+=1

	print "Breakdown of %s,%s:" % (city,state)
	print "Median rent - % s" % medianRent
	print "Median house price - % s" %  medianPrice
	print "Cost per square feet - % s" % sqaureFeet
	print "Percent of single residents - % s" % singleResidents
	print "Percent of homeOwners - % s" % homeOwners
	print "Median age - % s" % medianAge
	print "Median house incomce - % s" % houseIncome
	print "Percent college educated - % s" %collegeEducated
	print ""

"""def indeedScrape():
	city = raw_input("What city would you like to explore: ")
	state = raw_input("What state is %s in? " % city)
	jobTitle = raw_input("What job are you looking for? ")
	url = "https://www.indeed.com/jobs?q="+jobTitle+"r&l="+city+",+CA&radius=10&jt=fulltime"
	print url
	try:
		content = urllib2.urlopen(url).read()
	except:
		print city + ',' + state + " not found, please try again."
		return 

	soup = BeautifulSoup(content, "html.parser")
	x = soup.find_all("script", {"type": "text/javascript"})
	print x"""

def zipScrape(city,state):
	jobTitle = raw_input("What job are you looking for? ")
	url = "https://www.ziprecruiter.com/candidate/search?search="+jobTitle+"&location="+city+"%2C+CA&radius=5&days="
	try:
		content = urllib2.urlopen(url).read()
	except:
		print city + ',' + state + " not found, please try again."
		return 

	soup = BeautifulSoup(content, "html.parser")
	jobListing = soup.find_all("span", {"class": "just_job_title"})
	print 'List of full time job postings for %s withing a 5 mile radius of %s.' % (jobTitle,city)
	for job in jobListing:
		print job.get_text()

if __name__ == "__main__":
	city = raw_input("What city would you like to explore: ")
	state = raw_input("What state is %s in? " % city)
	truliaScrape(city,state)
	#indeedScrape()
	zipScrape(city,state)
