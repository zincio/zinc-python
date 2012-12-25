import requests,json
import sys,argparse
import time,datetime
import logging
import pprint

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class ZincAPIError(Exception):
    def __init__(self,code,message,http_code=None):
        self.code = code
        self.message = message
        self.http_code = http_code
    def __unicode__(self):
        return u'{0}: {1}'.format(self.code,self.message)
    def __str__(self):
        return unicode(self).encode('utf-8')
    def __repr__(self):
        return 'ZincAPIError(code={0.code:r},message={0.message:r},http_code={0.http_code:r})'

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

        try:
            if r['_type'] == 'error':
                raise ZincAPIError(code=r['code'],message=r['message'],http_code=r['_http_code'])
        except TypeError: pass # Probably a list

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
        return ZincOrder(client=self)._create(order_obj)

    def get_order(self,order_id):
        return ZincOrder(order_id,client=self).update()

    def get_all_orders(self):
        js = self._get('orders')
        return [ZincOrder(o,client=self) for o in js]

    def get_user(self):
        ''' Return the user object. '''
        return ZincUser(client=self).update()

class _ZincWrappedObject(object):
    def __init__(self,first=None,client=None):
        if isinstance(first,dict):
            self._obj = first
            self.id = first['id']
        elif isinstance(first,basestring):
            self.id = first
            self._obj = None
        if not client: raise Exception("specify a client")
        self.client = client
    def update(self):
        self._obj = self.client._get(self.ADDRESS.format(self))
        return self
    def dict(self):
        return self._obj
    def __getitem__(self,key):
        return self._obj[key]
    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__,json.dumps(self.dict(),indent=4,sort_keys=True))

class ZincOrder(_ZincWrappedObject):
    ADDRESS = 'orders/{0.id}'
    def _create(self,obj):
        self._obj = self.client._post('orders',order_obj)
        self.id = self._obj['id']
        return self
    def cancel(self):
        return ZincCancellation(client=self.client)._create(self.id)
    def get_cancellation(self):
        return ZincCancellation(self.id,client=self.client).update()

class ZincCancellation(_ZincWrappedObject):
    ADDRESS = 'orders/{0.id}/cancellation'
    def _create(self,id):
        self._obj = self.client._post('orders/{0}/cancellation'.format(id))
        self._id = id
        return self
    def get_order(self):
        return ZincOrder(self.id,client=self.client).update()

class ZincUser(_ZincWrappedObject):
    ADDRESS = 'user'

