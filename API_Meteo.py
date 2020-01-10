#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 14:18:42 2020

@author: fred
"""

import argparse
import requests

# =============================================================================
# Selction de la ville
# =============================================================================

def choix_ville():
    """
    Selection de la ville
    """
    
    print("-------------------------")
    ville = input("Choisissez une ville : ")
    print("-------------------------")
    ville = ville.capitalize()
    
    url = "https://api.meteo-concept.com/api/location/cities"
    params = {
        "token": "6f826b71898a5aba7ca0e17a00bf8890e01cfae5f262c65eb86d5fec38ad355a",
        "search": ville
    }
    
    r = requests.get(url, params=params)
    r = r.json()
    print(r)
    
    try:
        insee = r['cities'][0]["insee"]
        ville = r['cities'][0]["name"]
    except:
        print("La ville saisie n'existe pas")
        insee, ville = choix_ville()
    
    
    
    return insee, ville
    

# =============================================================================
# Affichage de la meteo
# =============================================================================

def affichage_meteo(insee):
    """
    Affichage de la meteo
    """

    url = "https://api.meteo-concept.com/api/forecast/daily"
    params = {
        "token": "6f826b71898a5aba7ca0e17a00bf8890e01cfae5f262c65eb86d5fec38ad355a",
        "insee": insee
        }
    
    r = requests.get(url, params=params)
    r = r.json()
    tmin = r["forecast"][0]["tmin"]
    tmax = r["forecast"][0]["tmax"]
    pluie = r["forecast"][0]["rr10"]
    
    return tmin, tmax, pluie


    


insee, ville = choix_ville()
tmin, tmax, pluie = affichage_meteo(insee)

print(f"Aujourd'hui à {ville}, la température minimale est de {tmin}, la maximale {tmax}")
if pluie >= 0:
    print(f"Le cumul de pluie sera de {pluie} mm")
else:
    print("Il ne devrait pas pleuvoir aujourd'hui")