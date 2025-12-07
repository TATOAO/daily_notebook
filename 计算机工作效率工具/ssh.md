

## find port in current ssh $ grep -i port /etc/ssh/sshd_config.




## rsa method

https://chatgpt.com/share/6746e076-a15c-8000-b8a3-04c84f48391c

```bash

ssh-keygen -t rsa -b 4096 -C "My Work Key"
ssh-keygen -t ed25519 -C "your_email@example.com"
# create the private key in ~/.ssh/id_rsa

ssh-copy-id -p $port_num username@server_ip
# copy the public key into the server

ssh -p $port_num username@server_ip

```

## how it works


Step 1: Server Challenges the Client
The server checks if your username has an associated public key in the ~/.ssh/authorized_keys file.
If a public key is found, the server generates a random challenge message (a large number) and encrypts it using the public key.

Step 2: Client Proves Ownership of the Private Key
The encrypted challenge message is sent back to your local machine.
Your SSH client uses the private key to decrypt the challenge message, proving that it has the corresponding private key.

Step 3: Client Sends the Response
After decrypting the challenge, the SSH client sends the original challenge message (now decrypted) back to the server.

Step 4: Server Verifies the Response
The server compares the decrypted response with the original challenge message.
If they match, the server is assured that the client has the correct private key and allows the connection.



# if ssh-copy-id is Not Available


Display the Public Key:

bash
Copy code
```
cat ~/.ssh/id_rsa.pub
```
Log in to the Server Using the Custom Port:

bash
Copy code
```
ssh -p 12345 username@server_ip
```
Add the Public Key to the Server:

Create or edit the ~/.ssh/authorized_keys file on the server:
bash
Copy code
```
vi ~/.ssh/authorized_keys
```
Paste the public key into the file.
Save and exit.
Set Permissions:

bash
Copy code
```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```



# SSH 隧道转发和反向



