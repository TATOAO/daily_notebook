import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription

async def hello_world():
    # Create two local RTCPeerConnections (pc1 and pc2).
    pc1 = RTCPeerConnection()
    pc2 = RTCPeerConnection()

    # Create a data channel on pc1.
    channel = pc1.createDataChannel("chat")

    @channel.on("open")
    def on_open():
        print("DataChannel (pc1->pc2) is open.")
        # Send a greeting from pc1 to pc2.
        channel.send("Hello from pc1!")

    @channel.on("message")
    def on_message(message):
        print("pc1 received message:", message)

    # When pc2 sees a data channel, set up a handler for incoming messages.
    @pc2.on("datachannel")
    def on_datachannel(channel):
        print("pc2 detected a DataChannel.")
        @channel.on("message")
        def on_message(message):
            print("pc2 received message:", message)
            channel.send("Hello back from pc2!")

    # --- Exchange Offer/Answer ---

    # 1. pc1 creates an offer and sets its local description.
    offer = await pc1.createOffer()
    await pc1.setLocalDescription(offer)

    # 2. pc2 receives that offer as its remote description.
    await pc2.setRemoteDescription(pc1.localDescription)

    # 3. pc2 creates an answer, sets local description.
    answer = await pc2.createAnswer()
    await pc2.setLocalDescription(answer)

    # 4. pc1 receives pc2's answer as its remote description.
    await pc1.setRemoteDescription(pc2.localDescription)

    # Give some time for ICE gathering + messaging.
    await asyncio.sleep(5)

    # Clean up.
    print("Closing the peer connections.")
    await pc1.close()
    await pc2.close()

if __name__ == "__main__":
    asyncio.run(hello_world())

