'''
Created on 10 juil. 2014

@author: pierre
'''
import getpass
import time
import OProject


class ZoneReconciliation(object):

    '''
    This class provide a simple encapsulation to decribe a ZR

    '''

    def __init__(self, operation, ZR, oproject, tablelist=[]):
        '''
        Constructor
        '''
        self.operation = operation
        self.tablelist = tablelist
        self.user = getpass.getuser()
        self.datecreation = time.localtime()
        self.oprojectname = oproject.name
