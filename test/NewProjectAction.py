'''
Created on 11 juil. 2014

@author: pierre
'''

from PyQt4.Qt import QFrame, QGridLayout, QAction, QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import QTabWidget, QColor, QMainWindow, QFileDialog
from __builtin__ import list
import os
from qgis.core import *
from qgis.gui import *
import shelve
import time

import global_mod
from test.URI_Builder import URI_Builder
from test.resources import *
from test.ui_main_window import Ui_MainWindow
from test.ui_start_tab_menu import Ui_TabWidget


class NewProjectAction(object):

    '''
    this class encapsulate all software/user interaction required to build a Projet
    '''
    #-------------------------------------------------------------------------
    #-------------------------ALL CONNECTION DEFINED HEREAFTER----------------
    #-------------------------------------------------------------------------

    def setupAction_newProject(self):
        """
        Give action to the tabulated window
        Connect Signals -> Slots
        """
        #======================================================================
        # Project Tab  (path; date; general info)
        #======================================================================
        self.connect(self.btnSelectPath, SIGNAL("clicked()"), self.browseDir)
        self.connect(
            self.editProjectName, SIGNAL("editingFinished()"), self.setProjectName)
        self.connect(
            self.btnProjectValidation, SIGNAL("clicked()"), self.writeProjectToFSI)
        self.connect(
            self.btnExtraction, SIGNAL("clicked()"), self.showCanvas)

    #-------------------------------------------------------------------------
    #-------------------------ALL SLOT ARE DEFINE BELOW-----------------------
    #-------------------------------------------------------------------------

    def browseDir(self):
        # Caption dirname in local variable
        dirname = QFileDialog.getExistingDirectory(self, caption=QString())
        #======================================================================
        # Write Project Directory
        #======================================================================
        # directory name does not exist; empty string;...
        if dirname.isEmpty():
            return
        else:
            self.editDirName.setText(dirname)
        # update oproject
        # pass the project path to the oproject
        global_mod.oproject.setProjectPath(str(self.editDirName.text()))

    def setProjectName(self):
        # update oproject
        # pass the project name to the oproject
        global_mod.oproject.setProjectName(str(self.editProjectName.text()))

    def writeProjectToFSI(self):
        # Build a generic/OS independant path
        # Transyping required from QString to regular python String
        path = os.path.join(
            str(self.editDirName.text()), str(self.editProjectName.text()))
        path_archive = os.path.join(path, "archive")
        path_current = os.path.join(path, "current")
        # Write directory with exception management
        #------------------------------------------------------------------ try:
        #---------------------------------------------------- os.mkdir(path)
        #------------------------------------------------------- except OSError:
        # ------------------------------------------ # TODO: error Management
        #---------------------------------------------------- print('error')
        #------------------------------------------------------------ return
        #----------------------------------------------------------------- else:

        os.mkdir(path)
        os.mkdir(path_archive)
        os.mkdir(path_current)

        # Change diectory
        os.chdir(path_current)
        self.extract2Disk()

        # Shelve the project information
        #oproject = OProject()
        global_mod.oproject.writeProjectShelf()

        #======================================================================
        # Test shelve reload
        # d = shelve.open('/home/pierre/Bureau/erer/shelf_PP.db')
        # obj = d['object']
        #======================================================================

        # test saving QGIS project view
        qproject = QgsProject.instance()
        path_proj = os.path.join(path, "XLproject.qgs")

        qproject.setFileName(path_proj)
        qproject.write()

    def extract2Disk(self):

        # write a SQLITE DB out
        layer = self.select_a_postgis_layer(URI_Builder.static_testing_uri())

        # Write a SQLITE/SPATIALITE FILE
        # create an instance of vector file writer, which will create the vector file.
        # Arguments:
        # 1. QgsVectorLayer to write
        # 2. path to new file (will fail if exists already)
        # 3. encoding of the attributes
        # 4. layer's spatial reference (instance of
        #    QgsCoordinateReferenceSystem) - optional
        # 5. driver name for the output file
        # return static WriterError

        error = QgsVectorFileWriter.writeAsVectorFormat(layer, "my_shapes2.sqlite",
                                                        "utf-8", None, "SQLite")
        if error == QgsVectorFileWriter.NoError:
            print "success!"

    def showCanvas(self):
        print "SHOW CANVAS"
        self.map_canvas = QgsMapCanvas()
        self.map_canvas.setCanvasColor(QColor(255, 255, 255))
        self.gridLayout_2.addWidget(self.map_canvas)

        layer = QgsVectorLayer(
            URI_Builder.static_testing_uri(), "test", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])

    #-------------------------------------------------------------------------
    #-------------------------GETTERS - SETTERS-------------------------------
    #-------------------------------------------------------------------------

    def getProjectName(self):
        pass

    def getProjetPath(self):
        pass
