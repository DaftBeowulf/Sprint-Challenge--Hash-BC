import hashlib
import requests

import sys
import json

from uuid import uuid4

from timeit import default_timer as timer

import random


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last six digits of hash(p) are equal
    to the first six digits of hash(p')
    - IE:  last_hash: ...AE9123456, new hash 123456888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = None
    proof0 = 10000000
    proof1 = 20000000
    proof2 = 30000000
    proof3 = 40000000
    proof4 = 50000000
    proof5 = 60000000
    proof6 = 70000000
    proof7 = 80000000
    proof8 = 90000000
    proof9 = 90000001
    #  TODO: Your code here
    while proof == None:
        if valid_proof(last_proof, proof0):
            print('\nproof0 found it!\n')
            proof = proof0
        elif valid_proof(last_proof, proof1):
            print('\nproof1 found it!\n')
            proof = proof1
        elif valid_proof(last_proof, proof2):
            print('\nproof2 found it!\n')
            proof = proof2
        elif valid_proof(last_proof, proof3):
            print('\nproof3 found it!\n')
            proof = proof3
        elif valid_proof(last_proof, proof4):
            print('\nproof4 found it!\n')
            proof = proof4
        elif valid_proof(last_proof, proof5):
            print('\nproof5 found it!\n')
            proof = proof5
        elif valid_proof(last_proof, proof6):
            print('\nproof6 found it!\n')
            proof = proof6
        elif valid_proof(last_proof, proof7):
            print('\nproof7 found it!\n')
            proof = proof7
        elif valid_proof(last_proof, proof8):
            print('\nproof8 found it!\n')
            proof = proof8
        elif valid_proof(last_proof, proof9):
            print('\nproof9 found it!\n')
            proof = proof9
        else:
            proof0 -= 1
            proof1 -= 1
            proof2 -= 1
            proof3 -= 1
            proof4 -= 1
            proof5 -= 1
            proof6 -= 1
            proof7 -= 1
            proof8 -= 1
            proof9 += 1

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Multi-ouroborus:  Do the last six characters of
    the hash of the last proof match the first six characters of the hash
    of the new proof?

    IE:  last_hash: ...AE9123456, new hash 123456E88...
    """

    # TODO: Your code here!
    last_hash = hashlib.sha256(f'{last_proof}'.encode()).hexdigest()
    curr_hash= hashlib.sha256(f'{proof}'.encode()).hexdigest()
    return curr_hash[:6] == last_hash[-6:]


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == 'NONAME\n':
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        print(r)
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))

        post_data = {"proof": new_proof,
                     "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))
