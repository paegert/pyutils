'''

A very simple logfile class

@package  logfile
@author   mpaegert
@version  \$Revision: 1.1 $
@date     \$Date: 2012/06/25 18:31:03 $

@author: map
Created on Feb 24, 2012

$Log: logfile.py,v $
Revision 1.1  2012/06/25 18:31:03  paegerm
*** empty log message ***

Initial Revision
'''

class Logfile(object):
    '''
    A simple log-file class for use with long running code in background tasks.
    The log-file is opened, a message added and closed immediately, so that 
    entries are visible even if nohup buffers normal output and files kept
    open are buffered by the operating system.
    
    Public Attributes:
    
    mirror - mirrors any message to console output via print if True
    '''


    def __init__(self, filename = 'logfile.txt', createflag = True,
                 mirrorflag = True):
        '''
        Initialize logfile, create on demand
        
        @param  filename    name of the file (default = logfile.txt)
        @param  createflag  True (default): create new file, overwrite old one
                            False (append only)
        @param  mirrorflag  True (default): print message to console as well
                            False: no output to console
        '''
        self._fname  = filename
        self._create = createflag
        if self._fname == '':
            self._fname = None
            self._create = False
        if self._fname != None and self._create == True:
            lf = open(self._fname, 'w')
            lf.close()
        self.mirror = mirrorflag
        
        
    def write(self, message = ''):
        if (self.mirror == True):
            print message
        if (self._fname != None) and (len(self._fname.strip()) > 0):
            lf = open(self._fname, 'a')
            lf.write(message + '\n')
            lf.close()
        return
    
    def writemany(self, messages):
        if messages == None:
            return
        if (self._fname != None) and (len(self._fname.strip()) > 0):
            lf = open(self._fname, 'a')
            for msg in messages:
                if self.mirror == True:
                    print msg
                lf.write(msg + '\n')
            lf.close()
            
    
if __name__ == '__main__':
    test = Logfile('testlog.txt')
    test.write('initial log')
    test.write()
    test.write('Empty line above this one?')
    msglist = []
    msglist.append('first line')
    msglist.append('second line')
    test.writemany(msglist)
    
    test2 = Logfile('testlog.txt', False, False)
    test2.write('Second object only appending, this should not appear on screen')
    
    test3 = Logfile(None, True, True)
    test3.write('This should be console output only')
    
    print 'Done'
    
    
