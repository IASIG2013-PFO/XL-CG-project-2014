'''
Created on 10 juil. 2014

@author: pierre
'''

import getpass
import os
import shelve
import time


class OProject(object):

    '''
    This class is a object container that Records the Project configuration
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.project_name = None
        self.project_path = None
        self.ZC = None
        self.user = None
        self.ZR = []

        #======================================================================
        # self.user = getpass.getuser()
        # self.creationDate = time.localtime()
        #======================================================================

        #shelve_project_parameters = shelve.open('shelf_PP.db')

        #======================================================================
        # construct the shelve:
        # try:
        #     shelve_project_parameters['general_info'] = {
        #         'project_name': "", 'project_path': "", 'project_date': self.creationDate, 'project_user': self.user}
        # finally:
        #     shelve_project_parameters.close()
        #======================================================================

    def setProjectPath(self, project_path):
        '''
        Path string to Project Folder
        '''
        self.project_path = project_path

    def setProjectName(self, project_name):
        '''
        project name
        '''
        self.project_name = project_name

    def setZC(self, zone_cliente):
        '''
        WKB representation of the client zone
        '''
        self.client_zone = zone_cliente

    def setZR(self, zone_reconciliation):
        '''
        ZR is an objet that contain:
            - Purpose of the ZR (string)
            - List of table related to the ZR
            - User owner of this ZR
            - Date
        '''
        self.ZR.append(zone_reconciliation)

    def writeProjectShelf(self):

        # Test if the shelf is already open/needs to be open

        shelve_project_parameters = shelve.open('shelf_PP.db')

        if not self.user:
            self.user = getpass.getuser()
            self.creationDate = time.localtime()

        # Construct the shelve:
        try:
            shelve_project_parameters['object'] = self
            shelve_project_parameters['general_info'] = {
                'project_name': self.project_name, 'project_path': self.project_path, 'project_date': self.creationDate, 'project_user': self.user}
            shelve_project_parameters['geographic_info'] = {
                'ZC': self.ZC, 'ZR': self.ZR}
        finally:
            shelve_project_parameters.close()
