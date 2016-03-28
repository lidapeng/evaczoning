'''
Created on Mar 25, 2016

@author: Dapeng Li
'''
#from reversegeocoders.agrclib import AGRCResult,AGRCReverseGeocoder 
# include all reverse geocoders
from reversegeocoders.geonameslib import GeonamesReverseGeocoder
from reversegeocoders.openstreetmaplib import OpenStreetResult,OpenStreetReverseGeocoder
from reversegeocoders.googlelib import GoogleResult,GoogleReverseGeocoder
from reversegeocoders.mapquestlib import MapQuestResult,MapQuestReverseGeocoder
from reversegeocoders.distance import VincentyDistance
from reversegeocoders.arcgislib import ArcGISResult,ArcGISReverseGeocoder
if __name__ == '__main__':
    #40.766453, -111.865761
    geonamesRGeocoder = GeonamesReverseGeocoder()
    osmRGeocoder = OpenStreetReverseGeocoder()
    result = geonamesRGeocoder.reverseGeocode(40.766017, -111.865726)
    print result.geonameID, result.name, result.distance
    result1 = osmRGeocoder.reverseGeocode(40.766017, -111.865726)
    #print result1.displayName
    googleRGeocoder = GoogleReverseGeocoder()
    result2 = googleRGeocoder.reverseGeocode(40.766017, -111.865726)
    print result2.name, result2.latitude, result2.longitude
    dist = VincentyDistance()
    print dist.measure([40.766017, -111.865726], [result2.latitude, result2.longitude])
    
    pass