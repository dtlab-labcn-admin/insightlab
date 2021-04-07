from insightlab import Insight, InsightObjects

TOKEN = ""

## Set login
i = Insight.API(TOKEN, "4")

## Find the object
my_server = i.find_object("Proxmox 4", "Server")

## Load an object
print(my_server.name)

# Print an attribute
print(my_server.attribute_value_by_name("Hostname"))

# Or if you know the item id
my_server = i.load("IDLAB-4802")
print(my_server.name)
print(my_server.attribute_value_by_name("Hostname"))