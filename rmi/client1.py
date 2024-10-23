import Pyro4

# The URI should be copied from the server output, or you can make it dynamic.
uri = "PYRO:obj_c76257cbd7944b3391c19c570683999a@localhost:53975"

# Connect to the remote object using the URI
remote_object = Pyro4.Proxy(uri)

# Call the remote method
response = remote_object.say_hello("John")
print(response)
