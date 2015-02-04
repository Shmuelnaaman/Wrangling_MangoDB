#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  'make_request' .
# 
# process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the approprate
# values in the data dictionary.
# A
from bs4 import BeautifulSoup
import requests
import json

html_page = "page_source.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}
    with open(page, "r") as html:
        #  find the necessary values
        soup=BeautifulSoup(open(page))
        Form_param=soup.find(id="form1")
        for viewstate_id in Form_param.find_all("input"):
            if viewstate_id['name']=='__VIEWSTATE':
                data['viewstate']= viewstate_id['value']
            elif viewstate_id['name']=='__EVENTVALIDATION':
                data['eventvalidation']= viewstate_id['value']
      
        pass

    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]

    r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                    data={'AirportList': "BOS",
                          'CarrierList': "VX",
                          'Submit': 'Submit',
                          "__EVENTTARGET": "",
                          "__EVENTARGUMENT": "",
                          "__EVENTVALIDATION": eventvalidation,
                          "__VIEWSTATE": viewstate
                    })

    return r.text


def test():
    data = extract_data(html_page)

    
test()