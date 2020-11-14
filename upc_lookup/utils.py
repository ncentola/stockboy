import requests

def look_up_upc(upc):
    '''
    Lookup UPC from whatever API you want and return some data like {'upc': upc, 'data': data}
    TODO - replace this with something more permanent
    '''
    
    r = requests.get('https://api.upcitemdb.com/prod/trial/lookup?upc={}'.format(upc))

    # just get the first element for now
    # not sure why there would be more than item entry...
    data = r.json().get('items')[0]

    return {
        'upc'   : upc,
        'data'  : data
    }
