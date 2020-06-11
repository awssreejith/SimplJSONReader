import json

if __name__ == "__main__":
    world_dict = {
     "Australia":[{"name":"South Australia","population":500000},{"name":"Western Australia","population":700000}]
     ,
     "India":[{"name":"Karnataka","population":1000000},{"name":"Tamil Nadu","population":1500000}]
     ,
     "England":[{"name":"Wales","population":200000},{"name":"Scotland","population":300000}]
    }

    world_str = '''{
     "Australia":[{"name":"South Australia","population":500000},{"name":"Western Australia","population":700000}]
     ,
     "India":[{"name":"Karnataka","population":1000000},{"name":"Tamil Nadu","population":1500000}]
     ,
     "England":[{"name":"Wales","population":200000},{"name":"Scotland","population":300000}]
    }'''

    jsonData_fromDict = None
    jsonData_fromStrg = None
    jsonData_fromFile = None

    with open('NobelLaurate.json','r') as jsonFile:
        jsonData_fromFile = json.load(jsonFile)
    try:
        jsonData_fromDict = json.dumps(world_dict,indent=2)
        #jsonData_fromStrg = json.loads(world_str)
        
        print("Converted to json succsfully")
    except Exception as ex:
        print (ex)

    print(jsonData_fromDict)
    print(type(jsonData_fromDict))
    #print(type(jsonData_fromStrg))

    #jsonData_fromStrg['Australia'][1]['population'] = '800000'
    #print(jsonData_fromStrg['Australia'])
    #print(json.dumps(jsonData_fromFile,indent=2))
    firstname = ''
    surname = ''
    count = 0
    for ele in jsonData_fromFile['prizes']:
        if 'laureates' in ele:
            laurt = ele['laureates']
            for elem in laurt:
                count+=1
                if 'firstname' in elem:
                    firstname = elem['firstname']
                else:
                    firstname = ''
                if 'surname' in elem:
                    surname = elem['surname']
                else:
                    surname = ''
                print('['+str(count)+'] '+ele['year'] + ' ---> ' +firstname+" "+surname+"  -- awarded for "+ele['category'])

    

