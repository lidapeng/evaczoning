#define the common classes
class Location:
##    lat = ""
##    lng = ""
    def __init__(self):
        self.lat = ""
        self.lng = ""
    def setlat(self,newlat):
        self.lat = newlat
    def setlng(self,newlng):
        self.lng = newlng

    def getlat(self):
        return self.lat
    def getlng(self):
        return self.lng
    
    def reset(self):
        self.lat = ""
        self.lng = ""
    def setLocation(self,loc):
        self.setlat(loc.getlat())
        self.setlng(loc.getlng())
