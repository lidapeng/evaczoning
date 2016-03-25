'''
Created on Jan 12, 2015

@author: Dapeng Li
'''
import distance
import point
from _server_admin.geometry import Point

if __name__ == '__main__':
    lat = 40.753075
    lon = -111.886324
    p1 = Point(lat,lon)
#     p2 = Point(lat+0.001, lon)
    p2 = Point(lat, lon+0.003)
    print p1,p2
    vinDist =distance.VincentyDistance()
    print 1000*vinDist.measure(p1,p2)
    