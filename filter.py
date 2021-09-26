#! /usr/bin/env python3
import csv
import json

with open("airports.csv") as fh:
    num = 0
    reader = csv.DictReader(fh)

    ## Types of airports to filter.
    ## Append to this list
    deny_type = ["closed", "heliport", "seaplane_base", "balloonport"]; 

    ## We want to filter on US-CA
    us_cali = filter(lambda x: x["iso_region"] == "US-CA"
                                and x["type"] not in deny_type
                                and not x["ident"].startswith("US-")
                                ,reader)



    ## Create a list with just the fields we want.
    rel_fields = ['ident', 'latitude_deg', 'longitude_deg']

    compressed = []

    for l in list(us_cali):
        x = {}
        for field in rel_fields:
            x[field] = l[field]

        compressed.append(x)

    #s = json.dumps(list(us_cali))
    s = json.dumps(compressed)

    print(s)

