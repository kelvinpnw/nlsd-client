ingest_server = 'https://nlsd-ingest.example.com'
print('set ingest server to ' + ingest_server)
# Get server auth key
# authkey = 'your-key-here'
infile = open('/home/nlsd/key', 'r')
authkey = infile.readline()

# Imports for Libraries
import sys
import base64
import requests
from sh import tail

for line in tail("-F", "/var/log/ufw.log", _iter=True):
    # Encode in base64 for transport
    log_line_encoded = base64.b64encode(line)
    payload = {'key': authkey, 'log': log_line_encoded}
    r = requests.post(ingest_server + '/api/nlsingest/logevent', params=payload)
    print(r.text)
