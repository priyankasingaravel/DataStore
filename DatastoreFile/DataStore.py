#import required packages
import sys
import time

#create a class
class DataStore: 
    #create a constructor for this class and add members to it
    def __init__(self):
        #dictionary to store key-value pair
    	self.jsonData = {}

    #create method to create and store key value pair in dictionary
    def create(self,key,value,timeout=0): 

        #check key is already present in dictionary
        if key in self.jsonData:
            print("Error:",key, "key is already present in data store")
        else:
            #check key does not contain any special characters or numbers
            if(key.isalpha()):

                #Length of the key
                keyLen = len(key)

                #size of the value in Bytes
                valueSize = sys.getsizeof(self.jsonData)

                #size of the dictionary in Bytes
                jsonFilesize = sys.getsizeof(self.jsonData)

                # To check key is less than or equal to 32 chars
                # To check value capped at 16KB
                # To check Dictionary which is storing data not exceeding 1GB
                if keyLen<=32 and valueSize<=16000 and jsonFilesize<=(1024*1024*1024):

                    #check timeout not equal to zero
                    if timeout!=0:

                        #store key-value in dictionary
                        #Add timeout value with current time  to set TTL property
                        self.jsonData[key] = [value, timeout+time.time()]
                        print("key", key," is created")
                    else:
                        #if time is zero store key-value in dictionary
                        self.jsonData[key] = [value, timeout]
                        print("key", key," is created")
                else:
                    #Shows error message if it exceeds memory Limit
                    print("Error:exceeds memory limit....")

            else:
                #Shows error message if key is invalid
                print("Error:Not a valid key...key must have only alphabets not special characters or numbers")


    #read method to display key-value pair
    def read(self,key):
         #check key in dictionary
    	 if key in self.jsonData:

            #Get the timeout value from the key 
    	 	Time = self.jsonData[key][1]

            #Check Time to live property
    	 	if Time!=0:

                #comparing present time with expiry time
    	 		if time.time()<Time:

                     #show key value pair if key is not expired
    	 			print(str(key)+":"+str(self.jsonData[key][0]))
    	 		else:
                     #Show error message if Time To Live for a key has expired
    	 			print("Error:",key, "key expired")
    	 	else:
                #Display the key value pair if timeout is zero
    	 		print(str(key)+":"+str(self.jsonData[key][0]))
    	 else:
            #Shows error message if key is not present
    	 	print("Error:",key, "key is not present in data store")
    
    
    #delete method to delete key-value pair
    def delete(self,key):

        #To check Key Present in Dictionary
        if key in self.jsonData:

            #Get the timeout value from the key 
            Time = self.jsonData[key][1]

            #Check Time to live property
            if Time!=0:
                #comparing present time with expiry time
                if time.time()<Time:
                    #delete key
                    del self.jsonData[key]
                    print(key, "key deleted")
                else:
                    #Show error message if Time To Live for a key has expired
                    print("Error:",key,"key expired")
            else:
                #Delete key if timeout is zero
                del self.jsonData[key]
                print(key, "key is deleted")
        else:
            #Shows error message if key is not present
            print("Error:",key,"key is not present in data store")



              
        
    	
    
   

        
        
        

    	  
