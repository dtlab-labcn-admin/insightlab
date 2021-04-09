#! /usr/bin/env python
from os import environ
from insightlab import Insight, InsightObjects

TOKEN = environ.get("INSIGHT_TOKEN", "")

## Set login
i = Insight.API(TOKEN, "4")

# Load the object
my_server = i.load("IDLAB-4802")
try:
    print(
        f"Current IPs: {my_server.attribute_value_by_name('IP', first_found = False)}"
    )
except:
    print(f"Current IPs: no ips found")

# Find the object we want to reference to
ip = i.find_object("10.0.10.20", "IP")

# Find the attribute id we want to assign this object to
attr_id = i.find_object_type_attribute_id("Server", "IP")

# Update the value using the object's id
# Note here: The "value" here is the object's id.
i.update_attribute(my_server.id, attr_id, [ip.id])

# Reload and print the results
my_server = i.load("IDLAB-4802")
ips = my_server.attribute_value_by_name("IP", first_found=False)[0].displayValue
print(f"Current IPs: {ips}")

input("Press Enter to continue...")

# Clear the ips
i.update_attribute(my_server.id, attr_id, [""])

# Reload and print the results
my_server = i.load("IDLAB-4802")
try:
    print(f"Current IPs: {my_server.attribute_value_by_name('IP')}")
except:
    print(f"Current IPs: no ips found")
