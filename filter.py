#! /usr/bin/env python3
import csv
import json

with open("airports.csv") as fh:
    num = 0
    reader = csv.DictReader(fh)

    deny_type = ["closed"]; ## Append to this list

    ## We want to filter on US-CA
    us_cali = filter(lambda x: x["iso_region"] == "US-CA"
                                and x["type"] not in deny_type
                                and x["ident"].startswith("K"), reader)


    ## TODO: We can minimize the fields needed for the app as well.

    s = json.dumps(list(us_cali))

    print(s)

