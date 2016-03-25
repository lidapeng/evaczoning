'''
Created on Apr 2, 2014

@author: Dapeng Li
'''
import arcpy
import mycsvwriter

if __name__ == '__main__':
    
    try:
        dataDirectory = r"D:\Project\geocoding\reversegeocoding\AGRC\aag"
        monroeFile = dataDirectory + '\\' + 'suburban1.shp'
        myCursor = arcpy.SearchCursor(monroeFile)
        myData = []
        row = myCursor.next()
        ID = 1
        while row:
            pt = row.getValue("Shape")
            dataRow = []
            print str(ID) + ':  ' + 'latitidue : ' + str(pt.firstPoint.Y) + " longitude: "+ str(pt.firstPoint.X)
            dataRow.append(pt.firstPoint.Y)
            dataRow.append(pt.firstPoint.X)
            myData.append(dataRow)
            row = myCursor.next()
            ID = ID + 1
        fields = ['latitude','longitude']
        csvWriter = mycsvwriter.myCSVWriter(fields,myData)
        csvWriter.writeToFile(dataDirectory + '\\' +'data' + '\\' + 'monroesuburbanaddr.csv')
    except Exception as e:
        print e.message
    pass