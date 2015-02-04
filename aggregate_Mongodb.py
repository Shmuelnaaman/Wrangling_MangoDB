#!/usr/bin/env python
"""
aggregation query to answer the following question. 

What is the most common city name in our cities collection?

identified None as the most frequently occurring city name. 
What that actually means is that there are a number of cities without a name field at all. 


To solve this problem the right way, we  ignore cities that don't have a name specified. 


'make_pipeline' function  creates and returns an aggregation pipeline 
that can be passed to the MongoDB aggregate function.  
the aggregation pipeline is a list of one or more dictionary objects. 


code  run against a MongoDB instance. 

"""

def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db

def make_pipeline():
    pipeline = [ {'$match':{ 'name': { '$exists': 'true' } } },
                 {'$group' : {'_id':'$name','count':{'$sum':1}}},
                 {'$sort':{'count':-1}},
                 {'$limit':1}]
    return pipeline

def aggregate(db, pipeline):
    result = db.cities.aggregate(pipeline)
    return result

if __name__ == '__main__':
    db = get_db('examples')
    pipeline = make_pipeline()
    result = aggregate(db, pipeline)
    import pprint
    pprint.pprint(result["result"][0])
