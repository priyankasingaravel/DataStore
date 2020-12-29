import threading

# Import classes from your brand new package
from DataStore import DataStore

# Create an object of DataStore class & call its method
data = DataStore()

#create key without timeout
data.create("India","New Delhi")

#create key with timeout
data.create("Japan","Tokyo",300)

#create invalid key
data.create("@France","Paris",20)

#create already existing key
data.create("India","New Delhi")

#read key India
data.read("India")

#read key Japan
data.read("Japan")

#Japan key expires after 5 minutes or 300 seconds
data.read("Japan")

#read key not present in datastore
data.read("Germany")

#create new key
data.create("England","London",120)

#delete key India
data.delete("India")

#check delete operation of key India is performed
data.delete("India")

#England key expires after 2 minutes or 120 seconds
data.delete("England")

#Try to delete key not present in data store
data.delete("Fiji")

#Access the data store using multiple threads
 
#create key 
t = threading.Thread(target=data.create,args=("Egypt","Cairo",)) #without timeout
t1 = threading.Thread(target=data.create,args=("Italy","Rome",60)) #with timeout

#start the thread
t.start()
t1.start()

#read key
t = threading.Thread(target=data.read,args=("Egypt"))
t.start()

#delete key
t = threading.Thread(target=data.delete,args=("Egypt"))
t.start()

#thread t1 expires after 1 minute or 60 seconds
t1 = threading.Thread(target=data.read,args=("Italy"))
t1.start()
