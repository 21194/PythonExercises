from tkinter import *
import random

names_list = []
global questions_answers
asked = []
score=0

questions_answers = {
    1: ["What must you do when you see blue and red flashing lights behind you?",
        'Speed up to get out of the way','Slow down and drive carefully',
        'Slow down and stop','Drive on as usual','Slow down and stop',3],
    2: ["You may stop on motorway only if:",'if there is an emergency',
        'To let down or pick up passengers','to make U-turn',
        'To stop and take a photo','If there is an emegency',1],
    3: ["When coming up to a pedestrian crossing without raised traffic island, what must you do?",
        'Speed up before the pedestrians cross','Stop and give way to pedestrians on any part of the crossing',
        'Sound the horn on your vehicle to warn the pedestrians',
        'Slow down to 30kmh','Stop and give way to pederians on any part of the crossing',2],
    4: ["Can you stop on a bus stop in a private motor vehicle?", 'Only between midnight and 6am',
        'Under no circumstances','when dropping off passengers','Only it it is less than 5 minutes',
        'Under no circumstances',2],
    5: ["What is the maximum speed you may drive if you have a 'space saver wheel' fitted? (km/h)",
        '70 km/h','100 km/h so you do not hold up traffic','80 km/h and if the wheel spacer displays a lower limit that applies',
        '90 km/h','80 km/h and if the wheel spacer displays a lower limit that applies',3],
    6: ["When following another vehicle on a dusty road, you should:",'Speed up to get passed',
        "Turn your vehicle's windscreen wipers on",'Stay back from the dust cloud',
        'Turn your vehicles headlights on', 'Stay back from the dust cloud',3],
    7: ["What does the sign containing the letters 'LSZ' mean",'Low Safety zone', 'Lone star zone', 'Limited speed zone',
        'Limited speed zone',4],
    8: ["What speed are you allowed to pass a school bus that has stopped get on or off?",'20 km/h',
        '30 km/h','70 km/h','10 km/h','20 km/h',1],
    9: ["What is the maximum distance a load may extend in front of a car?",'2 meters forward of the front edge of the front seat',
        '4 meters forward of the front edge of the front seat','3 meters forward of the front seat','2.5 meters forward of the front edge of the front seat',
        '3 meters forward of the front edge of the front seat',3],
    10: ["To avoid being blinded by the headlights of another vehicle coming towards you, what should you do?",
         'Look to the left of the road','look to the center of the road',
         'Wear sunglasses that have sufficient strength','Look to the right side of the road',
         'Look to the left of the road',1]
}

def randomiser():
    global qnum #qnum is the key in the dictionary questions_answers, we have 10 keys/questions
    qnum = random.randint(1,10) #randomises the order of questions asked
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()

class QuizStarter:
    def __init__(self, parent):
        background_colour="OldLace"
        #grid frame arrangement
        self.quiz_frame = Frame(parent,bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        self.heading_label = Label (self.quiz_frame, text = "NZ Road Rules", bg=background_colour)
        self.heading_label.grid(row=0)
        
        self.user_label = Label ( self.quiz_frame, text="Please enter your username below", bg=background_colour)
        self.user_label.grid(row=1)

        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,pady=20)

        self.continue_button = Button (self.quiz_frame, text ="Continue", bg="orange", command=self.name_collection)
        self.continue_button.grid(row=3,pady=20)


    def name_collection(self):
        name = self.entry_box.get()
        names_list.append(name)
        print(names_list)
        self.quiz_frame.destroy()
        Quiz(root)

class Quiz:
    def __init__(self, parent):
        background_colour="OldLace"
        #new frame set up
        self.quiz_frame = Frame(parent,bg = background_colour, padx=100, pady=100)
        self.quiz_frame.grid()

        randomiser()

        self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], bg=background_colour)
        self.question_label.grid(row=0, padx=10, pady=10)

        #holds the value of radio buttons
        self.var1=IntVar()

        #radio button 1
        self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], bg="brown", value=1,variable=self.var1, pady=10,padx=10)
        self.rb1.grid(row=1, sticky=W)
        
        #radio button  2
        self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], bg="brown", value=2,variable=self.var1, pady=10,padx=10)
        self.rb2.grid(row=2, sticky=W)

        #radio button 3
        self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], bg="brown", value=3,variable=self.var1, pady=10,padx=10)
        self.rb3.grid(row=3, sticky=W)

        #radio button 4
        self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], bg="brown", value=4,variable=self.var1, pady=10,padx=10)
        self.rb4.grid(row=4, sticky=W)

        #confirm answer button
        self.quiz_instance = Button(self.quiz_frame, text="Confirm", bg="green", command=self.test_progress)
        self.quiz_instance.grid(row=5, sticky=W)

        #show score
        self.score_label=Label(self.quiz_frame, text="SCORE",bg=background_colour)
        self.score_label.grid(row=6, padx=5, pady=5)

    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])

    
    def test_progress(self):
        print("testing")
#command for confirm answer button, responsible for checking selected answer against correct answer, updating score accordingly, also progresses the quiz 
        


if __name__ == "__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quizStarter_object = QuizStarter(root)
    root.mainloop()