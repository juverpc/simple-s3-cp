import yaml
import os

def read_yaml_file():

    with open("./environment/dev/config.yml", 'r') as stream:
        get_value = yaml.load(stream)
        data_bucket= (get_value['data_bucket'])
        model_path= (get_value['model_path'])
        locations= (get_value['locations'])
    for restaurant in locations:
        os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/chal/"+" "+ "./lambdas/"+str(restaurant)+"-chal/model/"+" "+ "--recursive")
        os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/champ/"+" "+ "./lambdas/"+str(restaurant)+"-champ/model/"+" "+ "--recursive")
        
      

if __name__ == "__main__":
    read_yaml_file()