import sys
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "design.ui" # Enter file here.
global filename
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    	def __init__(self):
        	QtGui.QMainWindow.__init__(self)
       	 	Ui_MainWindow.__init__(self)
       		self.setupUi(self)
 		self.browse.clicked.connect(self.Test)
		

	def Test(self):
		options = QtGui.QFileDialog.Options()
		options |= QtGui.QFileDialog.DontUseNativeDialog
		filename = QtGui.QFileDialog.getOpenFileName(self,"Select Image To Process", "","All Files (*);;Image Files(*.jpg *.gif)",options=options)
		if filename:
			print(filename)	
        	execfile("main.py")
		

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


