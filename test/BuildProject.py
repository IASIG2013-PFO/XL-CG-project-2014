'''
Created on 9 juil. 2014

@author: pierre
'''


class BuildProjet(object):

    '''
    This class perform a geographical selection over the database and save each tables as individual SQLITE files
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
