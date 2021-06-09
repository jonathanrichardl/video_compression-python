class Model:
    def __init__( self ):
        '''
        Initializes the two members the class holds:
        the file name and its contents.
        '''
        self.fileName = None
        self.destFolder = None
        self.destFilePath = None
        self.destContents = ""
        self.decFolder = None
        self.decFilePath = None
        self.destName = ''
        self.tablePath = None
        

    def isValid( self, fileName ):
        '''
        returns True if the file exists and can be
        opened.  Returns False otherwise.
        '''
        try: 
            file = open( fileName, 'r' )
            file.close()
            return True
        except:
            return False

    def setFileName( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        if self.isValid( fileName ):
            self.fileName = fileName
            # self.fileContents = open( fileName, 'r' ).read()
        else:
            # self.fileContents = ""
            self.fileName = ""
    
    def getFileName( self ):
            '''
            Returns the name of the file name member.
            '''
            return self.fileName

############### Ngurus path dan content dri file encoded
    def setDestFolder( self, fileName ):
        '''
        sets the member fileName to the value of the argument
        if the file exists.  Otherwise resets both the filename
        and file contents members.
        '''
        self.destFolder = fileName
    
    def setDestPath(self,name):
        self.destName = name
        self.destFilePath = self.destFolder+"/"+ name+".bin"

    def getDestFolder( self ):
            '''
            Returns the name of the file name member.
            '''
            return self.destFolder
    
    

    def getDestPath(self):
        return self.destFilePath

    def getDestContents(self):
        with open(self.destFilePath,'rb') as fin:
                fin.seek(0)
                self.destContents = fin.read(2000-0)
            
        return self.destContents
###############################################################################  

    def getHuffPath(self):
        self.tablePath = self.destFolder +"/" +self.destName+"-table.txt"
        return self.tablePath

################### Output folder path routing 
    def setDecodedFolder(self,foldName):
        self.decFolder = foldName

    def setDecodedPath(self,name):
        self.decFilePath = self.decFolder+"/"+ name+".mp4"
    
    def getDecodedFolder( self ):
        '''
        Returns the name of the file name member.
        '''
        return self.decFolder

    def getDecodedPath(self):
        return self.decFilePath

###############################################################################  

    def writeDoc( self, text ):
        '''
        Writes the string that is passed as argument to a
        a text file with name equal to the name of the file
        that was read, plus the suffix ".bak"
        '''
        if self.isValid( self.fileName ):
            fileName = self.fileName + ".bak"
            file = open( fileName, 'w' )
            file.write( text )
            file.close()