import apis
import cPickle

# dictionary from coursenumber to {name, requisites}
courses = cPickle.load(open("COURSE_DICTIONARY", "rb"))

APP_ID = "497344e6-8142-4f80-8074-d1161133a002"
SECRET_KEY = "8jTm1V9cvkvV_YUWMJBq7iIvSOzpD7M8fY9mTafkmnq5YmDRm6AkEYeI"
schedule = apis.Scheduling(app_id=APP_ID, app_secret_key=SECRET_KEY)

class Course(object):

    def __init__(self, coursenumber):
        self.course_number = coursenumber
        self.name = courses[coursenumber]['name']
        self.requsities = courses[coursenumber]['requisites']
        self.inFall = False
        self.inSpring = False

course_dictionary = dict()
for coursenumber in courses.keys():
    course_dictionary[coursenumber] = Course(coursenumber)
