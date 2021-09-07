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
        os.system("cd"+" "+"./lambdas/"+str(restaurant)+"-chal/model/")
        os.system("tar xzvf test.tar.gz")
        os.system("rm -rf test.tar.gz ")
        os.system("ls")
        os.system("cd ..")
        os.system("cd ..")
        os.system("cd ..")
        
        os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/champ/"+" "+ "./lambdas/"+str(restaurant)+"-champ/model/"+" "+ "--recursive")
        os.system("cd"+" "+ "./lambdas/"+str(restaurant)+"-champ/model/")
        os.system("tar xzvf test.tar.gz")
        os.system("rm -rf test.tar.gz ")
        os.system("cd ..")
        os.system("cd ..")
        os.system("cd ..")

if __name__ == "__main__":
    read_yaml_file()