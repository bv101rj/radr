#!/bin/python3

import requests
import json 
import os
import 


def get_gif():


def config(home_dir, config_dir, config_file_path):
    # Get user input
    print(f"You can navigate to radar.weather.gov you need to find your local station, upper left hand corner symbol looks like a copy button select local, click on what is close to you, it should have a 4 letter code")
    radar_location = input("Paste the that code here: ")
    
    #Create a place to save the config json
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config", "radr")
    os.makedirs(config_dir, exist_ok=True)
    config_file_path = os.path.join(config_dir, "config.json")

    config_data = {
            "configured": True,
            "radar_loc": radar_location,
    }
    
    with open(config_file_path, "w") as config_file:
        json.dump(config_data, config_file, indent=4)

    print(f"Config saved to {config_file_path}")

def check_config(config_file_path):
    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as config_file:
            config_data = json.load(config_file)
        if config_data.get("configured") is True:
            return (True, config_data.get("radar_loc"))
        else:
            return None 

def main():
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config", "radr")
    config_file_path = os.path.join(config_dir, "config.json")
    cfig = check_config

    if cfig == None :
        config(home_dir, config_dir, config_file_path)

    else :
        get_gif()

