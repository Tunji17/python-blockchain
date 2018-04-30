# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 23:08:01 2018

@author: ABIOYE OYETUNJI
"""
import hashlib
import pickle


class hash:
    

    # this method is used to hash the genesis block using sha256  but first encode 
    # the message which is a dictionary using a dumps from pickle 
    def hasher(message=""):            
        en_message = pickle.dumps(message)

        hashedmsg = hashlib.sha256(en_message).hexdigest()
                            
        return hashedmsg
     
        
    # this is used to hash the newly mined block and check it's proof of work or difficulty 
    # it sets a maximum nonce value so the system has a limit 
    def mine_a_block(difficulty,message=""):
        maxinonce = 2**32 
        
        for nonce in range(maxinonce):
            encode_result =pickle.dumps(str(message)+str(nonce))
            mined_result = hashlib.sha256(encode_result).hexdigest()

        # check if result is valid
            if mined_result[:difficulty] == "0" * difficulty:
                print("success")
                print("This is the nonce: ",nonce,"This is the mined hash: " , mined_result)
                return (mined_result)

        print("failed after ",maxinonce," tries")
        return nonce
        
            
       
        

# used for debugging purposes
        
#mydict = {
#         "james": "man",
#         "mary": "woman",
#         "goat": "animal",
#         "cat" : "animal"
#        }
#
#my_hash= hash()
#my_hash.hasher(mydict)
#



#my_hash.hasher()
#my_hash.mine_a_block(3)
#my_hash.mine_a_block(3)        
        
        
    