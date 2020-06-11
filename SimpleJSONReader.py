import json


if __name__ == "__main__":
    
    jsonData_fromFile = None

    with open('NobelLaurate.json','r') as jsonFile:
        jsonData_fromFile = json.load(jsonFile)
    try:
        jsonData_fromDict = json.dumps(world_dict,indent=2)
        
        print("Converted to json succsfully")
    except Exception as ex:
        print (ex)

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

    

