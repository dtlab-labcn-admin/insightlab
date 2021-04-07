from insightlab import Insight, InsightObjects

TOKEN = ""

## Set login
i = Insight.API(TOKEN, "4")

## Find the object
my_server = i.find_object("My New Server", "Server")

# Let's confirm it's the right one
print(my_server.name + " " + my_server.objectKey)

input("We good?")

# Delete the object
i.delete(my_server.id)
