drop_list = ['stopCode', 'stopShortName', 'stopDesc','subName',
                'date', 'zoneId', 'virtual', 'nonpassenger','depot',
                'ticketZoneBorder', 'onDemand', 'activationDate', 'stopUrl',
                'locationType', 'parentStation', 'stopTimezone','wheelchairBoarding',
            ]
types_dict = {"stopId": 'int',
              "delayInSeconds": 'float64',
              "estimatedTime": 'datetime64',
              }
headers = {
    "Content-Type": "application/json"
}
stops_list_url = 'https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7-a39f-d156d201b82b/download/stops.json'
departures_url = 'https://ckan2.multimediagdansk.pl/departures'
pbi_api = url = 'https://api.powerbi.com/beta/164e1b0e-c8e5-41a9-9bbb-6f7ed40eef04/datasets/e31f101e-8fa2-48de-badd-c76e06ef1f04/rows?key=eVQrrVj%2FS6PLhUzYJ1P94j%2FnMjOnk97LAZC2ybdxWDuuQ4JsQzC9gB8gisDGz9Xi0T9YYnD8O3HaAQ%2BP4HSlUg%3D%3D'