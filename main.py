import copy

passager = {
    "id" : 0,
    "name" : "",
    "kg" : 0
}

bus = {
    "idBus" : 0,
    "nberPlace" : 0
}
voyage = {
    "newId" : "",
    "newIdBus" : ""
}

passengerList = []
busList = []
voyageTab = []

def addBus() :
    isAddBus = False
    while isAddBus != True:
        idBus=input("Entrer l'immatriculation du Bus___")
        nberPlace=int(input("Entrer le nombre de places du BUS___"))
        #passagerList=input("Entrer la liste des passagers___")
        print("---")
        print("Opération réussie !")
        print("---")
        print(f'immatriculation: {idBus}, Nombre de places: {nberPlace}' )
        print("---")
        currentBus = copy.deepcopy(bus)
        currentBus["idBus"]=idBus
        currentBus["nberPlace"]=nberPlace
        busList.append(currentBus)
        choix = input("Ajouter un autre Bus ? o ou n___")
        if choix == "n":
            isAddBus = True
#    print(busList)

def addPassager() :
    isAddPassager = False
    while isAddPassager != True:
        id=input("Entrer le numéro de CNI du passager___")
        kg=int(input("Entrer le nombre de kg de bagages___"))
        name=input("Entrer le nom du passager___")
        print("---")
        print("Opération réussie !")
        print("---")
        print(f'Nom: {name}, Nombre de kg: {kg}, Numéro de CNI: {id}' )
        currentPassager = copy.deepcopy(passager)
        currentPassager["id"]=id
        currentPassager["kg"]=kg
        currentPassager["name"]=name
        passengerList.append(currentPassager)
        choix = input("Ajouter un autre passager ? o ou n___ ")
        if choix == "n":
            isAddPassager = True
        print("---")           

def matchPassagerToBus():
    getAllPassager()
    newId=input("Selectionner l'id du passager à ajouter à un bus ___ ")
    getAllBus()
    newIdBus = input("Selectionner l'id du bus ___ ")
    #voyageTab = [ newId, newIdBus ]
    print(f'Passager: {newId}, Bus N°: {newIdBus}' )
    currentVoyage = copy.deepcopy(voyage)
    currentVoyage[ "newId" ] = newId
    currentVoyage[ "newIdBus" ] = newIdBus
    voyageTab.append(currentVoyage)
    print(voyageTab)
    
    
def getPlaceAvailable():
    getAllBus()
    newIdBus = input("Selectionner l'id du bus ___ ")
    for voyage in voyageTab:
        if voyage["newIdBus"] == newIdBus:
            print("Nombre de passagers pour ce bus: {} !".format(len(voyage)))
    for bus in busList:
        if bus["idBus"] == newIdBus:
            print("Capacité du bus : {} ".format(bus["nberPlace"]))
        placeAvailable = bus["nberPlace"] - len(voyage)
        print("Le nombre de places disponible est de : {} !".format(placeAvailable))
            


# def getKg():

# def movePassagerToBus():

def getPassagerListInBus():
    getAllBus()
    newIdBus = input("Selectionner l'id du bus ___ ")
    for voyage in voyageTab:
        if voyage["newIdBus"] == newIdBus:
            print (voyage)


def getAllPassager():
    for val in passengerList:
        print(val)

def getAllBus():
    for val in busList:
        print(val)

def findPassagerBus():
    newId=input("Entrer le numéro de CNI du passager recherché___")
    for passager in passengerList:
        if passager["id"] == newId:
            print("le passager existe")
        # else:
        #     print("Le passager n'existe pas")
    for voyage in voyageTab:
        if voyage["newId"] == newId:
            print("___")
            print(voyage)
        else:
            print("Le passager n'a pas de bus")


isGuessRight = False
multiligne = """1. Ajouter un bus
2. Ajouter un passager
3. Ajouter un passager à un bus
4. Verifier le nombre place disponible sur un bus
5. Vérifier la charge d'un bus
6. Retirer un passager à un bus
7. Consulter le nombre de place libre par bus
8. Liste des passagers par bus
9. Liste de tous les passagers
10. Chercher un passager et avoir son bus
""" 
while isGuessRight != True:
    print("         °__^__°           ")
    print(multiligne)
    print("---")
    choix=input( "choix ___" )
    if choix == "1":
        addBus()
    elif choix == "2":
        addPassager()
    elif choix == "3":
        matchPassagerToBus()
    elif choix == "4":
        getPlaceAvailable()
    elif choix == "8":
        getPassagerListInBus()
    elif choix == "9":
        getAllPassager()
    elif choix == "10":
        findPassagerBus()
    else :
        isGuessRight = True
    
    # voyage = matchPassagerToBus(passager, bus)
    # print(voyage)

