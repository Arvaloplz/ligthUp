# *                          @ANDROIDEV
# *                            2020
'''                                                  
                                #                   
                               ###                  
                              #####                 
                             #######                
                            ###### ##               
                           ###### ####              
                          ##### #######             
                         ####     ######            
                        ####        #####           
                       ###           #####          
                      ###              ####         
                     ##                  ###        
                    #                      ##       
                   #                         #      
'''
import json  # librery
import os
import string
import random


# ?                    FUNCTIONS


def generateId():
    return''.join(random.choices(string.ascii_uppercase + string.digits, k=8))



# ?                  CREATE A NEW JSON

def addNewJson(jsonFile): 
    """Add a new Json file in the current directiry 
    """
    if os.path.splitext(jsonFile) != '.json':
        jsonFile = jsonFile + '.json'

    if findJson(jsonFile):
        return False
    else:
        try:
            print("Directory data must to be created")
        except FileExistsError:
            return False
    with open(jsonFile, 'w'):
        pass
    data={

    }
    writeJson(jsonFile,data)
    return True

# ?                  JSON IS EMPTY


def isEmptyJson(currJson: str):
    """Find if the json is empty

    """
    numItems = 0
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            if len(data) == 0 :True
            else: False

# ?                  JSON GET DATA


def getData(currJson: str):
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            return data
    else: return None

# ?                  DEL A JSON

def delJson(jsonFile:str):
    """Delete a Json in a current directory

    """
    if findJson(jsonFile):
        os.remove(jsonFile)
        return True
    else:
        return False


# ?                  FIND A JSON

def findJson(jsonFile:str):
    """Find a Json file in a current directory
    """
    path = os.getcwd()
    dir_list= os.listdir(path)
    if jsonFile in dir_list:
        return True
    else:
            return False
    return False


# ?                  WRITE JSON 

def writeJson(currJson: str, data:dict):
    """Write the data in the current Json File
        --------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED data -> Data to add

        --------------------
    """
    with open(currJson, 'w') as jsonFileOut:
        json.dump(data, jsonFileOut, indent=4)



# ?                  ADD FIELD(Array of object)


def addField(currJson: str, newField: str):
    """Add a dictionary
    --------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED newFile:str -> Dic jsonFile to add it. DEFAULT VALUE = 'default'

        --------------------
    RETURN:
        TRUE -> correctly added

        FALSE -> it have an issue

    """
    if '.json' in currJson:
        print('Finding ...')  
    else:
        currJson = currJson+'.json'  
    if findJson(currJson):
        f = open(currJson)
        data = json.load(f)
        data[newField] = []
        writeJson(currJson, data)
        return True
    else:
        return False


# ?                  FIND FIELD(Array of object)

def findField(currJson:str, field:str):
    """find a dictionary
    --------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED file:str -> Dic name to add it. DEFAULT VALUE = 'default'

        --------------------
    RETURN:
        TRUE -> found

        FALSE -> not found

    """
    if '.json' in currJson:print('finding...')
    else:
        currJson = currJson+'.json'  
    numField = 0
    if findJson(currJson):

        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            if isEmptyJson(currJson):
                return False   
            else:
                for element in data:
                    if field == element:
                        numField = numField + 1
                        return True
        return False
    else:
        print('json not foud')
        return False


# ?                  DELETE FIELD(Array of object)

def delField(currJson: str, field:str):
    """delete a dictionary
    --------------------

    REQUIRED currJson--> current Json File. 

    REQUIRED file:str -> Dic name to add it. DEFAULT VALUE = 'default'

        --------------------
    RETURN:
        TRUE -> deleted

        FALSE -> not deleted

    """
    if os.path.splitext(currJson) != '.json':
        currJson = currJson + '.json'
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)

        for element in data:
            if element == field:
                del data[element]
                break

        writeJson(currJson, data)
    else:
        return False


# ?                  ADD ITEM(Object in an Array)


def addItem(currJson: str, dic='default', item: dict = None, name: str = None):
    """Add a new item  to a determinate dictionary
    --------------------

    REQUIRED currJson--> current Json File. 

    dic='default' -> Dic name to add item in it. DEFAULT VALUE = 'default'

    REQUIRED item: dict= None --> The item to add, it must be a dictionary.

    name:str = None --> The name that you want to asing to your item

        --------------------
    RETURN:
        TRUE -> correctly added

        FALSE -> it have an issue

    """
    nameObject= False
    if name != None:
        nameObject = True
    idFound = False
    if '.json' in currJson:
        print('finding...')  
    else:
        currJson = currJson+'.json'  
    id = generateId()
    while idFound == False:
        if findItem(currJson,dic,itemValue= id) :
            id = generateId()
        else: 
            idFound = True
    item['ID']= id 
    if findJson(currJson):
        if nameObject:
            if findItem(currJson, itemList=name):
                return False
            else:
                return __addItemNamed(currJson, dic, item, name)
        else:
            f = open(currJson)
            data = json.load(f)
            if findField(currJson, dic):
                data[dic].append(item)
                writeJson(currJson, data)
                return True
            else:
                print('no existe la libreria, debe crearla')
                return False
    else:
        return False



