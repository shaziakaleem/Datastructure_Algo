class HashTable:
    def __init__(self,size):
        self.size = size
        self.slots = None
        self.data = None
    
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue]==None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue] = 11
            else:
                nextslot =  self.rehash(hashvalue,len(self.slots))
                while nextslot!=None and self.slots[nextslot]!==key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                slots[nextslot] = key
                data[nextslot] =  data
                
    def get(self,key):
        hashvalue = self.hashfunction(key,len(self.slots))
        found= False
        stop = False
        startslot=nextslot=hashvalue
        if self.slots[hashvalue]==key:
            data = self.data[hashvalue]
        else:
            while nextslot!=None and not stop and not found:
                if self.slots[nextslot]!=key:
                    nextslot = self.rehash(startslot,len(self.slots))
                else:
                    found = stop =True
                    data = self.data[nextslot]
        return data
    
     def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)




