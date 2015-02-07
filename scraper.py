import urllib2
import bs4
import re
import pickle

SCHOOLOFCOMPUTERSCIENCE_URL = "http://coursecatalog.web.cmu.edu/schoolofcomputerscience/courses/"
DEPARTMENTOFELECTRICALANDCOMPUTERENGINEERING_URL = "http://coursecatalog.web.cmu.edu/carnegieinstituteoftechnology/departmentofelectricalandcomputerengineering/courses/"
urls = [SCHOOLOFCOMPUTERSCIENCE_URL,
        DEPARTMENTOFELECTRICALANDCOMPUTERENGINEERING_URL]

course_dict = dict()

for url in urls:
    page = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(page)
    courseblocks = soup.find_all('dl', {'class':"courseblock"})
    for courseblock in courseblocks:
        course = courseblock.find('dt').contents[0]
        course_number = re.search(r'[0-9][0-9]-?[0-9]+', str(course)).group().replace("-","")
        course_string = courseblock.find('dd').text
        
        req_string = re.findall(r'requisites?: (?:(?:[0-9][0-9]-?[0-9]+| |\(|\)|and|or)+)', course_string)
        #prereq_string = re.findall(r'rerequisites?: (?:(?:[0-9][0-9]-?[0-9]+| |\(|\)|and|or)+)', course_string)
        #coreq_string = re.findall(r'orequisites?: (?:(?:[0-9][0-9]-?[0-9]+| |\(|\)|and|or)+)', course_string)
        
        # implement extraction of prereq and coreq boolean combinaitons here
        
        # for now, all prereqs and coreqs are treated as prerequisites
        req_course_strings = re.findall(r'[0-9][0-9]-?[0-9]+', str(req_string))
        for i in xrange(len(req_course_strings)):
            req_course_strings[i] = int(req_course_strings[i].replace("-", ""))
        req_courses = list(set(req_course_strings))
        course_name = str(course)
        req_courses = list(set(req_course_strings))
        course_dict[int(course_number)] = {'name': course_name, 'requisites': req_courses}

pickle.dump(course_dict, open("COURSE_DICTIONARY", "wb"))
#debug = pickle.load(open("COURSE_DICTIONARY", "rb"))
#print debug[18447]
