'''
Created on Mar 30, 2014

@author: Dapeng Li
'''
import sys
from reversegeocoders.distance import VincentyDistance
from reversegeocoders.point import Point
import mycsvwriter

if __name__ == '__main__':
    #strInputFile = r'D:\Project\geocoding\reversegeocoding\AGRC\aag\urban1.csv'
    strInputFile = r'D:\Project\geocoding\reversegeocoding\AGRC\aag\data\newrandsuburban.csv'
    try:
        inputFile = open(strInputFile,'r')
        data = inputFile.readlines()
        print len(data)
        for i in range(0,10):
            print data[i]
        dataFields = data[0].split(',')
        for i in dataFields:
            print i 
        num =  (len(data)-1)/6
        dataset = []
        item = []
        for i in range(0,num):
            for j in range(0,6):
                dataset.append(data[i*6 + j + 1 +1].split(','))
        distanceData = []
#         for i in range(0,10):
#             print dataset[i]
        for i in range(0,num):
            distanceRow = []
            for j in range(0,6):
                n= i*6 + j 
                pt = Point(float(dataset[n][1]),float(dataset[n][2]))
                print 'ID: ',i, len(dataset[n])
                if dataset[n][4]=='' or dataset[n][5]=='':
                    pt1 = Point(0.0,0.0)
                else:
                    pt1 = Point(float(dataset[n][4]),float(dataset[n][5]))
                dist = VincentyDistance()
                distanceValue = dist.measure(pt, pt1)*1000
                distanceRow.append(distanceValue)
            distanceData.append(distanceRow)
        print len(distanceData)
        strOutputFile = r'D:\Project\geocoding\reversegeocoding\AGRC\aag\data\distrandsuburban.csv'
        myfields = ['BingMap','Google','GeoNames','ArcGIS','MapQuest','OpenStreetMap']
        csvwriter = mycsvwriter.myCSVWriter(myfields,distanceData)
        csvwriter.writeToFile(strOutputFile)

        inputFile.close()
    except Exception as e:
        print e.message
            
    pass