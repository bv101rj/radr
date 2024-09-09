#!/bin/python3

import requests
import json 
import os
import subprocess

def get_gif(site):
    
    #URL that the loop gif is at1
    url = "https://radar.weather.gov/ridge/standard/{site_code}_loop.gif".format(site_code=site)

    #Get a response from the server
    response = requests.get(url, stream=True)

    #Place the GIF in tmp
    local_file = os.path.join("/tmp", "radar.gif")

    #Open and write the data
    with open(local_file, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    return local_file 

def loop_gif(local_file):
    #Takes local file as input, loops over it with mpv 
    command = "mpv /tmp/radar.gif --loop=inf --no-border --osc=no"

    #Loop using mpv
    process = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def config(home_dir, config_dir, config_file_path):
    
    # Get user input
    print(f"You can navigate to radar.weather.gov you need to find your local station, upper left hand corner symbol looks like a copy button, select local, click on what is close to you, it should have a 4 letter code")
    radar_location = input("Paste the that 4 letter code here: ")
    
    #Create a place to save the config json
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config", "radr")
    os.makedirs(config_dir, exist_ok=True)
    config_file_path = os.path.join(config_dir, "config.json")
    
    #Save the info to a json 
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
    
    #Map out storage location 
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(home_dir, ".config", "radr")
    config_file_path = os.path.join(config_dir, "config.json")
    
    #Check if we are configured
    cfig = check_config(config_file_path)

    # If we cfig is None, run the config, only will happen once. 
    if cfig == None :
        config(home_dir, config_dir, config_file_path)
    else :
        #Get out loop gif for a given radar station. 
        file = get_gif(cfig[1])
        loop_gif(file)

if __name__ == "__main__":
    main()
