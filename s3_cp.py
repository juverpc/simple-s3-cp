import yaml
import os

def copy_model_from_s3():

    with open("./environment/dev/config.yml", 'r') as stream:
        get_value = yaml.load(stream)
        data_bucket= (get_value['data_bucket'])
        model_path= (get_value['model_path'])
        locations= (get_value['locations'])
    for restaurant in locations:
       #CHALLENGER
        os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/chal/"+" "+ "./lambdas/"+str(restaurant)+"-chal/model/"+" "+ "--recursive")
        os.system("tar xzvf"+" "+"./lambdas/"+str(restaurant)+"-chal/model/test.tar.gz"+" "+"-C"+" "+"./lambdas/"+str(restaurant)+"-chal/model/")
        os.system("rm -rf" +" "+"./lambdas/"+str(restaurant)+"-chal/model/test.tar.gz")
       #CHAMPION        
        os.system("aws s3 cp s3://"+str(data_bucket)+"/"+str(model_path)+"/"+str(restaurant)+"/champ/"+" "+ "./lambdas/"+str(restaurant)+"-champ/model/"+" "+ "--recursive")
        os.system("tar xzvf"+" "+"./lambdas/"+str(restaurant)+"-champ/model/test.tar.gz"+" "+"-C"+" "+"./lambdas/"+str(restaurant)+"-champ/model/")
        os.system("rm -rf" +" "+"./lambdas/"+str(restaurant)+"-champ/model/test.tar.gz")
     
if __name__ == "__main__":
    copy_model_from_s3()