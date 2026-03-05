#https://machinelearningmastery.com/building-a-simple-mcp-server-in-python/

How to see what everything your server offers (tools, resources, and prompts) is the list command: 
fastmcp list my_server.py

fastmcp list my_server.py --resources
fastmcp list my_server.py --prompts

using key:value
fastmcp call my_server.py add a=10 b=5
fastmcp call my_server.py greet name=Rudi


using json format
fastmcp call my_server.py greet '{"name": "Rudi"}'
fastmcp call my_server.py add '{"a": 10, "b": 5}'

