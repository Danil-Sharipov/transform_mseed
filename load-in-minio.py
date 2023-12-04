import boto3

# Инициализация клиента S3
s3_client = boto3.client('s3',
                         endpoint_url='http://localhost:9000', 
                         aws_access_key_id='nWkSrEchrTAWItY4iAi7',
                         aws_secret_access_key='58KPiyb5FzqUb1euaEIFfTZ2caSRYZGwVvjxNK42')

# Создание бакета
bucket_name = 'my-test-bucket'
try:
    s3_client.create_bucket(Bucket=bucket_name)
except Exception:
    pass

# Загрузка файла в бакет
# s3_client.upload_file('../1-2.jpg', bucket_name, 'test.jpg')
from os import listdir
from os.path import isfile, join
mypath = './data/01'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
    s3_client.upload_file(mypath+'/'+i,bucket_name,i)