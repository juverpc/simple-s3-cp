import yaml
from yaml import Loader
import os

def copy_model_from_s3():

    with open("./environment/dev/config.yml", 'r') as stream:
        get_value = yaml.load(stream,Loader=Loader)
        data_bucket= (get_value['data_bucket'])
        model_path= (get_value['model_path'])
        locations= (get_value['locations'])
    
   
    for restaurant,stand_menus in locations.items():
        for menu in stand_menus['stand_menus']:
                     
        #CHALLENGER
        #auto_training_pipeline/deployed_models/+str(restaurant)+/stand_menu/
            os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/challenger_model/stand_menu_"+str(menu)+" "+ "./lambdas/"+str(restaurant)+"-chal/model/"+" "+ "--recursive")
            os.system("tar xzvf"+" "+"./lambdas/"+str(restaurant)+"-chal/model/model.tar.gz"+" "+"-C"+" "+"./lambdas/"+str(restaurant)+"-chal/model/")
            os.system("rm -rf" +" "+"./lambdas/"+str(restaurant)+"-chal/model/model.tar.gz")
        #CHAMPION        
            os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/champion_model/stand_menu_"+str(menu)+" "+ "./lambdas/"+str(restaurant)+"-champ/model/"+" "+ "--recursive")
            os.system("tar xzvf"+" "+"./lambdas/"+str(restaurant)+"-champ/model/model.tar.gz"+" "+"-C"+" "+"./lambdas/"+str(restaurant)+"-champ/model/")
            os.system("rm -rf" +" "+"./lambdas/"+str(restaurant)+"-champ/model/model.tar.gz")
     
if __name__ == "__main__":
    copy_model_from_s3()