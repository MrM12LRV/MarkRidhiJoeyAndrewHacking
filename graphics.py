from Tkinter import*
import random
import copy
import time
import courses

edgeList = set()
root = Tk()
class Animation(object):

    # Override these methods when creating your own animation
    def rightMousePressed(self, event):
        lighted = False
        for(key, courseObj) in courseViewDict.items():
            if((courseObj.x+20>event.x) and (courseObj.x-20<event.x)) and\
               ((courseObj.y+20>event.y) and (courseObj.y-20<event.y)):
               courseObj.lightUp()
               lighted = True
        if (not lighted):
            for (key, courseObj) in courseViewDict.items():
                courseObj.isLighted = False
        self.redrawAll()
        
    def leftMousePressed(self,event):
        for(key, courseObj) in courseViewDict.items():
            if((courseObj.x+20>event.x) and (courseObj.x-20<event.x)) and\
               ((courseObj.y+20>event.y) and (courseObj.y-20<event.y)):
                self.selected_course = courseObj
                courseObj.updateXY(event.x, event.y)
        self.redrawAll()

    def leftMouseMoved(self,event):
        self.selected_course.updateXY(event.x, event.y)
        self.redrawAll()
    
    def leftMouseReleased(self,event):
        self.selected_course = None
    
    def keyPressed(self, event): pass
    
    def timerFired(self): pass
    
    def init(self):
        self.redrawAll()
    
    def redrawAll(self):
        self.canvas.delete(ALL)
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
        root.bind("<Button-1>", self.leftMousePressed)
        root.bind("<B1-Motion>", self.leftMouseMoved)
        root.bind("<ButtonRelease-1>", self.leftMouseReleased)
        root.bind("<Button-3>", self.rightMousePressed)
        root.bind("<Key>", self.keyPressed)
        self.timerFiredDelay = 250 # milliseconds
        self.canvas.after(self.timerFiredDelay, self.timerFired)
        
        self.init()
        root.mainloop()  # This call BLOCKS (so your program waits until you close the window!)

class CourseView(object):

    width = 25
    height = 25

    def __init__(self, course):
        #self.x = (int(course.course_number) %10000)/10 + (int(course.course_number)%1000)/4- (3*int(course.course_number%100))
        self.x = random.randint(30,1540)
        self.y = (int(course.course_number) % 1000)-40
        self.x2 = self.x + CourseView.width
        self.y2 = self.y + CourseView.height
        self.x1 = self.x - CourseView.width
        self.y1 = self.y - CourseView.height
        
        self.course = course
        self.isLighted = False
        self.drag = False
         
    def updateXY(self,x,y):
        self.x = x
        self.y = y
        self.x2 = self.x + CourseView.width
        self.y2 = self.y + CourseView.height
        self.x1 = self.x - CourseView.width
        self.y1 = self.y - CourseView.height

    def displayCirc(self,canvas):
        if (self.isLighted):
            canvas.create_oval(self.x1, self.y1,self.x2,self.y2,fill="Yellow")
        else:
            canvas.create_oval(self.x1, self.y1,self.x2,self.y2,fill="Blue")
        
    def displayEdges(self, canvas):
        for prereq in self.course.requisites:
            if (prereq in courseViewDict):
                prereqView = courseViewDict[prereq]
                if(self.isLighted):
                 canvas.create_line(self.x, self.y, prereqView.x, prereqView.y,fill="Dark Green",width=8)
                else:
                 canvas.create_line(self.x, self.y, prereqView.x, prereqView.y)
    def displayCourseNum(self,canvas):
        if (self.isLighted==True):
            canvas.create_text(self.x,self.y,text=str(int(self.course.course_number)),font="Arial 20")
        else:
            canvas.create_text(self.x,self.y,text=str(int(self.course.course_number)),font="Arial")
    
    def lightUp(self):
        self.isLighted = True
        for prereq in self.course.requisites:
            if prereq in courseViewDict:
                #print self.course.course_number
                #print prereq
                courseview = courseViewDict[prereq]
                if not courseview.isLighted:
                    courseview.lightUp()

courseViewDict = {}
for (key, value) in courses.course_dictionary.items():
    if (str(key)[0:2] == "18"):
        courseViewDict[key] = CourseView(value)

Animation().run()
