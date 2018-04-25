# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 11:51:07 2018

@author: ABIOYE OYETUNJI
"""
#importing hashlib, datetime and pickle
import hashlib
import datetime
import pickle




# Creating the block class


class block:
    
    # the constructor method holds all the information for the block 
    def __init__(self,index,data,timestamp,previous_hash):
        self.index = index
        self.data = data
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.current_hash()
    
    # this is where i hashed all the information in the block using the pickle 
    # module to encode it first
    def current_hash(self):
        #using sha256, same encryption used in bitcoin 
        hashed_block = hashlib.sha256()
        
        pickled = pickle.dumps(str(self.index)+
                str(self.data)+
                str(self.timestamp)+
                str(self.previous_hash)+
                str(self.nonce))
        
        hashed_block.update(pickled)
        
        return hashed_block.hexdigest()
    
    # this method mine_a_block takes in the object self and the difficulty 
    # the difficulty is a standard that the hashed block must meet before it
    # can be added to the blockchain
    def mine_a_block(self, difficulty):
        while(self.hash[:difficulty] != "0"*difficulty):
            self.hash = self.current_hash()
            self.nonce+=1
        return self.hash
    
    def check_mined(self, difficulty):
        new_hash =""
        self.nonce =0
        while(new_hash[:difficulty] != "0"*difficulty):
            new_hash = self.current_hash()
            self.nonce +=1
        return new_hash
    
    
     
    
    # the blockchain class inherits from the block class
class blockchain(block):
    # the constructor method here declares a list which only contains the genesis block
    # and sets the variable difficulty to 3
    def __init__(self):
        self.blockchain = [self.genesis_block()]
        self.difficulty = 3
        
    # when creating the genesis block the index is of course 0, the data is genesisblock just for show
    # the timestamp using the datetime module previously imported to get the current  time
    def genesis_block(self):
        return block(0,"Genesisblock",datetime.datetime.now(),"0")
    
    # the current block is the last block before the new block to be added therefore 
    # the lenght of the blockchain - 1
    def get_current_block(self):
        return self.blockchain[len(self.blockchain) - 1 ]
    
    # here we set the new blocks previous hash to that of the current block and make sure the 
    # current block meets the difficulty set, then append it to the blockchain list and print 
    # out the new blocks hash just for show
    def add_new_block(self, new_block):
        new_block.previous_hash = self.get_current_block().hash
        new_block.mine_a_block(self.difficulty)
        self.blockchain.append(new_block)
        print(new_block.hash)
        
    # prints the informaion inside the block and the hashes
    def print_blockchain(self):
        print("Starting blockchain..... ")
        print("Block num...",self.blockchain[0].index, "data:", self.blockchain[0].data)
        print("Previous Hash...", self.blockchain[0].previous_hash)
        print("current Hash ...", self.blockchain[0].current_hash())
        for i in range(1, len(self.blockchain)):
            print("Block num...",self.blockchain[i].index, "data:", self.blockchain[i].data)
            print("Previous Hash...", self.blockchain[i].previous_hash)
            print("current Hash ...", self.blockchain[i].mine_a_block(self.difficulty))
    
    # a simple check to know if the blocks have been tampered with
    def is_a_validchain(self):
        for i in range(1, len(self.blockchain)):
            if self.blockchain[i].hash != self.blockchain[i].check_mined(self.difficulty):
                print("current hash", self.blockchain[i].hash,"does not match",self.blockchain[i].check_mined(self.difficulty))
                return False
            elif self.blockchain[i-1].hash != self.blockchain[i].previous_hash:
                print("previous hash", self.blockchain[i-1].hash,"does not match with the attr previous hash", self.blockchain[i].previous_hash )
                return False
        return True 
    
      
tj_coin = blockchain()


print("Mining block 1....")
tj_coin.add_new_block(block("1","50","20/4/2018","0"))
print("Mining block 2....")
tj_coin.add_new_block(block("2","20","20/4/2018","0"))
print("Mining block 3....")
tj_coin.add_new_block(block("3","100","20/4/2018","0"))
print("....."*15)
tj_coin.print_blockchain()
print("....."*15)
print(tj_coin.is_a_validchain())
tj_coin.blockchain[2].data = 200
tj_coin.print_blockchain()
print("....."*15)
print(tj_coin.is_a_validchain())
print("....."*15)
    
    