'''
Created on Feb 3, 2014
OpenStreetMap reverse geocoding service: Nominatim
http://wiki.openstreetmap.org/wiki/Nominatim#Reverse_Geocoding_.2F_Address_lookup
http://nominatim.openstreetmap.org/reverse?format=xml&lat=47.64054&lon=-122.12934&zoom=18&addressdetails=1

@author: Dapeng Li
'''
import string, os, sys, httplib, urllib2
import StringIO,csv,codecs
from xml.dom import minidom
import json

class OpenStreetResult:
    def __init__(self):
        self.place_id = ""
        self.displayName = ""
        self.latitude = ""
        self.longitude = ""
        self.osm_type = ""
        self.osm_id = ""
    def setPlaceID(self,pid):
        self.place_id = pid
    def setDisplayName(self,name):
        self.displayName = name
    def setOSMType(self,OSMtype):
        self.osm_type = OSMtype
    def setOSMID(self,OSMID):
        self.osm_id = OSMID
    def setLat(self,lat):
        self.latitude = lat
    def setLon(self,lon):
        self.longitude = lon
    
class OpenStreetReverseGeocoder:
    def reverseGeocode(self,lat,lon):
        try:
            result = OpenStreetResult()
            url =  r"http://nominatim.openstreetmap.org/reverse?format=json&lat=" + str(lat) + r"&lon=" + str(lon) + r"&zoom=18&addressdetails=1"
    #         print url
            s = urllib2.urlopen(url)
            data = json.load(s)
            result.setPlaceID(data['place_id'])
            result.setOSMID(data['osm_id'])
            result.setOSMType(data['osm_type'])
            result.setLat(data['lat'])
            result.setLon(data['lon'])
            result.setDisplayName(data['display_name'])
            
    #         s = urllib2.urlopen(url)
    #         xmldoc = minidom.parse(s)
    #         elem = xmldoc.getElementsByTagName('result')[0]
    #         print elem.firstChild.nodeValue
            return result
        except Exception as e:
            print e.message
    
    