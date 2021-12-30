from cryptography.fernet import Fernet

def checkExistence(service, username, password):
                    
                f=open("secretKey.txt", "r")
                secretKey=f.readlines()
                f.close()
                strSecretKey=str(secretKey[0])
                secretKeyBytes=strSecretKey.encode()

                key = secretKeyBytes
                fernet = Fernet(key)

                f=open("encData.txt", "r")
                content = f.readlines()
                f.close()

                existent=False

                for i in range(0, len(content), 4):
                    
                    if content[i] != "\n":
                        strContentToken = content[i]
                        stripContentToken = strContentToken.strip()
                        encContentToken = stripContentToken.encode()
                        decContentToken1 = fernet.decrypt(encContentToken).decode()

                        if content[i+1] != "\n":
                            strContentToken = content[i+1]
                            stripContentToken = strContentToken.strip()
                            encContentToken = stripContentToken.encode()
                            decContentToken2 = fernet.decrypt(encContentToken).decode()

                            if content[i+2] != "\n":
                                strContentToken = content[i+2]
                                stripContentToken = strContentToken.strip()
                                encContentToken = stripContentToken.encode()
                                decContentToken3 = fernet.decrypt(encContentToken).decode()

                    if decContentToken1==service and decContentToken2==username and decContentToken3==password:
                        existent=True
                
                return existent