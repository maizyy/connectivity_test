#!/usr/bin/env python3
"""
Connection test script
"""

import json
import subprocess
import platform

report= open(f"{platform.node()}_report.txt", "w")

def load_config():
   with open("config.json", "r") as config:
      return json.load(config)

def handle_service(service,data):
   addresses=data["addresses"].split(" ")
   ports=data["ports"].split(" ")
   report.write(f'{service}\n')
   for address in addresses:
      for port in ports:
         if 'udp' in data:
            command=f'nc -vzu {address} {port}'
         else:
            command=f'nc -vz {address} {port}'
         result = subprocess.run(command,shell=True)
         report.write(f'{command} ---> {result.returncode}\n')

def test(cfg):
   report.write(f'Report from : {platform.node()}\n')
   for service in cfg:
      if not 'skip' in cfg[service]:
         handle_service(service,cfg[service])
   report.close()


def main():
   cfg = load_config()
   test(cfg)

if __name__ == "__main__":
    main()