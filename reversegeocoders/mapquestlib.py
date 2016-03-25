'''
Created on Feb 2, 2014

@author: Dapeng Li
'''
import json
from pprint import pprint
import string, os, sys, httplib, urllib2
import StringIO,csv,codecs

class MapQuestResult:

    def __init__(self):
        self.street = ""
        self.city = ""
        self.latitude = ""
        self.longitude = ""
        self.geocodeQuality = ""
    def setStreet(self,str):
        self.street = str
    def setCity(self,city):
        self.city = city
    def setLat(self,lat):
        self.latitude = lat
    def setLng(self,lng):
        self.longitude = lng
    def setGeocodeQuality(self,quality):
        self.geocodeQuality = quality
        


class MapQuestReverseGeocoder:
    
    def reverseGeocode(self,lat,lon):
        try:
            result = MapQuestResult()
            mapquestURL = r'http://www.mapquestapi.com/geocoding/v1/reverse?key=Fmjtd|luub2huzn5%2Cal%3Do5-9utnga&location=' + str(lat) +r','+str(lon)
            
            s = urllib2.urlopen(mapquestURL)
                
            data = json.load(s)
    #         print data['options']['maxResults']
    #         result.setLat(data[0])
            result.setLat(data['results'][0]['locations'][0]['latLng']['lat'])
            result.setLng(data['results'][0]['locations'][0]['latLng']['lng'])
            
            result.setCity(data['results'][0]['locations'][0]['adminArea5'])
            result.setStreet(data['results'][0]['locations'][0]['street'])
            result.setGeocodeQuality(data['results'][0]['locations'][0]['geocodeQuality'])
            return result
        except Exception as e:
            print e.message
