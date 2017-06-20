#!/usr/bin/env python3
import argparse
import json
import sys

def main(inputfile, outputfile):
    data = json.load(inputfile)

    output = """<?xml version="1.0" encoding="UTF-8"?>
<gpx creator="@Categulario" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
 <metadata>
  <time>2017-06-19T19:47:31Z</time>
 </metadata>
 <trk>
  <name>Track 1</name>
  <trkseg>
"""

    for lat, lng in data['latlng']:
        output += """<trkpt lat="{}" lon="{}">
    <ele>2266.1</ele>
    <time>2017-06-19T19:47:31Z</time>
   </trkpt>
""".format(lat, lng)

    output += """</trkseg>
 </trk>
</gpx>
"""

    outputfile.write(output)

    inputfile.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Converts a json of latlngs extracted from strava to GPX')

    parser.add_argument('trackfile', type=open, help="The json file with the latlng array")
    parser.add_argument('-o --output', type=argparse.FileType('w', encoding='UTF-8'), default=sys.stdout, dest='output', help="The output file, defaults to stdout")

    args = parser.parse_args()

    main(args.trackfile, args.output)
