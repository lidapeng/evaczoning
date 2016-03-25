import arcpy
from arcpy import env
env.workspace =r"D:\Project\geocoding"
triggerbuffer = r"D:\Project\geocoding\triggerbuffer.gdb\Placemarks\Polygons"

def test1():    
    rows = arcpy.SearchCursor(triggerbuffer)
    row = rows.next()
    feat = row.Shape
    pts= feat.getPart(0)
    print "*****************"