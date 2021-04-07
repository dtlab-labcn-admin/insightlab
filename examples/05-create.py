from insightlab import Insight, InsightObjects

TOKEN = ""

## Set login
i = Insight.API(TOKEN, "4"))

# Find the object type's ID we want to create
obj_type = i.find_object_type_id("Server")

# Find the attribute ID
attr_id = i.find_object_type_attribute_id("Server", "Name")

# Instanciate a NewObject
newobj = InsightObjects.NewObject(obj_type)

# Add some attributes
newobj.add_attribute(attr_id,"My New Server")

# Add some referenced attribute
attr_id = i.find_object_type_attribute_id("Server", "IP")
ip = i.find_object("10.0.10.22", "IP")
newobj.add_attribute(attr_id, ip.id)

# Create the new object
i.create(newobj)

