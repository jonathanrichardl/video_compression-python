from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QObject, pyqtSlot, QUrl
from PyQt5.QtWidgets import QStyle,QDialog,QWidget
import os
import cv2
import sys
import threading
import time
import numpy as np
from utility.mainwindow import Ui_MainWindow
from utility.model import Model
from utility.encodelib import encode
from utility.decodelib import decode, getDimension, zigzag_to_block
from utility.dialog import Ui_Form
from utility.help import Ui_Help


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.model = Model()

        self.huffButton.clicked.connect(self.displayHuff)
        
        self.browseButton1.clicked.connect(self.browseSourceSlot)
        self.browseButton2.clicked.connect(self.browseDestSlot)
        # self.sourceInput.returnPressed.connect(self.returnSourceSlot)
        # self.DestInput.returnPressed.connect(self.returnDestSlot)
        self.outputName.returnPressed.connect(self.returnNameSlot)
        self.playButton1.clicked.connect(self.playVidSource)
        self.playButton2.clicked.connect(self.playVidRes)
        # self.decodedPathInput.returnPressed.connect(self.returnDecFolderSlot)
        self.browseButton3.clicked.connect(self.browseDecFolderSlot)
        self.decodedName.returnPressed.connect(self.returnDecNameSlot)
        
        self.dispButton.clicked.connect(self.displayFile)

        self.mediaPlayer1 =  QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer1.stateChanged.connect(self.mediaStateChanged1)
        self.mediaPlayer2 =  QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer2.stateChanged.connect(self.mediaStateChanged2)
        self.mediaPlayer1.setVideoOutput(self.videoScreen1)
        self.mediaPlayer2.setVideoOutput(self.videoScreen2)

        self.encodeButton.clicked.connect(lambda: self.launchThread(1))
        self.decodeButton.clicked.connect(lambda: self.launchThread(2))
        self.helpButton.clicked.connect(self.displayHelpWindow)

        self.customButton.clicked.connect(self.dialogbox) 
        
        

    @QtCore.pyqtSlot()
    def launchThread(self,option):
        if option ==1:
            if self.decodeButton.isEnabled():
                thread = threading.Thread(target=self.Encode)
                thread.start()
            else:
                self.debugPrint("Please wait until the other process is finished")
        else:
            if self.encodeButton.isEnabled():
                thread = threading.Thread(target=self.Decode)
                thread.start()
            else:
                self.debugPrint("Please wait until the other process is finished")

    @QtCore.pyqtSlot()
    def Encode(self):
        self.codeLength = []
        fileName = self.model.getFileName()
        outputFolder = self.model.getDestFolder()
        name = self.outputName.text()
        outputPath = self.model.getDestPath()
        if self.model.isValid(fileName):
            if outputFolder==None:
                self.debugPrint("Determine the output video folder first")
            elif name=="":
                self.debugPrint("Determine the output video name first")
            else:
                self.encodeButton.setEnabled(False)
                # Kode encoding
                cap = cv2.VideoCapture(fileName) #Read the video File
                frames,frame_num,fps,width,height = self.readVideo(cap)
                orisize = (((int(width)*int(height)*24)/8)/1024)*int(frame_num)
                self.oriSize.setText("Original Video Size : %.2f KB" %(orisize))
                self.debugPrint("Encoding..........")
                
                if (self.FFTRadio.isChecked()):
                    self.k=1
                elif (self.DCTRadio.isChecked()):
                    self.k=0
                elif (self.DSTRadio.isChecked()):
                    self.k=2
                if (self.yChromRadio.isChecked()) and (self.cChromRadio.isChecked()): #Y dan CbCr pake chrom
                        self.y=0
                        self.customQTable = None
                elif (self.yLumRadio.isChecked()) and (self.cChromRadio.isChecked()): # Y Lum, CbCr chrom
                        self.y=1
                        self.customQTable = None
                elif (self.yChromRadio.isChecked()) and (self.cLumRadio.isChecked()): # YChrom, CbCr Lum
                        self.y=2
                        self.customQTable = None
                elif (self.yLumRadio.isChecked()) and (self.cLumRadio.isChecked()): # Y and CbCr Lum
                        self.y=3
                        self.customQTable = None
                elif(self.yLumRadio.isChecked()) and (self.cLumRadio.isChecked()==False) and (self.cChromRadio.isChecked()==False) : # Y Lum, CbCr Custom
                        self.y=4
                elif(self.yChromRadio.isChecked()) and (self.cLumRadio.isChecked()==False) and (self.cChromRadio.isChecked()==False) : # Y Chrom, CbCr Custom
                        self.y=5
                elif(self.cLumRadio.isChecked()) and (self.yLumRadio.isChecked()==False) and (self.yChromRadio.isChecked()==False) : # CbCr lum, Y Custom
                        self.y=6
                elif(self.cChromRadio.isChecked()) and (self.yLumRadio.isChecked()==False) and (self.yChromRadio.isChecked()==False) : # CbCr chrom, Y Custom
                        self.y=7
                else:       
                        self.y=8
            
                counter=1
                tablePath = self.model.getHuffPath()
                encodePath = self.model.getDestPath()
                f = open(encodePath, 'wb')
                f.close()

                for frame in frames :
                    length,block,self.quant=encode(frame,frame_num,fps,tablePath,encodePath,self.k,self.y,self.customQTable)
                    self.codeLength.append(length)
                    self.debugPrint('Progress = '+str(counter)+' out of '+str(frame_num))
                    counter=counter+1
                self.encodeButton.setEnabled(True)
                self.debugPrint("Done Encoding")
                size = os.path.getsize(outputPath)
                size = round((size/1024),2)
                self.encSize.setText('Encoded File Size: '+ str(size) + ' KB')
                self.debugPrint("Frame terakhir sebelum kuantisasi :\n"+str(block))
                self.textBrowser_2.append("Frame terakhir setelah kuantisasi :\n"+str(self.quant))
                    
        else:
            self.debugPrint("Source file invalid!")

    @QtCore.pyqtSlot()
    def Decode(self):
        if self.model.getDestPath() ==None or self.model.getHuffPath == None:
            self.debugPrint("Determine Source to be Decoded")
            return
        sourceFile = self.model.getDestPath()
        tablePath = self.model.getHuffPath()
        outputFolder = self.model.getDecodedFolder()
        name = self.decodedName.text()
        outputPath = self.model.getDecodedPath()
        
        if self.model.isValid(sourceFile) or self.model.isValid(tablePath):
            if outputFolder==None:
                self.debugPrint("Determine the output video folder first")
            elif name=="":
                self.debugPrint("Determine the output video name first")
            else:
                self.decodeButton.setEnabled(False)
                counter=1
                frames = []
                width,height,frame_num,fps = getDimension(tablePath)
                width = int(width)
                height = int(height)
                self.debugPrint("Width : %d" % (width))
                self.debugPrint("Height : %d" % (height))
                
                self.debugPrint("Decoding..........")
                i = 0
                with open(sourceFile,'rb') as file, open(tablePath,'r') as table:
                    while(i<int(frame_num)):
                        frame=decode(file.read(self.codeLength[i]),table,self.k,self.y,self.customQTable)                        
                        frames.append(frame)
                        self.debugPrint('Progress = '+str(counter)+' out of '+str(frame_num))
                        counter = counter+1
                        i +=1
                
                codec_id = "mp4v"
                fourcc = cv2.VideoWriter_fourcc(*codec_id)
                out = cv2.VideoWriter(outputPath, fourcc, int(fps), (width, height)) # bikin fungsi ambil row, cols
                video=frames


                for frame in video: #Jumlah frame?
                    frame_bgr = cv2.cvtColor(frame, cv2.COLOR_YCR_CB2BGR)
                    #frame = frame[0, :, :]
                    out.write(frame_bgr)
                
                self.decodeButton.setEnabled(True)
                self.debugPrint("Done Decoding")

        else:
            self.debugPrint("Compressed file or table that is about to be decoded is invalid!")
    
        

    def debugPrint( self, msg ):
        '''Print the message in the text edit at the bottom of the
        horizontal splitter.
        '''
        self.textBrowser.append( msg )
    
    def mediaStateChanged1(self, state):
        if self.mediaPlayer1.state() == QMediaPlayer.PlayingState:
            self.playButton1.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton1.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
    
    def mediaStateChanged2(self, state):
        if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
            self.playButton2.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton2.setIcon(
                    self.style().standardIcon(QStyle.SP_MediaPlay))
    
    def readVideo(self,cap):
        frames = []
        while(cap.isOpened()):
            ret,frame = cap.read() #akan dibaca frame per frame, var frame akan menyimpan nilai pembacaanya 
            if not ret:
                frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
                fps = cap.get(cv2.CAP_PROP_FPS)
                width =int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.debugPrint("Reading Video Done. Total Frame : %d" % (frame_num))
                self.debugPrint("Width : %d" % (width))
                self.debugPrint("Height : %d" % (height))
                break
            frame_ycbcr = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frames.append(frame_ycbcr)
        return frames,frame_num,fps,width,height

    

    @QtCore.pyqtSlot()
    def playVidSource(self):
        if self.mediaPlayer1.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer1.pause()
        else:
            self.mediaPlayer1.play()

    @QtCore.pyqtSlot()
    def playVidRes(self):
        filename = self.model.getDecodedPath()
        if (self.model.isValid(filename)):
            self.mediaPlayer2.setMedia(QMediaContent(QUrl.fromLocalFile(filename)))

            if self.mediaPlayer2.state() == QMediaPlayer.PlayingState:
                self.mediaPlayer2.pause()
            else:
                self.mediaPlayer2.play()
                size = os.path.getsize(filename)
                size = round((size/1024),2)
                self.decodedSize.setText('File Size: '+ str(size) + ' KB')
                        
        else:
            self.debugPrint("Video not yet created")
    

    # @QtCore.pyqtSlot()
    # def returnSourceSlot(self):
    #     pass

    # @QtCore.pyqtSlot()
    # def returnDestSlot(self):
    #     pass

    # @QtCore.pyqtSlot()
    # def returnDecFolderSlot(self):
    #     pass


    @QtCore.pyqtSlot()
    def displayFile(self):
        filename = self.model.getDestPath()
        if (self.model.isValid(filename)):
            self.textBrowser_2.setText(str(self.model.getDestContents()))
            self.textBrowser_2.append("Frame terakhir setelah kuantisasi :\n"+str(self.quant))
        else:
            self.debugPrint("File has not been made yet!")
    
    @QtCore.pyqtSlot()
    def displayHuff(self):
        filename = self.model.getHuffPath()
        if (self.model.isValid(filename)):
            with open(filename) as fin:
                fin.seek(0)
                contents = fin.read(2000-0)
            self.textBrowser_2.setText(contents)
            self.textBrowser_2.append("Frame terakhir setelah kuantisasi :\n"+str(self.quant))
        else:
            self.debugPrint("File has not been made yet!")
    
    @QtCore.pyqtSlot()
    def displayQuant(self):
        filename = self.model.getHuffPath()
        if (self.quant):
            self.textBrowser_2.setText("Frame terakhir setelah kuantisasi :\n"+str(self.quant))
        else:
            self.debugPrint("Encode First!")

    @QtCore.pyqtSlot()
    def browseSourceSlot(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "Video Files (*.mp4 *.flv *.ts *.mts *.avi);;All Files (*)",
                        options=options)
        if fileName:
            self.debugPrint( "setting source file name: " + fileName )
            self.model.setFileName( fileName )
            self.mediaPlayer1.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton1.setEnabled(True)
            self.sourceInput.setText(fileName)
            # size = os.path.getsize(self.model.getFileName())
            # size = round((size/1024),2)
            # self.SourceSize.setText('File Size: '+ str(size) + ' KB')
            
        
    # Buat nyari folder yang mau di bikinin hasil encodednya. Penamaan variabel agak ngaco
    @QtCore.pyqtSlot()
    def browseDestSlot(self):
        options = QtWidgets.QFileDialog.Options()
        foldName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if foldName:
            self.debugPrint( "setting Encoding Folder : " + foldName )
            self.model.setDestFolder( foldName ) #Bikin folder + outputname
            self.DestInput.setText( self.model.getDestFolder())

    # Return nama output encoded. Penamaan variabel agak ngaco biarin lah ahahahaha
    @QtCore.pyqtSlot()
    def returnNameSlot(self):
        name =  self.outputName.text()
        self.model.setDestPath(name)
        fileName = self.model.getDestPath()
        self.outputName.setText( fileName )
        self.dispButton.setEnabled(True)
        self.huffButton.setEnabled(True)
        self.debugPrint("Entered Encoded File Name !")
        
    
    # Pilih folder video decoded mau dibikin dimana
    @QtCore.pyqtSlot()
    def browseDecFolderSlot(self):
        options = QtWidgets.QFileDialog.Options()
        foldName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if foldName:
            self.debugPrint( "setting Destination Folder : " + foldName )
            self.model.setDecodedFolder( foldName ) #Bikin folder + outputname
            self.decodedPathInput.setText( self.model.getDecodedFolder())
            
    
    @QtCore.pyqtSlot()
    def returnDecNameSlot(self):
        self.debugPrint("Entered Output Video File Name !")
        name =  self.decodedName.text()
        self.model.setDecodedPath(name)
        fileName = self.model.getDecodedPath()
        self.playButton2.setEnabled(True)
        self.decodedName.setText(fileName)
        if self.model.isValid(fileName):
            size = os.path.getsize(fileName)
            size = round((size/1024),2)
            self.decodedSize.setText('File Size: '+ str(size) + ' KB')
        else:
            self.decodedSize.setText('File Size: Not yet created')

    def displayHelpWindow(self):
        self.myHelp = MyHelp()
        self.myHelp.show()

    def dialogbox(self):
        self.myDialog = MyDialog()
        self.myDialog.show()
        self.myDialog.okButton.clicked.connect(self.returnTable)
    
    def returnTable(self):
        table = [
            self.myDialog.tab0.text(),
            self.myDialog.tab1.text(),
            self.myDialog.tab2.text(),
            self.myDialog.tab3.text(),
            self.myDialog.tab4.text(),
            self.myDialog.tab5.text(),
            self.myDialog.tab6.text(),
            self.myDialog.tab7.text(),
            self.myDialog.tab8.text(),
            self.myDialog.tab9.text(),
            self.myDialog.tab10.text(),
            self.myDialog.tab11.text(),
            self.myDialog.tab12.text(),
            self.myDialog.tab13.text(),
            self.myDialog.tab14.text(),
            self.myDialog.tab15.text(),
            self.myDialog.tab16.text(),
            self.myDialog.tab17.text(),
            self.myDialog.tab18.text(),
            self.myDialog.tab19.text(),
            self.myDialog.tab20.text(),
            self.myDialog.tab21.text(),
            self.myDialog.tab22.text(),
            self.myDialog.tab23.text(),
            self.myDialog.tab24.text(),
            self.myDialog.tab25.text(),
            self.myDialog.tab26.text(),
            self.myDialog.tab27.text(),
            self.myDialog.tab28.text(),
            self.myDialog.tab29.text(),
            self.myDialog.tab30.text(),
            self.myDialog.tab31.text(),
            self.myDialog.tab32.text(),
            self.myDialog.tab33.text(),
            self.myDialog.tab34.text(),
            self.myDialog.tab35.text(),
            self.myDialog.tab36.text(),
            self.myDialog.tab37.text(),
            self.myDialog.tab38.text(),
            self.myDialog.tab39.text(),
            self.myDialog.tab40.text(),
            self.myDialog.tab41.text(),
            self.myDialog.tab42.text(),
            self.myDialog.tab43.text(),
            self.myDialog.tab44.text(),
            self.myDialog.tab45.text(),
            self.myDialog.tab46.text(),
            self.myDialog.tab47.text(),
            self.myDialog.tab48.text(),
            self.myDialog.tab49.text(),
            self.myDialog.tab50.text(),
            self.myDialog.tab51.text(),
            self.myDialog.tab52.text(),
            self.myDialog.tab53.text(),
            self.myDialog.tab54.text(),
            self.myDialog.tab55.text(),
            self.myDialog.tab56.text(),
            self.myDialog.tab57.text(),
            self.myDialog.tab58.text(),
            self.myDialog.tab59.text(),
            self.myDialog.tab60.text(),
            self.myDialog.tab61.text(),
            self.myDialog.tab62.text(),
            self.myDialog.tab63.text(),
            
        ]

        if '' in table or 0 in table:
            self.debugPrint("Please fill all table cells with value more than 0")
            return
        try:
            table=[int(x) for x in table]
        except:
            self.debugPrint("Please fill all table with numbers")
            return
        
        self.customQTable = zigzag_to_block(table)
        self.debugPrint("Custom Quantization Table has been set")
        self.debugPrint("Custom Quantization table : \n"+ str(self.customQTable))

        self.yChromRadio.setAutoExclusive(False)
        self.yLumRadio.setAutoExclusive(False)
        self.cChromRadio.setAutoExclusive(False)
        self.cLumRadio.setAutoExclusive(False)
        self.yChromRadio.setChecked(False)
        self.yLumRadio.setChecked(False)
        self.cChromRadio.setChecked(False)
        self.cLumRadio.setChecked(False)
        self.yChromRadio.setAutoExclusive(True)
        self.yLumRadio.setAutoExclusive(True)
        self.cChromRadio.setAutoExclusive(True)
        self.cLumRadio.setAutoExclusive(True)

        self.myDialog.close()
        



class MyDialog(QDialog,Ui_Form):
    def __init__(self,parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

class MyHelp(QDialog,Ui_Help):
    def __init__(self,parent=None):
        super(MyHelp, self).__init__(parent)
        self.setupUi(self)
 

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

main()