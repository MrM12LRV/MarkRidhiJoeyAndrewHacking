from Tkinter import*
import random
import copy
import time
import courses

edgeList = set()
root = Tk()
class Animation(object):
    # Override these methods when creating your own animation
    def mousePressed(self, event):
        for(key, courseObj) in courseViewDict.items():
            if((courseObj.x+20>event.x) and (courseObj.x-20<event.x)) and\
               ((courseObj.y+20>event.y) and (courseObj.y-20<event.y)):
               courseObj.lightUp()
    
    def mouseEntered(self, event):
        for(key, courseObj) in courseViewDict.items():
            if((courseObj.x+20>event.x) and (courseObj.x-20<event.x)) and\
               ((courseObj.y+20>event.y) and (courseObj.y-20<event.y)):
               courseObj.lightUp()
    
    def keyPressed(self, event): pass
    
    def timerFired(self):
        self.redrawAll()
    
    def init(self): pass
    
    def redrawAll(self):
        for (key, courseObj) in courseViewDict.items():
            courseObj.displayEdges(self.canvas)
        for (key,courseObj) in courseViewDict.items():
            courseObj.displayCirc(self.canvas)
            courseObj.displayCourseNum(self.canvas)
    
    # Call app.run(width,height) to get your app started
    def run(self, width=1600, height=900):
        # create the root and the canvas
        #root = Tk()
        root.title("Schedule Bot")
        self.window=root
        self.width = width
        self.height = height
        self.canvas = Canvas(root, width=width, height=height)
        self.canvas.pack()
        # set up events
        def redrawAllWrapper():
            self.canvas.delete(ALL)
            self.redrawAll()
        def mousePressedWrapper(event):
            self.mousePressed(event)
            redrawAllWrapper()
        def keyPressedWrapper(event):
            self.keyPressed(event)
            redrawAllWrapper()
        root.bind("<Button-1>", mousePressedWrapper)
        root.bind("<Key>", keyPressedWrapper)
        # set up timerFired events
        self.timerFiredDelay = 250 # milliseconds
        def timerFiredWrapper():
            self.timerFired()
            redrawAllWrapper()
            # pause, then call timerFired again
            self.canvas.after(self.timerFiredDelay, timerFiredWrapper)
        # init and get timerFired running
        self.init()
        timerFiredWrapper()
        # and launch the app
        root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

class CourseView(object):

    width = 25
    height = 25

    def __init__(self, course):
         self.x = (int(course.course_number) % 1000) + 10+(int(course.course_number)%100)*4
         self.y = (int(course.course_number) % 10)*70 + 100
         self.x2 = self.x + CourseView.width
         self.y2 = self.y + CourseView.height
         self.course = course
         self.isLighted = False

    def displayCirc(self,canvas):
        if (self.isLighted):
            canvas.create_oval(self.x, self.y,self.x2,self.y2,fill="Yellow")
        else:
            canvas.create_oval(self.x, self.y,self.x2,self.y2,fill="Blue")
        
    def displayEdges(self, canvas):
        for prereq in self.course.requisites:
            if (prereq in courseViewDict):
                prereqView = courseViewDict[prereq]
                canvas.create_line(self.x, self.y, prereqView.x, prereqView.y)
    def displayCourseNum(self,canvas):
        canvas.create_text(self.x,self.y,text=str(int(self.course.course_number)),font="Arial")
    
    def lightUp(self):
        self.isLighted = True

courseViewDict = {}
for (key, value) in courses.course_dictionary.items():
    courseViewDict[key] = CourseView(value)

Animation().run()
