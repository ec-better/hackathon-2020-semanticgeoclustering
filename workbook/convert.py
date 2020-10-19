import json

prefix = "http://slipo.eu/id/poi"
rdftype = "<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>"
poi = "<http://slipo.eu/def#POI>"
category = "<http://slipo.eu/def#category>"
termPrefix = "http://slipo.eu/id/term"
termValue = "<http://slipo.eu/def#termValue>"
rdf = ""
i = 0
hasGeometry = "<http://www.opengis.net/ont/geosparql#hasGeometry>"
geometryID = "<http://slipo.eu/id/poi/__id__/geometry>"
wkt = "<http://www.opengis.net/ont/geosparql#asWKT>"
epsg = "<http://www.opengis.net/def/crs/EPSG/0/4326>"
wktLiteral = "<http://www.opengis.net/ont/geosparql#wktLiteral>"
#'/home/mmami/FhG/Projects/BETTER/EOPEN/EnglishFloodTweets_10000.json'
with open('EnglishFloodTweets__.json') as json_file:# dummy_tweet.json
    data = json.load(json_file)
    temp = 0
    for p in data['tweets']:
        print(p['id'])
        
        temp = temp+1
        point_id = p['id']
        concepts = p['image_concepts']

        if concepts != "n/a":
            subject = "<" + prefix + "/" + point_id + ">"            
            triple = subject + " " + rdftype + " " + poi + " . "
            rdf += triple + "\n"

            conceptsArray = concepts.split()
            for cat in conceptsArray:   
                term = ("<" + termPrefix + "/%s>" % i)             
                triple2category = subject + " " + category + " " + term + " .\n"                
                categoryTerm = subject + " " + termValue + " \"" + cat + "\" .\n"
                rdf += triple2category + categoryTerm
                i = i+1
            
            locations = p['estimated_locations']
            geometry = locations[0]['geometry']
            coordinates = geometry['coordinates']
            lat = coordinates[0]
            long = coordinates[1]

            geometryObject = geometryID.replace("__id__", point_id)

            geo = subject + " " + hasGeometry + " " + geometryObject + " ."
            geoPoint = ((geometryObject + " " + wkt + " \"" + epsg + " POINT(%f %f)\"^^" + wktLiteral + " .") % (lat, long))


            rdf += geo + "\n" + geoPoint + "\n"

            # print(rdf)

                

    # print(rdf)

    output_file = open('EOPEN_POIs_100.nt', 'w+') # append mode
    output_file.write(rdf)
    output_file.close()
