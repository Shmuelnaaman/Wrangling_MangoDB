# web service quarie and transform it to json
# 
# 
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    params["query"] = "artist:" + name
    return query_site(url, params)


def pretty_print(data, indent=4):
    if type(data) == dict:
        print json.dumps(data, indent=indent, sort_keys=True)
    else:
        print data


def main():
    results = query_by_name(ARTIST_URL, query_type["simple"], "First Aid Kit")
   # pretty_print(results)
    
    release_name=   map(lambda x: x['name'] , results["artists"])
    b = [item for item in range(len(release_name)) if release_name[item] == 'First Aid Kit']
    
    print "\nnumber of  bands name :'First Aid Kit':"
    print len(b)
    #######################################################################
    
    results = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
    release_name=   map(lambda x: x['name'] , results["artists"])

    b = [item for item in range(len(release_name)) if release_name[item] == 'Queen']
    for i in b:
        if  results['artists'][i].has_key('begin-area'):
           print "\nBegin area name for Queem:"
           print results['artists'][i]['begin-area']['name']
    #######################################################################
    
    results = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
    release_name=   map(lambda x: x['name'] , results["artists"])

    b = [item for item in range(len(release_name))]
    for i in b:
       if  results['artists'][i]['area']:
        #   print "\nBegin area name for Queem:"
           print results['artists'][i]['area']['name']
    #pretty_print(results["artists"][1])
    
    #######################################################################
    
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    release_name=   map(lambda x: x['name'] , results["artists"])

    #b = [item for item in range(len(release_name)) if release_name[item] == 'Nirvana']
    #for i in b:
    print "\nNirvana disambiguation:"
    print results['artists'][0]['disambiguation']
           
           #pretty_print(results["artists"][1])
    
    results = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
    #release_name=   map(lambda x: x['name'] , results["One Direction"])

    #b = [item for item in range(len(release_name)) if release_name[item] == 'Nirvana']
    #for i in b:
    print "\nOne direction formed:"
    print results['created']
           
           #pretty_print(results["artists"][1])
    
    
        
    


if __name__ == '__main__':
    main()
