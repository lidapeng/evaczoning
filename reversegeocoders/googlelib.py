import arcpy
from arcpy import env
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import string, os, sys, httplib, urllib2
import StringIO,csv,codecs
from xml.dom import minidom

# store the results from Google reverse geocoding service
class GoogleResult:

    def __init__(self):
        self.type = ""
        self.name = ""
        self.latitude = ""
        self.longitude = ""
        self.geonameID = ""
        self.locType = ""        
    def setTyponymName(self,name):
        self.typonymName = name
    def setName(self,name):
        self.name = name
    def setLat(self,lat):
        self.latitude = lat
    def setLng(self,lng):
        self.longitude = lng
    def setGeonameID(self,id):
        self.geonameID = id    
    def setLocType(self,locType):
        self.locType = locType   
    def setInit(self):
        self.typonymName = ""
        self.name = ""
        self.latitude = ""
        self.longitude=""
        self.geonameID = ""

class GoogleReverseGeocoder():
    
    def reverseGeocode(self,lat,lon):
        try:
            result = GoogleResult()
            googleURL = r"http://maps.googleapis.com/maps/api/geocode/xml?latlng=" + str(lat) + r"," + str(lon) + r"&sensor=false"
            s = urllib2.urlopen(googleURL)
            xmldoc = minidom.parse(s)
            loc = xmldoc.getElementsByTagName('result')
            
            elemType = loc[0].getElementsByTagName('type')[0]
            result.setTyponymName(elemType.firstChild.nodeValue) 
            
            elemAddr = loc[0].getElementsByTagName('formatted_address')[0]
            result.setName(elemAddr.firstChild.nodeValue)
            
            elemLoc =  loc[0].getElementsByTagName('location')[0]
            
            lat = elemLoc.getElementsByTagName('lat')[0]
            lon = elemLoc.getElementsByTagName('lng')[0]
            
            result.setLat(lat.firstChild.nodeValue)
            result.setLng(lon.firstChild.nodeValue)
            
            elemGeometry = loc[0].getElementsByTagName('geometry')[0]
            locType = elemGeometry.getElementsByTagName('location_type')[0]
            result.setLocType(locType.firstChild.nodeValue)
            
            return result
        except Exception as e:
            print e.message
class GoogleHandler(ContentHandler):
    typonymName = ""
    name = ""
    latitude = ""
    longitude = ""
    geonameID = ""
    istyponymName = False
    isname = False
    isLat = False
    isLng = False
    isgeonameID = False
##    geonameArray = GeoName()
#     geoname = GeoName()
    def startElement(self, name, attrs):
        if (name == "geoname"):
            pass
        if (name == "toponymName") :
            self.istyponymName = True
        if (name == "name") :
            self.isname = True
        if (name == "lat"):
            self.isLat = True
        if (name == "lng"):
            self.isLng = True
        if (name == "geonameId"):
            self.isgeonameID = True
    def characters (self, ch):
        if self.istyponymName:
            self.typonymName += ch
        if self.isname:
            self.name += ch
        if self.isLat:
            self.latitude +=ch
        if self.isLng:
            self.longitude += ch
        if self.isgeonameID:
            self.geonameID += ch

    def endElement(self,name):
        if (name == "toponymName") :
            print "%s" % self.typonymName
            self.istyponymName = False
            self.geoname.setTyponymName(self.typonymName)
            self.typonymName = ""
        if (name == "name") :
            print "%s" % self.name
            self.isname = False
            self.geoname.setName(self.name)
            self.name = ""
        if (name == "lat"):
            print "%s" % self.latitude
            self.isLat = False
            self.geoname.setLat(self.latitude)

            self.latitude = ""
        if (name == "lng"):
            print "%s" % self.longitude
            self.isLng = False
            self.geoname.setLng(self.longitude)

            self.longitude = ""
        if (name == "geonameId"):
            print "%s" % self.geonameID
            self.isgeonameID = False
            self.geoname.setGeonameID(self.geonameID)

            self.geonameID = ""
        if (name == "geoname"):
            #csvwriter.writerow(["Name","Address","Telephone","Fax","E-mail","Others"])  
            mylist = []
            mylist.append(self.geoname.typonymName)
            mylist.append(self.geoname.name)
            mylist.append(self.geoname.latitude)
            mylist.append(self.geoname.longitude)
            mylist.append(self.geoname.geonameID)
            
            print "**************"
            print len(mylist)
