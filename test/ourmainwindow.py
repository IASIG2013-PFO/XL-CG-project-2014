
from PyQt4.Qt import QFrame, QGridLayout, QAction, QIcon
from PyQt4.QtCore import *
from PyQt4.QtGui import QTabWidget, QColor, QMainWindow, QFileDialog
from __builtin__ import list
import os
from qgis.core import *
from qgis.gui import *

from test.NewProjectAction import NewProjectAction
from test.resources import *
from test.ui_main_window import Ui_MainWindow
from test.ui_start_tab_menu import Ui_TabWidget


class OurMainWindow(QMainWindow, Ui_MainWindow):

    '''
    This class generate a QMainWindow that represent our main Window
    Inherit From QMainWindow - PyQT4
    Inherit from our custom class Ui_MainWindow that construct our custom tabulated window.
    '''

    def __init__(self, db_connection,  parent=None):

        self.pointList = list()
        self.selectionRectangle = QgsRectangle()
        self.connection = db_connection
        #======================================================================
        # QT main window constructor
        # Super Constuctor for our Main Windows; the Parent window
        #======================================================================
        super(OurMainWindow, self).__init__(parent)
        #======================================================================
        # SetupUi from ui_main_window
        # Build the Main windows apparence and layout
        #======================================================================
        self.setupUi(self)

        #======================================================================
        # Create and add Child Widgets:
        # 1 - Tabulation
        #======================================================================
        self.our_tab_view = OurTabWiew(self, self.connection)
        self.formLayout.addChildWidget(self.our_tab_view)

        #======================================================================
        # Give Action to the main windows
        #======================================================================
        self.setupAction_main()

    def setupAction_main(self):
        """
        Give action to the main window
        Connect Signals -> Slots
        """

        # setup action(s)
        self.zoomin_action = QAction(
            QIcon(":/ourapp/zoomin_icon"),
            "Zoom In",
            self)

        self.zoomout_action = QAction(
            QIcon(":/ourapp/zoomout_icon"),
            "Zoom Out",
            self)

        self.pan_action = QAction(
            QIcon(":/ourapp/pan_icon"),
            "Pan",
            self)

        self.clickPoint_action = QAction(
            QIcon(":/ourapp/rectangle_icon"),
            "Click Point",
            self)

        # create toolbar
        self.toolbar = self.addToolBar("Map Tools")
        self.toolbar.addAction(self.zoomin_action)
        self.toolbar.addAction(self.zoomout_action)
        self.toolbar.addAction(self.pan_action)
        self.toolbar.addAction(self.clickPoint_action)

        # connect the tool(s)
        self.zoomin_action.triggered.connect(self.zoom_in)
        self.zoomout_action.triggered.connect(self.zoom_out)
        self.pan_action.triggered.connect(self.pan)
        self.clickPoint_action.triggered.connect(self.clickPoint)

        # create the map tool(s)
        self.tool_zoomin = QgsMapToolZoom(
            self.our_tab_view.getTabMapCanvas(), False)
        self.tool_zoomout = QgsMapToolZoom(
            self.our_tab_view.getTabMapCanvas(), True)
        self.tool_pan = QgsMapToolPan(self.our_tab_view.getTabMapCanvas())

        # self.tool_clickPoint = QgsMapToolEmitPoint(self.map_canvas)
        self.tool_clickPoint = QgsMapToolEmitPoint(
            self.our_tab_view.getTabMapCanvas())
        # self.tool_clickPoint.canvasClicked.connect(self.clicked)
        # self.tool_clickPoint.canvasClicked.connect(self.setRectangle)
        self.tool_clickPoint.canvasClicked.connect(self.selectFromRectangle)

    def zoom_in(self):
        self.our_tab_view.getTabMapCanvas().setMapTool(self.tool_zoomin)

    def zoom_out(self):
        self.our_tab_view.getTabMapCanvas().setMapTool(self.tool_zoomout)

    def pan(self):
        self.our_tab_view.getTabMapCanvas().setMapTool(self.tool_pan)

    def clickPoint(self):
        self.our_tab_view.getTabMapCanvas().setMapTool(self.tool_clickPoint)

    def pickPoint(self):
        self.tool_clickPoint.canvasClicked.connect(self.addAndSelect)

    def clicked(self, point, button):

        print point

    def setRectangle(self, point, button):

        if (len(self.pointList) < 2):
            # print "ajouter un point"
            self.pointList.append(QgsPoint(point))
            print len(self.pointList)

        if (len(self.pointList) == 2):
            selection_rectangle = QgsRectangle(
                self.pointList[0], self.pointList[1])
            # print selection_rectangle.asWktCoordinates(),
            # selection_rectangle.asPolygon()
            print selection_rectangle.width()
            self.pointList = list()
            # True = a polygon
            r = QgsRubberBand(self.our_tab_view.getTabMapCanvas(), True)
            r.setWidth(3)

            r.setToGeometry(QgsGeometry.fromRect(selection_rectangle), None)
            return selection_rectangle

    def selectFromRectangle(self, point, button):

        # define rectangle
        select_rect = self.setRectangle(point, button)
        if (select_rect != None):
            # check rectangle
            print select_rect.asWktCoordinates()
            # get the current layer
            current_layer = self.our_tab_view.getTabMapCanvas().layer(0)
            print current_layer.name()
            current_layer.select(select_rect, True)
            # destruct QgsRectange used for selection
            del select_rect
            print "destructed"


