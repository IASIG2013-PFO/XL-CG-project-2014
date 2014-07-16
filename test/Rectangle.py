'''
Created on 7 juil. 2014

@author: pierre
'''

# Qt4 required class import
from PyQt4 import *
from PyQt4.Qt import SIGNAL, QColor
from PyQt4.QtGui import *
from qgis._core import *
from qgis.gui import *
from signal import signal


# Qgis Required class import
class RectangleMapTool(QgsMapToolEmitPoint):

    def __init__(self, canvas):
        '''
        Embed a custom test signal emitted at deactivation
        '''
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.rubberBand = QgsRubberBand(self.canvas, QGis.Polygon)
        # self.rubberBand.setColor(QColor().cyan())
        self.rubberBand.setWidth(1)
        self.reset()
        # Test Custom Signal
        # Connect "deactivated" signal to printDeactivated public method
        self.connect(self, SIGNAL("deactivated"),
                     self.printDeactivated)

    def reset(self):
        self.startPoint = self.endPoint = None
        self.isEmittingPoint = False
        self.rubberBand.reset(QGis.Polygon)

    def canvasPressEvent(self, e):
        self.startPoint = self.toMapCoordinates(e.pos())
        self.endPoint = self.startPoint
        self.isEmittingPoint = True
        self.showRect(self.startPoint, self.endPoint)

    def canvasReleaseEvent(self, e):
        self.isEmittingPoint = False
        r = self.rectangle()
        if r is not None:
            print "Rectangle:", r.xMin(), r.yMin(), r.xMax(), r.yMax()

    def canvasMoveEvent(self, e):
        if not self.isEmittingPoint:
            return

        self.endPoint = self.toMapCoordinates(e.pos())
        self.showRect(self.startPoint, self.endPoint)

    def showRect(self, startPoint, endPoint):
        self.rubberBand.reset(QGis.Polygon)
        if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
            return

        point1 = QgsPoint(startPoint.x(), startPoint.y())
        point2 = QgsPoint(startPoint.x(), endPoint.y())
        point3 = QgsPoint(endPoint.x(), endPoint.y())
        point4 = QgsPoint(endPoint.x(), startPoint.y())

        self.rubberBand.addPoint(point1, False)
        self.rubberBand.addPoint(point2, False)
        self.rubberBand.addPoint(point3, False)
        self.rubberBand.addPoint(point4, True)  # true to update canvas
        self.rubberBand.show()

    def rectangle(self):
        if self.startPoint is None or self.endPoint is None:
            return None
        elif self.startPoint.x() == self.endPoint.x() or self.startPoint.y() == \
                self.endPoint.y():
            return None

        return QgsRectangle(self.startPoint, self.endPoint)

    def deactivate(self):
        QgsMapTool.deactivate(self)
        # emit dummy "deactivated signal" when deactivate()
        self.emit(SIGNAL("deactivated"))

    def printDeactivated(self):
        print "deactivated"

    @property
    def x_origin(self):
        r = self.rectangle()
        return r.xMaximum()

    @x_origin.setter
    def x_origin(self, x_new):
        r = self.rectangle()
        a = r.xMaximum()
        a = 25
        print a

####################################################################
if __name__ == "__main__":
    # create Qt application
    app = QApplication([])
    # set up QGIS environment variables
    QgsApplication.setPrefixPath('/usr', True)
    QgsApplication.initQgis()

    map_canvas = QgsMapCanvas()
    r = RectangleMapTool(map_canvas)

    r.deactivate()
