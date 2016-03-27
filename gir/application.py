'''
Created on Jan 31, 2014

@author: Dapeng Li
'''
import mylib
import sys
import binglib
import googlelib
import geonameslib
import arcgislib
import mapquestlib
import openstreetmaplib
import mycsvwriter
import arcpy

if __name__ == '__main__':
    print 'main'
    print mylib.fun1(1,2)
    print sys.argv[0],sys.argv[1]
    data =[]
#     data.append([1,2,3])
#     data.append([4,5,6])
    dataDirectory = r"D:\Project\geocoding\reversegeocoding\AGRC\aag\data"
    urbanData = dataDirectory + '\\' + r'randurban.shp'
    suburbanData = dataDirectory + '\\' + r'randsuburban.shp'
    pointData = dataDirectory + '\\' + r'points.shp'
    myCursor = arcpy.SearchCursor(pointData)
    
    
    row = myCursor.next()
    ID = 1
    while row:
        pt = row.getValue("Shape")
        print str(ID) + ':  ' + 'latitidue : ' + str(pt.firstPoint.Y) + " longitude: "+ str(pt.firstPoint.X)
        #addr = row.getValue("FullAdd") +' ' + row.getValue("City") +' ' + row.getValue("ZipCode")+' '+row.getValue('State')
#         print addr
        
        lat = pt.firstPoint.Y
        lon = pt.firstPoint.X
        
        bing = binglib.BingReverseGeocoder()
        resBing = bing.reverseGeocode(lat,lon)
        while not resBing:
            resBing = bing.reverseGeocode(lat,lon)
        print resBing.address, resBing.latitude, resBing.longitude
        row = []
        row.append(ID)
        row.append(lat)
        row.append(lon)
#         row.append(addr)
        row.append('BingMap')
        row.append(resBing.latitude)
        row.append(resBing.longitude)
        row.append(resBing.address)
        row.append('')
        data.append(row)
         
        google = googlelib.GoogleReverseGeocoder()
        resGoogle = google.reverseGeocode(lat,lon)
        while not resGoogle:
            resGoogle = google.reverseGeocode(lat,lon)
        print resGoogle.name, resGoogle.latitude, resGoogle.longitude
         
        row = []
        row.append(ID)
        row.append(lat)
        row.append(lon)
#         row.append(addr)
        row.append('Google')
        row.append(resGoogle.latitude)
        row.append(resGoogle.longitude)
        row.append(resGoogle.name)
        row.append('')
        data.append(row)
         
        geonames = geonameslib.GeonamesReverseGeocoder()
        resGeonames = geonames.reverseGeocode(lat,lon)
        while not resGeonames:
            resGeonames = geonames.reverseGeocode(lat,lon)
        print resGeonames.typonymName, resGeonames.name, resGeonames.latitude, resGeonames.longitude
         
        row = []
        row.append(ID)
        row.append(lat)
        row.append(lon)
#         row.append(addr)
        row.append('GeoNames')
        row.append(resGeonames.latitude)
        row.append(resGeonames.longitude)
        row.append(resGeonames.name)
        row.append(resGeonames.typonymName)
        data.append(row)
        
    # #     wkid= 4326  WGS84
        arcgis = arcgislib.ArcGISReverseGeocoder()
        resArcGIS = arcgis.reverseGeocode(lat,lon)
        while not resArcGIS:
            resArcGIS = arcgis.reverseGeocode(lat,lon)
        
       # print resArcGIS.address, resArcGIS.latitude, resArcGIS.longitude, resArcGIS.Loc_name, resArcGIS.wkid
         
        row = []
        if resArcGIS is not None:
            row.append(ID)
            row.append(lat)
            row.append(lon)
    #         row.append(addr)
            row.append('ArcGIS')
            row.append(resArcGIS.latitude)
            row.append(resArcGIS.longitude)
            row.append(resArcGIS.address)
            row.append('')
        data.append(row)        
    #     
    #     print "mapquest"    
        mapquest = mapquestlib.MapQuestReverseGeocoder()
        resMapquest = mapquest.reverseGeocode(lat,lon)
        while not resMapquest:
            resMapquest = mapquest.reverseGeocode(lat,lon)
        print resMapquest.latitude, resMapquest.longitude, resMapquest.street, resMapquest.city, resMapquest.geocodeQuality
         
        row = []
        row.append(ID)
        row.append(lat)
        row.append(lon)
#         row.append(addr)
        row.append('MapQuest')
        row.append(resMapquest.latitude) 
        row.append(resMapquest.longitude)
        row.append(resMapquest.street + resMapquest.city)
        row.append('')
        data.append(row)    
         
    #     print "OpenStreetMap"
        openstreet = openstreetmaplib.OpenStreetReverseGeocoder()
        resOpenStreet = openstreet.reverseGeocode(lat,lon)
        while not resOpenStreet:
            resOpenStreet = openstreet.reverseGeocode(lat,lon)
        print resOpenStreet.place_id, resOpenStreet.osm_id, resOpenStreet.osm_type, resOpenStreet.latitude, resOpenStreet.longitude,resOpenStreet.displayName
         
        row = []
        row.append(ID)
        row.append(lat)
        row.append(lon)
#         row.append(addr)
        row.append('OpenStreetMap')
        row.append(resOpenStreet.latitude)
        row.append(resOpenStreet.longitude)
        row.append(resOpenStreet.displayName)
        row.append('')
        data.append(row)
        
        row = myCursor.next() 
        ID = ID +1
        
#     fields = ['BingMap','Google','GeoNames','ArcGIS','MapQuest','OpenStreetMap']
#     fields = ['ID','latitude','longitude','originalAddress','ServiceName','lat','lon','address','typonym']
    fields = ['ID','latitude','longitude','ServiceName','lat','lon','address','typonym'] 
    csvWriter = mycsvwriter.myCSVWriter(fields,data)
    csvWriter.writeToFile(dataDirectory + '\\' + 'julianpoints.csv')
         
    pass

