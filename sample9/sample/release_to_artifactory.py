#!/usr/bin/python3
"""
Please enter the release version such as below:
SDK_VERSION= DATA_VERSION= CUR_DATE= ./release_to_artifactory.py
"""

import requests
import os
import sys

ARTI_TO_REPO = ""
if os.environ.get("ARTIFACTORY_TO_REPO"):
    ARTI_TO_REPO = os.environ["ARTIFACTORY_TO_REPO"]
ARTI_TO_COMPONENT_PATH = "tmp"
if os.environ.get("ARTIFACTORY_TO_COMPONENT_PATH"):
    ARTI_TO_COMPONENT_PATH = os.environ["ARTIFACTORY_TO_COMPONENT_PATH"]
ARTI_TO_URL = ""
ARTI_TO_USER = ""
ARTI_TO_PASS = ""

SDK_VERSION=""
DATA_VERSION=""
CUR_DATE=""

class upload_in_chunks(object):
    def __init__(self, filename, chunksize=1 << 13):
        self.filename = filename
        self.chunksize = chunksize
        self.totalsize = os.path.getsize(filename)
        self.readsofar = 0
    def __iter__(self):
        with open(self.filename, 'rb') as file:
            while True:
                data = file.read(self.chunksize)
                if not data:
                    sys.stderr.write("\n")
                    break
                self.readsofar += len(data)
                percent = self.readsofar * 1e2 / self.totalsize
                sys.stderr.write("\r{percent:3.0f}%".format(percent=percent))
                yield data
    def __len__(self):
        return self.totalsize

def deploy_artifactory(filepath, arti_to_path_component, newFilename=""):
    file_name = os.path.basename(filepath)
    if len(newFilename):
        print("receive new filename: ", newFilename)
        file_name = newFilename
    full_url = f"{ARTI_TO_URL}/{ARTI_TO_REPO}/{ARTI_TO_COMPONENT_PATH}/{arti_to_path_component}/{file_name}"
    print(f"url: {full_url}")
    if not len(ARTI_TO_PASS):
        print("env ARTI_TO_PASS is missing, which are required!")
        sys.exit(1)

    try:
        response = requests.put(full_url, data=upload_in_chunks(filepath, chunksize=10), auth=(ARTI_TO_USER, ARTI_TO_PASS))
        if response.status_code < 300:
            print("upload {} to artifactory successfully!".format(file_name))
        elif response.status_code == 403:
            print(f"upload {file_name} to artifactory already exists!")
        else:
            print("upload {} to artifactory failed! status code = {}".format(file_name, response.status_code))
    except Exception as e:
        print("requests put meet error: ", e)

if __name__ == '__main__':
    if os.environ.get("SDK_VERSION"):
        SDK_VERSION = os.environ["SDK_VERSION"]
    if os.environ.get("DATA_VERSION"):
        DATA_VERSION = os.environ["DATA_VERSION"]
    if os.environ.get("CUR_DATE"):
        CUR_DATE = os.environ["CUR_DATE"]

    if not len(SDK_VERSION) or not len(DATA_VERSION) or not len(CUR_DATE):
        print("SDK_VERSION or DATA_VERSION or CUR_DATE is missing, all of them are required!")
        sys.exit(1)

    if os.environ.get("ARTIFACTORY_TO_USER"):
        ARTI_TO_USER = os.environ["ARTIFACTORY_TO_USER"]
    if os.environ.get("ARTIFACTORY_TO_PASS"):
        ARTI_TO_PASS = os.environ["ARTIFACTORY_TO_PASS"]

    print("deploying data txt...")
    dp_txt = f"asdk/data/data.txt"
    deploy_artifactory(dp_txt, f"rls/{CUR_DATE}/{DATA_VERSION}")
    print("deploying sdk txt...")
    sdk_txt = f"asdk/sdk.txt"
    deploy_artifactory(sdk_txt, f"rls/{CUR_DATE}/{SDK_VERSION}")

    print("deploy task done!")
