#! /usr/bin/env python
from os import environ
from insightlab import Insight, InsightObjects

TOKEN = environ.get("INSIGHT_TOKEN", "")

## Set login
i = Insight.API(TOKEN, "4")

## Load the object
my_server = i.load("IDLAB-5709")
print(f"Current hostname: {my_server.attribute_value_by_name('Hostname')}")

## Find the attribute's id
id = my_server.attribute_id_by_name("Hostname")

## Update the attribute's value
i.update_attribute(my_server.id, id, ["new_hostname.test.idlab.org"])

# Reload the object
my_server = i.load("IDLAB-5709")
print(f"New hostname: {my_server.attribute_value_by_name('Hostname')}")

input("Press Enter to continue...")

# Reset to original
i.update_attribute(my_server.id, id, ["test.server.idlab.org"])
