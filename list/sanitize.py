def st(data):
    if '-' in data:
        seq = '-'
    elif ':' in data:
        seq = ':'
    else:
        return data
    
    (mins, secs) = data.split(seq)
    return mins + '.' + secs;