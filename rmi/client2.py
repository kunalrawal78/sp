import xmlrpc.client

# Connect to the XML-RPC server (replace 'localhost' if the server is on a different machine)
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

# Call the remote method 'say_hello'
response_hello = proxy.say_hello("John")
print(response_hello)

# Call another remote method 'add_numbers'
response_add = proxy.add_numbers(5, 7)
print(f"The sum of 5 and 7 is: {response_add}")
