'''
Created on 4 juil. 2014

@author: pierre
'''
import getpass
from qgis.core import QgsDataSourceURI


class URI_Builder(object):

    '''
    This Class build an URI required by the QgsVectorLayer(uri, name, provider) to make a connection on a  database
    User is defaulted to getpass.getuser() ( equivalent to os.getlogin() - work for both linux and windows platforms)
    '''

    uri = QgsDataSourceURI()

    def __init__(self, host="localhost", port="5432", bd="stage", user=getpass.getuser(), schema="public", table="epci", champ="geometrie", *args):
        '''
        Build an URI
        Set a connection 
        Set a DB path to a specific Schema->Tabel->Field
        '''
        self.uri.setConnection(host, port, bd, user, "")

        #self.uri.setConnection(host, port, bd, user, "1969_Rhodes")

        # SQL INJECTION - test de selection geographique par polygone
        polygone = "POLYGON((355900 6330300, 455900 6330300,455900 6230300,355900 6230300, 355900 6330300  ))"
        asql = "ST_WITHIN(ST_CENTROID(geometrie), ST_GeomFromText('POLYGON((355900 6430300, 455900 6430300,455900 6230300,355900 6230300, 355900 6430300  ))', 2154) )"

        # POLYGON((355900 6330300, 455900 6330300,455900 6230300,355900
        # 6230300, 355900 6330300  ))

        self.uri.setDataSource(schema, table, champ, asql)

    def getUri(self):
        '''
        Return a connection
        '''
        return self.uri

    def getDBpath(self):
        '''
        Return a DBpath
        '''
        return self.uri.uri()

    @staticmethod
    def static_testing_uri():
        host = "localhost"
        port = "5432"
        bd = "stage"
        user = getpass.getuser()
        schema = "public"
        table = "epci"
        champ = "geometrie"
        polygone = "POLYGON((355900 6330300, 455900 6330300,455900 6230300,355900 6230300, 355900 6330300  ))"
        asql = "ST_WITHIN(ST_CENTROID(geometrie), ST_GeomFromText('POLYGON((355900 6430300, 455900 6430300,455900 6230300,355900 6230300, 355900 6430300  ))', 2154) )"

        uri = QgsDataSourceURI()
        uri.setDataSource(schema, table, champ, asql)
        uri.setConnection(host, port, bd, user, "")
        return uri.uri()
