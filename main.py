from requests_toolbelt import MultipartEncoder
import random
import requests

def rH(n):
	return ''.join([random.choice('0123456789ABCDEF') for x in range(n)])

def rI():
	return '%s-%s-%s-%s-%s'%(rH(8),rH(4),rH(4),rH(4),rH(12))

def dL(u,p):
	m=MultipartEncoder(fields = {'password':(None,p),
                       'username':(None,u),
                       'phone':(None,''),
                       'app_id':(None,rI()),
                       'grant_type':(None,'password')})
	r=requests.post('https://api.vsco.co/2.0/oauth/passwordgrant',data=m,headers={'Authorization':'Basic dnV6ZWRhemViZWp1Z2UzeWh1Z3k5ZXFlbWE1YTV1cmU5dTJ1c2FyYTpyeWplNXlydXBlemUyZXN5YmVyeQ==','Accept-Encoding':'gzip, deflate','x-client-platform':'ios','Accept-Language':'en-GB, de-DE, da-DK, en-US, ru-RU','x-client-build':'3486','X-CLIENT-LOCALE':'en','User-Agent':'VSCO/3486 CFNetwork/808.2.16 Darwin/16.3.0','Content-Type':m.content_type},verify=False)
	return r.content
	
if __name__ == "__main__":
	print dL('test','test')