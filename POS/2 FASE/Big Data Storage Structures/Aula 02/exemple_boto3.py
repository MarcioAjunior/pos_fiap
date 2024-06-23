import boto3
from botocore.exceptions import NoCredentialsError

def handle_s3(file_name, bucket, action, object_name=None, prefix=None):
    
    session = boto3.Session(
        keys_aws
    )
    s3_client = session.client('s3')

    try:
        if action == 'upload':
            if object_name is None:
                object_name = file_name.split('/')[-1]
            if prefix:
                object_name = f"{prefix}/{object_name}"
            s3_client.upload_file(file_name, bucket, object_name)
        elif action == 'delete':
            if object_name is None or prefix:
                raise ValueError("Para deletar um objeto, o 'object_name' deve ser especificado e 'prefix' deve ser None ou vazio.")
            s3_client.delete_object(Bucket=bucket, Key=object_name)
        elif action == 'list':
            paginator = s3_client.get_paginator('list_objects_v2')
            for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
                for obj in page.get('Contents', []):
                    print(obj['Key'])
        else:
            print(f"Ação '{action}' não reconhecida.")
            return False
    except NoCredentialsError:
        print("As credenciais não estão disponíveis")
        return False
    except ValueError as ve:
        print(ve)
        return False
    except Exception as e:
        print(f"Erro ao realizar ação '{action}' no arquivo: {e}")
        return False

    return True

if __name__ == '__main__':

    #Exemplo de uso para upload:
    handle_s3(r'C:\Users\marci\TESTE_AWS.txt',\
            'fiap-2024-marcio-luz-mlet',\
            'upload',\
            'TESTE_AWS.txt',\
            'script_aula_01')


    #Exemplo de uso para listagem:
    handle_s3(None,\
            'fiap-2024-marcio-luz-mlet',\
            'list',\
            prefix='script_aula_01')