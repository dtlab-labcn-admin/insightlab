from insightlab import Insight, InsightObjects

TOKEN = ""

## Set login
i = Insight.API(TOKEN, "4")

## Make a simple IQL query
r = i.iql_query('objectType IN objectTypeAndChildren("Server")')
for o in r.objects:
    print(o.label)
