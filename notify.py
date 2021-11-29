import requests,json

with open('token.json', encoding='utf-8')as f :
    token = json.load(f)
    
class Notify:
    def __init__(self, token):
        self.token = token 
        self.headers = { "Authorization": "Bearer " + self.token}
    def sendmsg(self, msg):
        headers = self.headers 
        payload = {'message': msg}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code
    def localimg(self, msg , pic):
        headers = self.headers
        payload = {
            'message': msg
        }
        files = {'imageFile': open(pic, 'rb')}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload, files = files)
        return r.status_code
    def netimg(self, msg , picurl):
        headers = self.headers
        payload = {'message': msg , 'imageThumbnail': picurl,'imageFullsize': picurl}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code
    def sticker(self,msg,packageid, stickerID):
        headers = self.headers
        payload = {'message': msg ,'stickerPackageId':packageid ,'stickerId': stickerID}
        r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code 

myNotify = Notify(token = token["token"])
myNotify.sendmsg(msg = "文字測試")
res = myNotify.localimg(msg = "我是熊大" , pic = 'image/brown.png')
myNotify.netimg(msg = "小熊維尼" , picurl = "https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2017-07/fa2c3d72-7fad-4ccf-9857-e90af952b956_m.jpg")
myNotify.sticker(msg ="貼圖測試" , packageid = 446 ,stickerID = 1988)
