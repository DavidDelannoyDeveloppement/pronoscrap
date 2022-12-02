print("")

import requests
from bs4 import BeautifulSoup

#Apport des couleurs
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
#


#Téléchargement des ressources
url_main_page = "https://www.pronosoft.com/fr/bookmakers/championnats/"
page = requests.get(url_main_page)
body = BeautifulSoup(page.content, "html.parser")



#Scraping
div_generale = body.find("div", class_ ="grid-cyb")
leagues = div_generale.find_all("h3", class_="league")
table_donnees = div_generale.find_all("div", class_ = "cyborg-d")
cyborg_m = div_generale.find_all("div", class_= "cyborg-m")




# Fonctions de vérification du nom de l'équipe :
def name_verif_dom(name_loc):
    #Ligue 1
    if name_loc[0] == "Paris":
        name = "Paris St-Germain"
        return name
    
    elif name_loc[0] == "Clermont":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join


    #Liga
    elif name_loc[0] == "Rayo":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "Athletic":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "Atletico":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join
    
    elif name_loc[0] == "Celta":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "FC":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "Real":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join


    #Premier League
    elif name_loc[0] == "Crystal":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "Aston":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "West":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[0] == "Manchester":
        name_loc_split = (name_loc[0:2])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join














    else:
        name = name_loc[0]
        return name





def name_verif_ext(name_loc):

    #Ligue 1
    if name_loc[-1] == "Germain":
        name = "Paris St-Germain"
        return name

    elif name_loc[-1] == "Foot":
        name = name_loc[-2]
        return name


    #Liga
    elif name_loc[-1] == "Vallecano":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[-1] == "Bilbao":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[-1] == "Madrid":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[-1] == "Vigo":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[-1] == "Séville":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[-1] == "Barcelone":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join

    elif name_loc[-1] == "Sociedad":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join


    #Premier League
    elif name_loc[-1] == "Palace":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join    

    elif name_loc[-1] == "Villa":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join 

    elif name_loc[-1] == "Ham":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join 

    elif name_loc[-1] == "Utd":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join 

    elif name_loc[-1] == "City":
        name_loc_split = (name_loc[-2:])
        name_loc_join = " ".join(name_loc_split)
        return name_loc_join 











    elif name_loc[-1] == "04":
        name = name_loc[-2]
        return name

    elif name_loc[-1] == "05":
        name = name_loc[-2]
        return name





    else:
        name = name_loc[-1]
        return name






#Fonction de tri et de comparaison des côtes et pourcentages de victoires

def leagues_et_matchs(leagues_loc, table_donnees_loc, cyborg_m_loc):

    for l in range(len(leagues_loc)):
        leagues_str = leagues[l].text
        leagues_split = leagues_str.split(" - ")
        print(f"{color.BOLD + color.CYAN}{leagues_split[0]}, {leagues_split[1]}{color.END}, matchs sélectionnés :")

        try:
            matchs = table_donnees_loc[l].find_all("td", class_="match")
            prono_cyb = cyborg_m_loc[l].find("ul", class_= "prono-cyb")
            cote_1 = prono_cyb.find_all("span", class_= "dev_span_1")
            cote_2 = prono_cyb.find_all("span", class_= "dev_span_2")
            
        except:
            print("Pas de match pour cette journée")
        
        else:

            for m in range(len(matchs)):
                # print(matchs[m].text)
                match_split = ((matchs[m].text).split(" "))

                #comparatif domicile

                try:
                    cote_1_m = cote_1[m].text
                    cote_split_str = cote_1_m.split(" ")
                    cote_split_float =float(cote_split_str[0].replace(',','.'))
                    pourcentage_1_str = cote_split_str[-1].replace('%','')
                    pourcentage_1_str_2 = pourcentage_1_str.replace('(','')
                    pourcentage_1_str_3 = pourcentage_1_str_2.replace(')','')
                    pourcentage_1_int = int(pourcentage_1_str_3)

                except:
                    cote_split_float = 10
                    #print("Pas de cote dispo pour ce match")
                else:
                    if cote_split_float <= cote_mini_float and pourcentage_1_int >= pourcentage_mini_int:
                        match_split_verif = name_verif_dom(match_split)
                        print(f"{color.BOLD}{match_split_verif} (Domicile){color.END}")
                
                


                #comparatif extérieur

                try:
                    cote_2_m = cote_2[m].text
                    cote_split_str = cote_2_m.split(" ")
                    cote_split_float =float(cote_split_str[0].replace(',','.'))
                    pourcentage_1_str = cote_split_str[-1].replace('%','')
                    pourcentage_1_str_2 = pourcentage_1_str.replace('(','')
                    pourcentage_1_str_3 = pourcentage_1_str_2.replace(')','')
                    pourcentage_1_int = int(pourcentage_1_str_3)
                    
                except:
                    cote_split_float = 10
                    #print("Pas de cote dispo pour ce match")
                else:
                    if cote_split_float <= cote_mini_float and pourcentage_1_int >= pourcentage_mini_int:
                        match_split_verif = name_verif_ext(match_split)                        
                        print(f"{match_split_verif} (Extérieur)")


        print("")
        print("")





#Demandes user
cote_mini_str = input("Côte minimum demandée ? ")
cote_mini_float = float(cote_mini_str)

pourcentage_mini_str = input("% minimum demandé ? ")
pourcentage_mini_int = int(pourcentage_mini_str)

demande_ext_str = input("Sélectionner aussi les équipes favorites à l'extérieur (o/n)? ")
print("")

print(leagues_et_matchs(leagues, table_donnees, cyborg_m ))



print("")