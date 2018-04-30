# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 01:02:08 2018

@author: ABIOYE OYETUNJI
"""

import hash
import datetime


class blockchain():
    # the constructor method here declares a list which only contains the genesis block
    def __init__(self):
        print("The genesis block hash is ")
        self.blockchain = [self.genesis_block()]
        
        
    # this method defines the genesis block which is the first block in the blockchain
    # with previous hash "0"  
    def genesis_block(self):
        date = datetime.datetime.now()
        genesis_block_content = {
                                "block_num": 0,
                                "data":"the genesis block",
                                "timestamp" : date,
                                "previous_hash" : 0
                                }
       
        genesis_hash =  hash.hash.hasher(genesis_block_content)
        print(genesis_hash)
            
        
        genesisBlock = {"hash" : genesis_hash, "content" : genesis_block_content}
        
        
        return genesisBlock



    # this method creates a new block which contains content that includes the hash of 
    # the previous block thats how they are linked
    def add_new_block(self): 
        previous_block = self.blockchain[len(self.blockchain) - 1 ]
        previous_hash = previous_block["hash"]
        date = datetime.datetime.now()
        block_num = previous_block["content"]["block_num"] + 1 

        new_block_content = {   "block_num": block_num,
                                "data":"this a new block",
                                "timestamp" : date,
                                "previous_hash" : previous_hash
                                }
        new_block_hash = hash.hash.mine_a_block(3,new_block_content)
        new_block = {"hash" : new_block_hash, "content" : new_block_content}
        self.blockchain.append(new_block)
        print("This is the",block_num,"block" )
        print(self.blockchain[-1])
        
        
        
        
    
    

# this prints out the blockchain for test purposes
chain = blockchain()
print("..." * 24 )
chain.add_new_block()
print("..." * 24 )
chain.add_new_block()
print("..." * 24 )
chain.add_new_block()