#import everything from Tkinter
from Tkinter import *

class AutomaticLeafClassifier():
	def __init__(self,master):
		self.master=master
		self.master.geometry('800x300+100+200')
		self.master.title('AUTOMATIC LEAF-INFECTION DETECTION')
		
		
		self.label1= Label(self.master,text='This is a basic GUI interface having information about Automatic Leaf-Infection Detection\n\n',font="Times 15",fg='blue').grid(row=0,column=2)
		self.button1=Button(self.master,text='ABOUT\nTHE PROJECT',fg='green',command=self.gotoabout,font='bold').grid(row=5,column=2)
		self.button2=Button(self.master,text='How To\nImplement',fg='green',command=self.gotoimplement,font='bold').grid(row=15,column=2)
		self.button3=Button(self.master,text='QUIT',fg='red',command=self.quit,font='bold').grid(row=30,column=2)
		
	def gotoabout(self):
		root2=Toplevel(self.master)
		myGUI=About(root2)
	
	def gotoimplement(self):
		root3=Toplevel(self.master)
		myGUI=Implement(root3)
		
	def quit(self):
		self.master.destroy()
	
class About():
	
	def __init__(self,master):
		self.master=master
		self.master.geometry('1000x700+100+200')
		self.master.title('ABOUT')
		
		self.label1= Label(self.master,text='\t\tAutomatic Leaf-Infection Detection\n\n',font="Times 30",fg='red').grid(row=0,column=1)
		
		
		self.label2= Label(self.master,text='Since, disease detection in plants plays an important role in the agriculture field,as having\n a disease in plants are quite natural. If proper care is not taken in this area then it can\n cause serious effects on plants and due to which respective product quality, quantity or \n productivity is also affected.Plant diseases cause a periodic outbreak of diseases which leads\n to large-scale death. These problems need to be solved at the initial stage, to save life and\n money of people.\nAutomatic detection of plant diseases is an important research topic as it may prove benefits\n in monitoring large fields of crops, and at a very early stage itself it detects the symptoms \nof diseases means when they appear on plant leaves. Farm landowners and plant caretakers \n(say, in a nursery) could be benefited a lot with an early disease detection, in order to\n prevent the worse to come to their plants and let the human know what has to be done beforehand\n for the same to work accordingly, in order to prevent the worse to come to him too.\n\nThis enables machine vision that is to provide image-based automatic inspection, process control.\nComparatively, visual identification is labor intensive less accurate and can be done only\n in small areas.\n The project involves the use of self-designed image processing algorithms and techniques \ndesigned using python to segment the disease from the leaf while using the concepts of machine \nlearning to categorise the plant leaves as healthy or infected.\nBy this method, the plant diseases can be identified at the initial stage itself and the pest and infection \ncontrol tools can be used to solve pest problems while minimizing risks to people and the environment.\n',fg='black',font='Times 15').grid(row=3,column=1)
		
		self.button5=Button(self.master,text="Back",fg='black',command=self.back1,font='Times 20').grid(rows=5,column=1)
	
	def back1(self):
		self.master.destroy()
	
class Implement():
	
	def __init__(self,master):
		self.master=master
		self.master.geometry('1000x400+100+200')
		self.master.title('IMPLEMENTATION DETAILS')
		
		self.label1= Label(self.master,text='\t\Implementation Procedure For the Project is as follows:\n\n',font="Times 25",fg='red').grid(row=0,column=0)
		
		self.label2= Label(self.master,text='+ RGB image acquisition;\n+ Convert the input image from RGB to HSI format;\n+ Masking the green-pixels;\n+ Removal of masked green pixels;\n+ Segment the components;\n+ Obtain useful segments;\n+ Evaluating feature parameters for classification;\n+ Configuring SVM for disease detection.\n\n',fg='blue',font='Times 15').grid(row=6,column=0)
		self.button4=Button(self.master,text="Back",fg='black',command=self.back2,font='Times 20').grid(rows=5,column=0)
	
	def back2(self):
		self.master.destroy()
	
def main():
	root=Tk()
	myGUIFirst=AutomaticLeafClassifier(root)
	root.mainloop()
	
if __name__=='__main__':
	main()