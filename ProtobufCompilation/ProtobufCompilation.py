
import os
from subprocess import Popen

# Ensure that proto.exe is in the directory of this file and protos exists in object_detection

# Grabbing directories
curDir = os.getcwd()
PROTO_PATH = curDir + "/object_detection/protos"

# Executing proto on all .proto files
for path, dirs, files in os.walk(PROTO_PATH):
    for filename in files:
        filestr = filename.split('.')
        if (filestr[1] == "proto"):
            print("executing on file: " + filename)
            process = Popen('protoc object_detection/protos/' + filename + ' --python_out=.')
        else:
            print("ignored file: " + filename)