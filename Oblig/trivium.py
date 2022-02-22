#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 18:27:03 2022

@author: edyta
"""

from BitVector import *


iv = BitVector(bitlist = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
key =BitVector(bitlist = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,
      1,0,1,0,1,0,1,0,1,0,1,0])



def setup(key, iv):

    initialState = BitVector(size=288) # initialize vector to insert iv and key
    initialState[0:80] = key
    initialState[93:173] = iv #IV stands for initialization vector
    initialState[-3:] = BitVector(bitlist = [1,1,1])
    return initialState
   
def warmUp(key, iv):
    initialState = setup(key, iv)
    for i in range(1152 * 288): #warmup rounds
        states = generation(initialState)
    return states



def generation(state):
    t1 = state[65] ^ state[92] ^ (state[90] & state[91]) ^ state[170]
    t2 = state[161] ^ state[176] ^ (state[174] & state[175]) ^ state[263]
    t3 = state[242] ^ state[287] ^ (state[285] & state[286]) ^ state[68]
    state.shift_right_by_one()
    state[0] = t3
    state[93] = t1
    state[177] = t2   
    return state


def trivium(key, iv, bits):
    streamBits = BitVector(size=bits)
    state = warmUp(key, iv)
    for i in range(bits): 
        streamBits[i] = (state[65] ^ state[92]) ^ (state[161] ^ state[176]) ^ (state[242] ^ state[287])
        state = st(state)
 
    return streamBits
        







