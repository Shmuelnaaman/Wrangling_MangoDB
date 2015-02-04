#!/usr/bin/env python
"""
aggregation query to answer the following question. 

, find the average regional city population 
for all countries in the cities collection. What we are asking here is that you 
first calculate the 
average city population for each region in a country and then calculate the 
average of all the 
regional averages for a country. 


"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [   {'$match':{ 'name': { '$exists': 'true' } } },
                {'$unwind':'$isPartOf'} ,                   
                   {'$group' : {'_id':'$isPartOf',
                                'dis_avg':{'$avg': '$population'}, 
                                'country':{'$first':'$country' }}}  , 
                  {'$group' : {'_id':'$country',
                                'avgRegionalPopulation':{'$avg': '$dis_avg'}}} ,  
                  {'$sort':{'cutr_avg':-1}}
                 ]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    if len(result["result"]) < 150:
        pprint.pprint(result["result"])
    else:
        pprint.pprint(result["result"][:100])
    for country in result["result"]:
        if country["_id"] == 'Algeria':
            assert country["_id"] == 'Algeria'
            assert country["avgRegionalPopulation"] == 187590.19047619047
    assert {'_id': 'Algeria', 
             'avgRegionalPopulation': 187590.19047619047} in result["result"]
