from xmlrpc.server import SimpleXMLRPCServer

# Define a simple class with methods that can be called remotely.
class RemoteClass:
    def say_hello(self, name):
        return f"Hello, {name} from the XML-RPC server!"

    def add_numbers(self, x, y):
        return x + y

# Create an XML-RPC server listening on localhost and port 9000.
def start_server():
    server = SimpleXMLRPCServer(("localhost", 9000))
    print("Server is listening on port 9000...")

    # Register an instance of the class so its methods can be called remotely.
    server.register_instance(RemoteClass())

    # Start the server and keep it running to listen for remote calls.
    server.serve_forever()

if __name__ == "__main__":
    start_server()
