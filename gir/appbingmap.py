'''
Created on Apr 2, 2014

Redo all the locations returned from Bing Map reverse geocoding service
@author: Dapeng Li
'''
from reversegeocoders import binglib
import mycsvwriter
import time

if __name__ == '__main__':
    
    try:
        dataDirectory = r"D:\Project\geocoding\reversegeocoding\AGRC\aag\data"
        strInputFile = dataDirectory + '\\' + 'randsuburban.csv'
        bingInputFile = dataDirectory + '\\' + 'bingrandsuburban.csv'
        
        JulianPointFile = dataDirectory + '\\' + 'julianpoints.csv'
        julianAddrFile = dataDirectory + '\\' + 'bingjulianaddress.csv'
        bingAddrFile = open(julianAddrFile,'r')
        bingAddrData = bingAddrFile.readlines()
        
        inputFile = open(JulianPointFile,'r')
        data = inputFile.readlines()
        inputFile.close()
        dataFields = data[0].split(',')
        for i in dataFields:
            print i 
        num =  (len(data)-1)/6
        print 'length: ', len(data)
        print 'num: ',num
        dataset = []
        
        for i in range(0,num):
            
            for j in range(0,6):
                n = i*6 + j + 1
                item =[]
                rows = data[n].split(',')
                for r in rows:
                    item.append(r)
#                 print 'length of item: ',len(item)
                if j == 0:
                    print 'ID: ',i
#                     bingRes = bingGeocoder.Geocode(bingAddrData[n])
                    strAddr = str(bingAddrData[n])
                    strAddr = strAddr.translate(None,'!@#$&"\n')
                    
                    print strAddr
                    
                    bingGeocoder = binglib.BingGeocoder()
                    
                    bingRes = bingGeocoder.Geocode(strAddr)
                    while(not bingRes):
                        bingRes = bingGeocoder.Geocode(strAddr)
                    
#                     time.sleep(2)
                    print 'length of item: ', len(item)
                    item[4] = str(bingRes.latitude)
                    print item[4]
                    item[5] = str(bingRes.longitude)
                    print item[5]
                row = []
                for k in range(0,6):
                    row.append(item[k])
#                     print k
                row.append(bingAddrData[n].translate(None,'!@#$&"\n'))
                dataset.append(row)
                print n,'inserted\n'
#                     print bingRes.address,bingRes.latitude,bingRes.longitude
#                 dataset.append(data[i*6 + j + 1].split(','))
        strOutputFile = r'D:\Project\geocoding\reversegeocoding\AGRC\aag\data\newjulianpoints.csv'
#         myfields = ['BingMap','Google','GeoNames','ArcGIS','MapQuest','OpenStreetMap']
        csvwriter = mycsvwriter.myCSVWriter(dataFields,dataset)
        csvwriter.writeToFile(strOutputFile)
    except Exception as e:
        print e.message
            
    
#     bingGeocoder = binglib.BingGeocoder()
#     bingRes = bingGeocoder.Geocode(r'417 W 370 S, Monroe')
#     print bingRes.address,bingRes.latitude,bingRes.longitude
#     rvGeocoder = binglib.BingReverseGeocoder()
#     res = rvGeocoder.reverseGeocode(38.6255, -112.13049)
#     print res.address,res.latitude,res.longitude
    pass