from datetime import datetime, timedelta
import time
import traceback
import os
import io
from typing import final
import unittest                 # https://docs.python.org/3/library/unittest.html
from owlready2 import *         # https://pypi.org/project/Owlready2/

def main():
    
    try:
        
        myworld = World(filename='backup.db', exclusive=False)
        
        #onto_path.append(os.path.dirname(__file__))
        
        # aqui a KIPO e a Ontologia do Scrum tiveram um Merge!
        kiposcrum = myworld.get_ontology(os.path.dirname(__file__) + '/kiposcrum_pellet.owl').load()
        
    except:
        
        print("Erro no começo")
    
    print("\n------------------------------------\n")
    
    sync_reasoner()
    
    try:
        
        with kiposcrum:
            
            #print("KIPCO__Agent is a...")
            #print( str(kiposcrum["KIPCO__Agent"].is_a) + "\n")
            
            print("KIPCO__Agent instances...")
            print( str(kiposcrum["KIPCO__Agent"].instances()) + "\n")
            
            print("Commited_Team_Member is a...")
            print( str(kiposcrum["Commited_Team_Member"].is_a) + "\n")
            
            myworld.close()
            
            # print( kiposcrum["KIPCO__Agent"].instances() )
    except:
        
        print("Erro na leitura")
    
    finally:
        
        print("\n------------------------------------\n")
    
if __name__ == '__main__':
    
    main()