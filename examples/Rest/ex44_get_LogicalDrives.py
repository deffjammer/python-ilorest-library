# Copyright 2016 Hewlett Packard Enterprise Development, LP.
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.

import sys
from restobject import RestObject

def ex44_get_LogicalDrives(restobj):

    sys.stdout.write("\nEXAMPLE 44: Dump LogicalDrivese details\n")
    instances = restobj.search_for_type("HpSmartStorageArrayController.")

    for instance in instances:
        response = restobj.rest_get(instance["href"])
        if "ArrayControllers" in response.dict:
            sys.stdout.write("\tArrayControllers:  " +
                           str(response.dict["ArrayControllers"]) + "\n")
        else:
            sys.stderr.write("\tArrayControllers is not " \
                        "available on HpSmartStorageArrayController resource\n")

if __name__ == "__main__":
 
    iLO_host = "https://10.0.0.100"
    iLO_account =  "admin"
    iLO_password =  "password"
    
    # Create a REST object
    REST_OBJ = RestObject(iLO_host, iLO_account, iLO_password)
    ex44_get_LogicalDrives(REST_OBJ)



