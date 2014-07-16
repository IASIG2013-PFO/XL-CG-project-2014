from PyQt4.QtGui import QApplication
from qgis.core import QgsApplication

from test.URI_Builder import URI_Builder
from test.ourmainwindow import OurMainWindow


# create Qt application
app = QApplication([])
# set up QGIS environment variables
e = QgsApplication.setPrefixPath('/usr', True)
e = QgsApplication.initQgis()

# set Database connection
db_connection = URI_Builder()


# set the main window and show its
mw = OurMainWindow(db_connection)
mw.show()
#mw = OurMainWindow(db_connection)
# mw.show()

# Launch Application
app.exec_()

# "delete" our main window
mw = None
# clean up QGIS
QgsApplication.exitQgis()