class OurTabWiew(QTabWidget,  Ui_TabWidget, NewProjectAction):

    '''
    This class generate a QTab Widget
    Inherit From QtabWidget - PyQT4
    Inherit from our custom class -Ui_Tabwidget that construct our custom tabulated window.
    '''

    def __init__(self, parent, db_connection):

        #======================================================================
        # QT Tab view constructor
        # Super Constuctor for our Tabulated Windows; CHILD of Top parent
        #======================================================================
        super(OurTabWiew, self).__init__(parent)
        #======================================================================
        # SetupUi from ui_Start_tab_menu
        # Build the windows apparence and layout
        #======================================================================
        self.setupUi(self)

        self.setupAction_newProject()
        #======================================================================
        # Instanciate a Qgis map canvas and pass it to the main windows
        #======================================================================
        self.map_canvas = QgsMapCanvas()
        self.map_canvas2 = QgsMapCanvas()

        self.map_canvas.setCanvasColor(QColor(255, 255, 255))
        self.map_canvas2.setCanvasColor(QColor(255, 255, 255))

        self.gridLayout.addWidget(self.map_canvas)
        self.gridLayout_2.addWidget(self.map_canvas2)

        # self.add_postgis_layer(uri.uri())
        self.add_postgis_layer(db_connection.getDBpath())
        self.map_canvas.zoomToFullExtent()
        self.map_canvas2.zoomToFullExtent()

        # write a SQLITE DB out
        layer = self.select_a_postgis_layer(db_connection.getDBpath())

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

    # Add an OGR (*.shp) Layer
    def add_ogr_layer(self, path):
        (name, ext) = os.path.basename(path).split('.')
        layer = QgsVectorLayer(path, name, 'ogr')

        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])

    # Add a layer from Postgis geometry
    def add_postgis_layer(self, uri_path):
        layer = QgsVectorLayer(uri_path, "couche1", "postgres")
        QgsMapLayerRegistry.instance().addMapLayer(layer)
        canvas_layer = QgsMapCanvasLayer(layer)
        self.map_canvas.setLayerSet([canvas_layer])
        self.map_canvas2.setLayerSet([canvas_layer])

    def select_a_postgis_layer(self, uri_path):
        layer = QgsVectorLayer(uri_path, "test", "postgres")
        return layer

    def getTabMapCanvas(self):
        return self.map_canvas
