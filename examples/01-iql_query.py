#! /usr/bin/env python
from os import environ
from insightlab import Insight, InsightObjects

TOKEN = environ.get("INSIGHT_TOKEN", "")

## Set login
i = Insight.API(TOKEN, "4")

## Make a simple IQL query
r = i.iql_query('objectType IN objectTypeAndChildren("Server")')
for o in r.objects:
    print(o.label)
