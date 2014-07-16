'''
Created on 7 juil. 2014

@author: pierre
'''
from qgis.gui import QgsMapTool
from qgis._core import QgsPoint


#Define a Custom PointTool Class that inherit from QgsMaptool
class PointTool(QgsMapTool):   
    def __init__(self, canvas):
        QgsMapTool.__init__(self, canvas)
        self.canvas = canvas    

    def canvasPressEvent(self, event):
        pass

    def canvasMoveEvent(self, event):
        #Uncomment Activate point Hovering
        #x = event.pos().x()
        #y = event.pos().y()
        #point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        pass

    def canvasReleaseEvent(self, event):
        #Get the click
        x = event.pos().x()
        y = event.pos().y()

        point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
        self.p = QgsPoint(point[0], point[1])

        print point, self.p
        print self.p.wellKnownText()

    def activate(self):
        pass

    def deactivate(self):
        pass

    def isZoomTool(self):
        return False

    def isTransient(self):
        return False

    def isEditTool(self):
        return True
    
    def getPoint(self):
        return self.p