# ?                  ADD ITEM with Name list(Object in an Array)

def __addItemNamed(currJson: str, dic, item: dict, name: str = 'DefaultName'):
    if '.json' in currJson: print('lets find it')  
    else:
        currJson = currJson+'.json'  
    if findJson(currJson):
            f = open(currJson)
            data = json.load(f)
            if findField(currJson, dic):
                data[dic].append({
                    name:item
                })
                writeJson(currJson, data)
                return True
            else:
                return False
    else:
        return False


# ?                  DELETE ITEM(Object in an Array)

def delItem(currJson: str, itemListDel: str = None, itemValueDel: str = None, itemDict: dict = None):
    """Delete a item  to determinate dictionary
    --------------------

        REQUIRED currJson--> current Json File.

        dic='default' -> Dic name to add it. DEFAULT VALUE = 'default'

    REQUIRED  some of this options:
    
        itemListDel: str = None --> delete a item by name of the list that contains
        a particular dictionary
        
        itemValueDel: str = None --> delete a item that contains
        a particular value in it .
        
        itemDict: dict = None --> delete the itemDict if it´s in the Field.


        --------------------
    RETURN:

        TRUE -> correctly deleted

        FALSE -> it have an issue

    """
    if '.json' in currJson:
        print('finding...')  
    else:
        currJson = currJson+'.json'  
    if findJson(currJson):
        if itemDict:
            print('del by dict')  
        if itemValueDel:
            return __delValueItem(currJson, itemValueDel)
        if itemListDel:
            return __delListItem(currJson, itemListDel)

        return False
    else:
        return False


# ?                  DELETE ITEM by value(Object in an Array)

def __delValueItem(currJson: str, itemDel):
    if findJson(currJson):

        deleted= False
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)

            for element in data:
                for i in range(len(data[element])):
                        values = data[element][i]
                        for value in values.values():
                            if value == itemDel:
                                del data[element][i]
                                writeJson(currJson, data)
                                return True

        return False
    else:
        return False


# ?                  DELETE ITEM by list name(Object in an Array)

def __delListItem(currJson: str, itemDel):
    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)

            for element in data:
                for i in range(len(data[element])):
                    if itemDel in data[element][i]:
                        del data[element][i]
                        writeJson(currJson,data)
                        return True

        return False
    else:
        return False


# ?                  FIND ITEM

def findItem(currJson: str, itemList: str = None, itemValue: str = None, itemDict: dict = None):
    """Find a item  to a determinate Json
    --------------------

        REQUIRED currJson--> current Json File.

    REQUIRED  some of this options:
    
        itemListDel: str = None --> find a item by name of the list that contains
        a particular dictionary
        
        itemValueDel: str = None --> find a item that contains
        a particular value in it .
        
        itemDict: dict = None --> find the itemDict if it´s in the Field.

        --------------------
    RETURN:

        TRUE -> correctly deleted

        FALSE -> it have an issue

    """
    if '.json' in currJson:
        print('lets find it')  
    else:
        currJson = currJson+'.json'  
    if findJson(currJson):
        if itemDict: 
            return __findDictItem(currJson, itemDict)
        if itemValue:
            return __findValueItem(currJson, itemValue)
        if itemList:
            return __findListItem(currJson, itemList)
        return False
    else:
        return False


# ?                  FIND ITEM by value

def __findValueItem(currJson: str, item):

    numItems = 0
    if findJson(currJson):
        print(os.getcwd())
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            for element in data:
                for i in range(len(data[element])):
                    values = data[element][i]
                    for value in values.values():
                        if value == item:
                            numItems = numItems + 1
                            return values
                            

            if numItems > 0:
                print("Amount : ", numItems)
                return True
        print('no se encontro!')
        return None
    else:
        print('json not foud')
        return None


# ?                  FIND ITEM by list name

def __findListItem(currJson: str, item):
    numItems = 0

    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            if isEmptyJson(currJson): return False
            else:
                for element in data:
                    for i in range(len(data[element])):
                        if item in data[element][i]:
                            numItems = numItems + 1
                if numItems > 0:
                    return True
        return False
    else:
        return False


# ?                  FIND ITEM by dict

def __findDictItem(currJson:str, item):
    numItems = 0

    if findJson(currJson):
        with open(currJson, 'r') as data_file:
            data = json.load(data_file)
            for element in data:
                for dics in data[element]:
                    if item == dics:
                        numItems = numItems +1
            if numItems >0:
                return True
        return False

    else:
        return False


# ?                  EDIT ITEM

def editItem(currJson: str,dic:str='default', item:dict={}):
    if '.json' in currJson:
        print('finding...')  
    else:
        currJson = currJson+'.json'  
    if findJson(currJson):
        if findItem(currJson, itemValue= item['ID']):
            if delItem(currJson, itemValueDel=item['ID']):
                print('Item with ', item['ID'] , ' was deleted')
            else:
                return False
            if addItem(currJson,dic,item):
                return True
            else:
                return False
    else:
        return False

if 'data' in os.listdir(os.getcwd()):
    os.chdir('data')
else:
    os.mkdir('data')
    os.chdir('data')

