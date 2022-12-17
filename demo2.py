from google.cloud import storage

# Authenticate ourselves using the service account private key
path_to_private_key = '/Users/brenocarlo/Downloads/leega-poc-delivery-inovacao-8629db90e865.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

#bucket = client.create_bucket('teste-bucket-17dez-0823')
#print(f'Bucket with name [{bucket.name}] created on GCS!')

bucket = storage.Bucket(client, 'teste-bucket-17dez-0823')
# Name of the file on the GCS once uploaded
blob = bucket.blob('LTV_GA.csv')
# Path of the local file
blob.upload_from_filename('/Users/brenocarlo/Downloads/LTV_GA.csv')