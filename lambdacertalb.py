import sys
import boto3
import json
import re


acm = boto3.client('acm')
## Get a list of Certificates in ACM
def lambda_handler(event, context):
    response = acm.list_certificates(
       CertificateStatuses=[
          'PENDING_VALIDATION','ISSUED','INACTIVE','EXPIRED','VALIDATION_TIMED_OUT','REVOKED','FAILED',
      ],
     Includes={
            'extendedKeyUsage': [
              'TLS_WEB_SERVER_AUTHENTICATION','TLS_WEB_CLIENT_AUTHENTICATION','CODE_SIGNING','EMAIL_PROTECTION','TIME_STAMPING','OCSP_SIGNING','IPSEC_END_SYSTEM','IPSEC_TUNNEL','IPSEC_USER','ANY','NONE','CUSTOM',
            ],
            'keyUsage': [
                'DIGITAL_SIGNATURE','NON_REPUDIATION','KEY_ENCIPHERMENT','DATA_ENCIPHERMENT','KEY_AGREEMENT','CERTIFICATE_SIGNING','CRL_SIGNING','ENCIPHER_ONLY','DECIPHER_ONLY','ANY',
            ],
            'keyTypes': [
                'RSA_1024','RSA_2048','RSA_3072','RSA_4096','EC_prime256v1','EC_secp384r1','EC_secp521r1',
            ]
        },
    )
## Spit out Certarn and DomainName pairs on new lines    
    print("Start Response Output: ")
    #print(type(response))
    #print(response)

## Take the contents of Response Trim off the Front and Back end of it, and then load the payload as a json object with CertificateArn and DomainName as keyvalue pairs
    #print ("Converting to json.")
    jsond_object = json.dumps(response) 
    #print(type(jsond_object))
    jsond_object = jsond_object[29:]
    jsond_object = jsond_object[:-600]
    #jsond_object = json.dumps(jsond_object)
    print(jsond_object)
