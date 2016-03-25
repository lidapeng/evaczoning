'''
Created on Feb 1, 2014

@author: Dapeng Li
'''
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import string, os, sys, httplib, urllib2
import StringIO,csv,codecs
import urllib
from xml.dom import minidom

# result from Bing map reverse geocoding service 
class BingResult:

    def __init__(self):
        self.address=""
        self.latitude = ""
        self.longitude = ""
        self.distance = ""        
    def setAddress(self,addr):
        self.address = addr
    def setLat(self,lat):
        self.latitude = lat
    def setLon(self,lon):
        self.longitude = lon
    def setDistance(self,dist):
        self.distance = dist

#geocoder for BingMap
class BingGeocoder():
    def parseXML(self,url):
        result = BingResult()
        print url
        s = urllib2.urlopen(url)
        xmldoc = minidom.parse(s)
        loc = xmldoc.getElementsByTagName('Location')
        elem = loc[0].getElementsByTagName('Name')[0]
        result.setAddress(elem.firstChild.nodeValue)
        
        lat = loc[0].getElementsByTagName('Latitude')[0].firstChild.nodeValue
        print lat
        for node in loc:
            print 'output:', node.hasAttributes()
        return result
    def Geocode(self,strAddress):
#         construct the URL for reverse geocoding query
#         url = r'http://dev.virtualearth.net/REST/v1/Locations/' + strAddress + r'?output=' +    urllib.quote('xml') + r'&key=' + urllib.quote(r'Agzi-DVIKLqXS52fI9TVve0pICvNAEQLzR_IBKBlsp_uqJbyoqpWz1MbuZGpxZT9')
        try:
            address = urllib2.quote(strAddress)
            #url = r'http://dev.virtualearth.net/REST/v1/Locations/' + strAddress + r'?output=xml&key=Agzi-DVIKLqXS52fI9TVve0pICvNAEQLzR_IBKBlsp_uqJbyoqpWz1MbuZGpxZT9'
            url = 'http://dev.virtualearth.net/REST/v1/Locations/%s'%(address)
            url = url + r'?output=xml&key=Agzi-DVIKLqXS52fI9TVve0pICvNAEQLzR_IBKBlsp_uqJbyoqpWz1MbuZGpxZT9'
            print url
            result = BingResult()
    #         req = urllib2.Request(url)
            s = urllib2.urlopen(url)
            xmldoc = minidom.parse(s)
            loc = xmldoc.getElementsByTagName('Location')
            print loc
            if loc == None:
                return None
            elem = loc[0].getElementsByTagName('Name')[0]
    #         set the address value
            result.setAddress(elem.firstChild.nodeValue)
            
            lat = loc[0].getElementsByTagName('Latitude')[0].firstChild.nodeValue
            lon = loc[0].getElementsByTagName('Longitude')[0].firstChild.nodeValue
            result.setLat(lat)
            result.setLon(lon)
            return result 
        except Exception as e:
            print e.message
               
#  reverse geocoder for Bing map   
class BingReverseGeocoder(): 
    
    def parseXML(self,url):
        result = BingResult()
        print url
        s = urllib2.urlopen(url)
        xmldoc = minidom.parse(s)
        loc = xmldoc.getElementsByTagName('Location')
        elem = loc[0].getElementsByTagName('Name')[0]
        result.setAddress(elem.firstChild.nodeValue)
        
        lat = loc[0].getElementsByTagName('Latitude')[0].firstChild.nodeValue
        print lat
        for node in loc:
            print 'output:', node.hasAttributes()
        return result
    
    def reverseGeocode(self,lat,lon):
        try:
    #         construct the URL for reverse geocoding query
            url = r'http://dev.virtualearth.net/REST/v1/Locations/' + str(lat) + r',' + str(lon) + r'?o=xml&key=Agzi-DVIKLqXS52fI9TVve0pICvNAEQLzR_IBKBlsp_uqJbyoqpWz1MbuZGpxZT9'
            
            result = BingResult()
            
            s = urllib2.urlopen(url)
            xmldoc = minidom.parse(s)
            loc = xmldoc.getElementsByTagName('Location')
            elem = loc[0].getElementsByTagName('Name')[0]
    #         set the address value
            result.setAddress(elem.firstChild.nodeValue)
            
            lat = loc[0].getElementsByTagName('Latitude')[0].firstChild.nodeValue
            lon = loc[0].getElementsByTagName('Longitude')[0].firstChild.nodeValue
            result.setLat(lat)
            result.setLon(lon)
            
            return result
        except Exception as e:
            print e.message
            
    