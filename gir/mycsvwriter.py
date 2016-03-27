'''
Created on Feb 22, 2014
This class is used to write data to a csv file.
@author: Dapeng Li
'''
import csv

class myCSVWriter(object):
    '''
    classdocs
    '''
    def __init__(self,fields, data):
        '''
        Constructor
        '''
        self.fields = fields
        self.data = data
    def writeToFile(self,fileName):
        
        try:
            print 'writing file to ' + fileName
            f = open(fileName,'wb')
#             csvWriter = csv.writer(open(fileName,'wb'),delimeter=',')
            csvWriter = csv.writer(f)
            csvWriter.writerow(self.fields)
#             for i in self.data:
#                 csvWriter.writerow(i)
            csvWriter.writerows(self.data)
            f.close()
            print 'file written to ' + fileName
        except Exception as e:
            print e.message
            
