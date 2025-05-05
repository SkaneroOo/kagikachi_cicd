from websockets.sync.client import connect

try:
    with connect("ws://localhost:7878/") as client:

        client.ping()
        # client.send("set x 1", True)      # protocol is not yet fully implemented on server
        # resp = client.recv()
        # print(resp)
        client.close_socket()

except Exception as e:
    print(e)