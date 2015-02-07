import apis

APP_ID = "497344e6-8142-4f80-8074-d1161133a002"
SECRET_KEY = "8jTm1V9cvkvV_YUWMJBq7iIvSOzpD7M8fY9mTafkmnq5YmDRm6AkEYeI"


schedule = apis.Scheduling(app_id=APP_ID, app_secret_key=SECRET_KEY)
print schedule.departments(semester='S14')

def tree():
    return "hi"
