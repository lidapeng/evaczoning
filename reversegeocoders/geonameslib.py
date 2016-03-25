
from xml.sax.handler import ContentHandler
import string, os, sys, httplib, urllib2
import StringIO,csv,codecs
from xml.dom import minidom

class GeonamesResult:

    def __init__(self):
        self.typonymName = ""
        self.name = ""
        self.latitude = ""
        self.longitude = ""
        self.geonameID = ""
        self.distance = "" 
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
    def setDistance(self,dist):
        self.distance = dist


class GeonamesReverseGeocoder():
    
    def reverseGeocode(self,lat,lon):
        try:
            result = GeonamesResult()
            geonamesURL = r"http://api.geonames.org/findNearbyPlaceName?lat=" + str(lat) + r"&lng=" + str(lon) + r"&username=edwarde"
            s = urllib2.urlopen(geonamesURL)
            xmldoc = minidom.parse(s)
    #         print geonamesURL
            elemGeoname = xmldoc.getElementsByTagName('geoname')[0]
            
            elemType = elemGeoname.getElementsByTagName('toponymName')[0]
            result.setTyponymName(elemType.firstChild.nodeValue)
            
            elemName = elemGeoname.getElementsByTagName('name')[0]
            result.setName(elemName.firstChild.nodeValue)
            
            lat = elemGeoname.getElementsByTagName('lat')[0]
            lon = elemGeoname.getElementsByTagName('lng')[0]
            result.setLat(lat.firstChild.nodeValue)
            result.setLng(lon.firstChild.nodeValue)
            
            elemID = elemGeoname.getElementsByTagName('geonameId')[0]
            result.setGeonameID(elemID.firstChild.nodeValue)
            
            dist = elemGeoname.getElementsByTagName('distance')[0]
            result.setDistance(dist.firstChild.nodeValue)
            
            return result
        except Exception as e:
            print e.message
class GeoNamesHandler(ContentHandler):
    typonymName = ""
    name = ""
    latitude = ""
    longitude = ""
    geonameID = ""
    distance = ""
    istyponymName = False
    isname = False
    isLat = False
    isLng = False
    isgeonameID = False
    isDistance = False
##    geonameArray = GeoName()
    geoname = GeonamesResult()
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
        if (name == "distance"):
            self.isDistance = True
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
        if self.isDistance:
            self.distance += ch
    def endElement(self,name):
        if (name == "toponymName") :
##            print "%s" % self.typonymName
            self.istyponymName = False
            self.geoname.setTyponymName(self.typonymName)
            self.typonymName = ""
        if (name == "name") :
##            print "%s" % self.name
            self.isname = False
            self.geoname.setName(self.name)
            self.name = ""
        if (name == "lat"):
##            print "%s" % self.latitude
            self.isLat = False
            self.geoname.setLat(self.latitude)

            self.latitude = ""
        if (name == "lng"):
##            print "%s" % self.longitude
            self.isLng = False
            self.geoname.setLng(self.longitude)

            self.longitude = ""
        if (name == "geonameId"):
##            print "%s" % self.geonameID
            self.isgeonameID = False
            self.geoname.setGeonameID(self.geonameID)
            self.geonameID = ""
        if (name == "distance"):
            self.isDistance = False
            self.geoname.setDistance(self.distance)
            self.distance = ""
        if (name == "geoname"):
            pass
    
