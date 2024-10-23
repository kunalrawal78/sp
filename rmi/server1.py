import Pyro4

# This is a simple class that we'll expose to remote calls.
@Pyro4.expose
class RemoteClass:
    def say_hello(self, name):
        return f"Hello, {name} from the remote object!"

# The Pyro daemon will make this class available to the client over the network.
def start_server():
    # Start Pyro4 daemon
    daemon = Pyro4.Daemon()

    # Register the class with Pyro4
    uri = daemon.register(RemoteClass)

    # Print the URI so that the client can connect to this object
    print(f"Ready. Object URI: {uri}")

    # Start the event loop of the server to wait for incoming requests
    daemon.requestLoop()

if __name__ == "__main__":
    start_server()
