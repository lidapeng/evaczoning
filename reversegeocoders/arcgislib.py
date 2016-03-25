##ArcGIS online parser
##the return format is JSON

import json
from pprint import pprint
import string, os, sys, httplib, urllib2
import StringIO,csv,codecs

class ArcGISResult:

    def __init__(self):
        self.Loc_name = ""
        self.address = ""
        self.latitude = ""
        self.longitude = ""
        self.wkid = ""
    def setAddress(self,addr):
        self.address = addr
    def setLat(self,lat):
        self.latitude = lat
    def setLng(self,lng):
        self.longitude = lng
    def setWkid(self,id1):
        self.wkid = id1  
    def setLocName(self,locName):
        self.Loc_name = locName 

class ArcGISReverseGeocoder:
    
    def reverseGeocode(self,lat,lon):
        
        
        try:
            arcgisURL = r"http://sampleserver1.arcgisonline.com/ArcGIS/rest/services/Locators/ESRI_Geocode_USA/GeocodeServer/reverseGeocode?location=" + str(lon) + r"," + str(lat) + r"&distance=1000&outSR=&f=pjson"
#             print arcgisURL
            
            s = urllib2.urlopen(arcgisURL)
            
            data = json.load(s)
            
            arcgisResult = ArcGISResult()
            arcgisResult.setAddress(data["address"]["Address"])
            arcgisResult.setLat(data['location']['y'])
            arcgisResult.setLng(data['location']['x'])
            arcgisResult.setLocName(data["address"]["Loc_name"])
            arcgisResult.setWkid(data["location"]["spatialReference"]["wkid"])
            
            return arcgisResult
        ##json_data.close()
        except Exception as e:
            print e.message



