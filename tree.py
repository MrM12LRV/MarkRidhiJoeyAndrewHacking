import apis
import os.path, pickle

APP_ID = "497344e6-8142-4f80-8074-d1161133a002"
SECRET_KEY = "8jTm1V9cvkvV_YUWMJBq7iIvSOzpD7M8fY9mTafkmnq5YmDRm6AkEYeI"
schedule_apis_filepath = "schedule"



if (os.path.exists(schedule_apis_filepath)):
    filehandler = open(schedule_apis_filepath, 'r')
    schedule = pickle.load(filehandler)
    print "loaded locally"
else:
    schedule = apis.Scheduling(app_id=APP_ID, app_secret_key=SECRET_KEY)
    filehandler = open(schedule_apis_filepath, 'w')
    pickle.dump(schedule, filehandler) 
    print "loaded from apis"

#print schedule.course(semester='S14', course_number=15112)

def tree():
    return "hi"
