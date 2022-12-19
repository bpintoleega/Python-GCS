
from __future__ import print_function
import time
import os
from google.cloud import storage


# Authenticate ourselves using the service account private key
path_to_private_key = '/Users/brenocarlo/Downloads/leega-poc-delivery-inovacao-8629db90e865.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

def func(n):
    try:
        #filename = 'TaxiRider_20200103.csv.csv'
        filename = n
        bucket = storage.Bucket(client, 'teste-bucket-17dez-0823')
        # Name of the file on the GCS once uploaded
        blob = bucket.blob('LTV_GA' + filename + '.csv')
        # Path of the local file
        blob.upload_from_filename('/Users/brenocarlo/Documents/Python-GCS/Source/' + filename)
        print(filename)
    except:
        import traceback
        print(traceback.format_exc())

path_of_the_directory = '/Users/brenocarlo/Documents/Python-GCS/Source/'
object = os.scandir(path_of_the_directory)
for n in object :
    if n.is_dir() or n.is_file():
        #print(n.name)
        func(n.name)
        time.sleep(300)
object.close()






