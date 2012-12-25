import requests,json
import sys,argparse
import time,datetime
import logging
import pprint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class ZincClient(object):
    def __init__(self,api_key,version=1,base='api.zinc.io',verify_https=True):
        self.api_key = api_key
        self.base = base
        self.version = version
        self.verify_https = verify_https
        
        if not self.verify_https:
            logger.warning('*** WARNING ***')
            logger.warning('HTTPS verification is disabled. This is probably NOT what you want. Do not continue unless you understand the implications.')
            logger.warning('*** WARNING ***')

    def _req(self,method,url,data=None):
        ''' Make a HTTP request to the specified `url`.
                `method` can be 'get' or 'post'.
                `data` will be converted to JSON before posting if given.
            '''
        kwargs = {'verify': self.verify_https, 'auth':(self.api_key,'')}
        if data:
            kwargs['data'] = json.dumps(data)
            kwargs['headers'] = {'content-type':'application/json'}

        fullurl = 'https://{0.base}/v{0.version}/{1}'.format(self,url.lstrip('/'))
        logger.info('Request: {0} to {1}'.format(method.upper(),fullurl))
        if data: logger.debug('Request data: %s',self._pjs(data))

        r = getattr(requests,method)(fullurl,**kwargs).json
        if isinstance(r,type(lambda:0)): r = r() # new requests uses r.json()

        try:
            logger.debug('Response data: %s',self._pjs(r))
        except: pass

        return r

    def _get(self,url):
        ''' See self._req for docs. '''
        return self._req(method='get',url=url)
    def _post(self,url,data=None):
        ''' See self._req for docs. '''
        return self._req(method='post',url=url,data=data)
    def _pjs(self,js):
        return json.dumps(js,sort_keys=True,indent=4)

    def create_order(self,order_obj):
        ''' Create a new order from order_obj. If wait, keep getting the order until it is finished. '''
        js = self._post('orders',order_obj)
        return ZincOrder(js,client=self)

    def get_order(self,order_id):
        o = ZincOrder(order_id,client=self)
        o.update()
        return o

    def get_all_orders(self):
        js = self._get('orders')
        return [ZincOrder(o,client=self) for o in js]

    def get_user(self):
        ''' Return the user object. '''
        return self._get('user')

class ZincOrder(object):
    def __init__(self,first,client):
        if isinstance(first,dict):
            self._obj = first
            self.id = first['id']
        elif isinstance(first,basestring):
            self.id = first
            self._obj = None
        self.client = client

    def update(self):
        self._obj = self.client._get('orders/{0.id}'.format(self))

    def dict(self):
        return self._obj

    def __getitem__(self,key):
        return self._obj[key]

    def cancel(self):
        return self.client._post('orders/{0.id}/cancellation'.format(self))
    
    def get_cancellation(self):
        return self.client._get('orders/{0.id}/cancellation'.format(self))

    def __repr__(self):
        return 'ZincOrder({0})'.format(pprint.pformat(self.dict()))

