# A function that calculates a if a hero will have enough bullets to kill two dragons protecting

def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False 