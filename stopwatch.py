'''
A very simple stopwatch class

@package  txt2sqlite
@author   mpaegert
@version  \$Revision: 1.1 $
@date     \$Date: 2012/02/01 18:44:38 $
'''

import time

class Stopwatch(object):
    '''
    A very simple stopwatch class
    
    Attributes
    
    elapsed - time elapsed
    '''

    def __init__(self):
        '''
        Constructor: setting start and stop time
        '''
        self.__class__ = Stopwatch
        self._stop  = None
        self.elapsed = 0.0
        self._start = time.time()
        
    def cont(self):
        '''
        restarting the watch, keeping elapsed time 
        '''
        self._stop  = None
        self._start = time.time()

    def start(self):
        '''
        starting the watch, nulling elapsed time
        '''
        self.elapsed = 0.0
        self.cont()
        
    def stop(self):
        '''
        stopping the watch, computing time elapsed
        @return: elapsed time
        '''
        self._stop  = time.time()
        self.elapsed = self.elapsed + (self._stop - self._start)
        return self.elapsed
    
    def stopintermediate(self):
        '''
        Stopping and returning intermediate time
        @return: elapsed time since last cont() or start()
        '''
        self.stop()
        return self._stop - self._start
        
    def __str__(self):
        '''
        @return: formatted string of elapsed time in seconds
        '''
        return 'elapsed time = ' + str(self.elapsed) + ' sec'


if __name__ == '__main__':
    watch = Stopwatch()
    print 'started with creation, waiting some time'
    time.sleep(1.5)
    watch.stop()
    print "time = ", watch.elapsed
    print watch
    
    print ""
    print "restarting"
    watch.cont()
    time.sleep(1)
    print 'intermediate time = ', watch.stopintermediate()
    print watch
    print 'done'
    