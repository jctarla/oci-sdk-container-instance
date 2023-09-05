
import requests
import oci
import base64
import logging
from oci import Signer
import json


logging.getLogger('oci').setLevel(logging.DEBUG)

config = oci.config.from_file()  # Load the OCI configuration from a file
config['log_requests'] = True


auth = Signer(
tenancy=config['tenancy'],
user=config['user'],
fingerprint=config['fingerprint'],
private_key_file_location=config['key_file'],
pass_phrase=config['pass_phrase']
)

body_payload = {
    "containers": [
        {
            "imageUrl": "gru.ocir.io/xxxxxo/xxxxxa:latest",
            "displayName": "NewCreatedFromAPI2",
            "definedTags": {},
            "freeformTags": {}
        }
    ],
    "compartmentId": "ocid1.compartment.oc1..axxxx",
    "availabilityDomain": "LNlm:SA-SAOPAULO-1-AD-1",
    "shape": "CI.Standard.E3.Flex",
    "shapeConfig": {
        "ocpus": 1,
        "memoryInGBs": 1
    },
    "vnics": [
        {
            "subnetId": "ocid1.subnet.oc1.sa-saopaulo-1.xxxx",
            "displayName": "myVCNWiz"
        }
    ],
    "displayName": "NewCreatedFromAPID2"
}

headers = {'Content-Type': 'application/json'}

payload_json = json.dumps(body_payload)

response = requests.post('https://compute-containers.sa-saopaulo-1.oci.oraclecloud.com/20210415/containerInstances', data=payload_json, auth=auth, headers=headers)
response.raise_for_status()
print(response.json())


