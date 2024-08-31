import numpy as np
import secretflow as sf

def data_psi(parties:list, spu:sf.SPU):
    if len(parties) > 2:
        raise ValueError("Only two parties are supported")
    members = []
    for party in parties:
        members.append(sf.PYU(party))
    
