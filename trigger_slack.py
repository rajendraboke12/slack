from slackclient import SlackClient
from pprint import pprint
import logging
import yaml

with open("configfile.yml","r") as configfile:
    config=yaml.load(configfile)
    apikey=config["apikey"]

def write(inward_arr,var_arr):
    try:
        for i in inward_arr:
            var_arr[0] = str(var_arr[0]).strip()
            mylist = var_arr[0].split(',')
            i["$channel"]=mylist[0]
            i["$msg"]=mylist[1]
            sc = SlackClient(apikey)
            sc.api_call(
                "chat.postMessage",
                channel=i["$channel"],
                text=i["$msg"]
                )
    except Exception,ex:
        i["$ERROR"]="something error is happened"
        logging.error("Exception : "+ex)
    outward_arr=inward_arr
    return outward_arr

inward_arr=[{"$intelref":"greenshow","$violationfield":"source"}]
var_arr=["#development,Source IP 192.168.0.98 Hello from bot"]
outward_arr=write(inward_arr,var_arr)
pprint(outward_arr)
