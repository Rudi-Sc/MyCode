#https://machinelearningmastery.com/building-a-simple-mcp-server-in-python/

using key:value
fastmcp call my_server.py add '{"a": 10, "b": 5}'
fastmcp call my_server.py add a=10 b=5

using json format
fastmcp call my_server.py greet name=Rudi
fastmcp call my_server.py greet '{"name": "Rudi"}'

