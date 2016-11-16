#coding=utf-8

__author__ = 'zwq'

import json
from pyhessian.client import HessianProxy


class Callee:
    def __call__(self, *args):
        print('Called', args)

    def proxy(self):
        url="http://10.102.36.151:8080/hessian/orderService"
        try:
            proxy=HessianProxy(url)
#            addr='{"orderId":null,"orderSn":null,"parentOrderId":null,"parentOrderSn":null,"userId":88892059,"opencityId":0,"orderStatus":null,"consignee":null,"country":null,"province":null,"city":null,"district":null,"area":null,"areaNumber":null,"address":null,"zipCode":null,"telNumber":null,"mobile":null,"email":null,"ip":null,"bestDate":0,"isTogether":0,"bestTime":0,"shippingId":null,"sfairline":null,"invoiceId":null,"userRank":null,"favourableId":null,"payId":1,"shippingFee":0,"productAmount":null,"orderAmount":null,"discount":null,"balance":0,"couponId":null,"couponType":null,"couponMoney":0,"useIntegral":null,"integralMoney":null,"integral":null,"giftCard":null,"giftCardMoney":0,"addTime":null,"orderType":null,"projetDeliveryTime":null,"orderSource":null,"orderProducts":[{"productId":2386,"productName":null,"productSn":null,"productNum":1,"returnMoney":null,"productPrice":null,"subtotal":null,"sellPrice":null,"integral":null,"weight":null,"totalWeight":null,"giftWeight":null,"activityEntities":[],"isShow":null,"isMaster":null,"sfshipping":null,"sfairline":null,"productPic":null,"giftType":0,"stockType":null,"integralF":null,"difference":null,"productType":"0","couponId":null,"fatherId":null,"fatherNum":null,"isPresale":null,"parentId":null,"orderProductId":null,"dmDiscount":null,"giftBagBase":null,"businessModel":null,"isSell":null,"inPrice":null,"dmCode":"0","sfvMinSellNum":null,"sfvShippingTime":null,"isBook":null,"isHave":null,"merchantNumber":null,"dmDiscountActivity":null,"id":null,"orderId":null,"sellNum":null,"activeId":null,"addTime":null,"productStatus":null,"linkId":null,"couponAmout":null,"reduceAmout":null,"activityCombinations":null,"giftBag":null,"subProducts":[],"actId":null,"addId":null,"mpiecePrice":null,"couponMoney":null,"wareHouseId":null,"brandId":0,"categoryOne":0,"categoryTwo":0,"categoryThree":0,"wareHouseCode":null,"shippingTimeId":0,"shippingFee":0,"serviceFee":0,"cod":null}],"invoice":null,"dmMoney":0,"productNum":null,"totalProductNum":null,"device":12,"activityEntities":[],"totalWeight":null,"couponSn":"","isBalance":0,"isGiftCard":0,"chanDiZhiCaiPrice":0,"consigneeAddr":{"addrId":null,"userId":null,"country":null,"province":2,"city":52,"district":500,"area":3409,"address":"xcfbcxvnvbgncvxbncvbn","zipCode":null,"telNumber":"","mobile":"18512345678","email":"","receiverName":"qqq","storeCode":null},"greetCard":null,"consignorAddr":null,"senderFlag":0,"payTime":null,"senderAddrId":null,"greetCardId":null,"smsType":null,"payAmount":null,"dmCode":"","couponTypeId":null,"stopAct":[],"isList":1,"giverName":null,"giverProvince":null,"giverCity":null,"giverDistrict":null,"giverArea":null,"giverAddress":null,"giverMobile":null,"sendTime":0,"isShowTogether":null,"sfarea":null,"areaFlag":null,"moneyPaid":null,"channelName":null,"promtionChannels":2,"orderRemark":null,"vendorRemark":null,"outerId":null,"userName":null,"orderBelong":0,"temperatureType":0,"saleType":0,"orderCps":null,"storeCode":null,"orderBelongMark":null,"userMdId":null,"orderBelongMdId":null,"orderBelongHbId":null,"serviceFee":0,"orderSort":null,"pickupMode":null,"lastToHomeTime":null,"activityId":null,"groupId":null,"preSale":false,"freshOrder":false},"iscart":0}'
#            data=json.dumps(addr)
#            #print proxy.status_code
#            print proxy.createOrderByJson(data)
        except NotImplementedError:
            print 'url error'
        return proxy

p = Callee().proxy()
addr='{"orderId":null,"orderSn":null,"parentOrderId":null,"parentOrderSn":null,"userId":88892059,"opencityId":0,"orderStatus":null,"consignee":null,"country":null,"province":null,"city":null,"district":null,"area":null,"areaNumber":null,"address":null,"zipCode":null,"telNumber":null,"mobile":null,"email":null,"ip":null,"bestDate":0,"isTogether":0,"bestTime":0,"shippingId":null,"sfairline":null,"invoiceId":null,"userRank":null,"favourableId":null,"payId":1,"shippingFee":0,"productAmount":null,"orderAmount":null,"discount":null,"balance":0,"couponId":null,"couponType":null,"couponMoney":0,"useIntegral":null,"integralMoney":null,"integral":null,"giftCard":null,"giftCardMoney":0,"addTime":null,"orderType":null,"projetDeliveryTime":null,"orderSource":null,"orderProducts":[{"productId":2386,"productName":null,"productSn":null,"productNum":1,"returnMoney":null,"productPrice":null,"subtotal":null,"sellPrice":null,"integral":null,"weight":null,"totalWeight":null,"giftWeight":null,"activityEntities":[],"isShow":null,"isMaster":null,"sfshipping":null,"sfairline":null,"productPic":null,"giftType":0,"stockType":null,"integralF":null,"difference":null,"productType":"0","couponId":null,"fatherId":null,"fatherNum":null,"isPresale":null,"parentId":null,"orderProductId":null,"dmDiscount":null,"giftBagBase":null,"businessModel":null,"isSell":null,"inPrice":null,"dmCode":"0","sfvMinSellNum":null,"sfvShippingTime":null,"isBook":null,"isHave":null,"merchantNumber":null,"dmDiscountActivity":null,"id":null,"orderId":null,"sellNum":null,"activeId":null,"addTime":null,"productStatus":null,"linkId":null,"couponAmout":null,"reduceAmout":null,"activityCombinations":null,"giftBag":null,"subProducts":[],"actId":null,"addId":null,"mpiecePrice":null,"couponMoney":null,"wareHouseId":null,"brandId":0,"categoryOne":0,"categoryTwo":0,"categoryThree":0,"wareHouseCode":null,"shippingTimeId":0,"shippingFee":0,"serviceFee":0,"cod":null}],"invoice":null,"dmMoney":0,"productNum":null,"totalProductNum":null,"device":12,"activityEntities":[],"totalWeight":null,"couponSn":"","isBalance":0,"isGiftCard":0,"chanDiZhiCaiPrice":0,"consigneeAddr":{"addrId":null,"userId":null,"country":null,"province":2,"city":52,"district":500,"area":3409,"address":"xcfbcxvnvbgncvxbncvbn","zipCode":null,"telNumber":"","mobile":"18512345678","email":"","receiverName":"qqq","storeCode":null},"greetCard":null,"consignorAddr":null,"senderFlag":0,"payTime":null,"senderAddrId":null,"greetCardId":null,"smsType":null,"payAmount":null,"dmCode":"","couponTypeId":null,"stopAct":[],"isList":1,"giverName":null,"giverProvince":null,"giverCity":null,"giverDistrict":null,"giverArea":null,"giverAddress":null,"giverMobile":null,"sendTime":0,"isShowTogether":null,"sfarea":null,"areaFlag":null,"moneyPaid":null,"channelName":null,"promtionChannels":2,"orderRemark":null,"vendorRemark":null,"outerId":null,"userName":null,"orderBelong":0,"temperatureType":0,"saleType":0,"orderCps":null,"storeCode":null,"orderBelongMark":null,"userMdId":null,"orderBelongMdId":null,"orderBelongHbId":null,"serviceFee":0,"orderSort":null,"pickupMode":null,"lastToHomeTime":null,"activityId":null,"groupId":null,"preSale":false,"freshOrder":false},"iscart":0}'
data=json.dumps(addr)
print p(data)

#a=1
#if a=='createOrderByJson':
#    proxy.createOrderByJson(data)
#elif a=='createOrderByJsonaaa'
#    proxy.createOrderByJsonaaa

#def p():
#
# return proxy
#
#case:
#    p.createOrderByJsonaaa


#service = HessianProxy("http://hessian.caucho.com/test/test")
#print service.replyDate_1()

#字典传递类对象例子
#addr={"tel":u"电话","fax":"02788889999","code":"ccc","street":"ddd"}
#proxy.setAddress(addr)
#print proxy.getAddress().fax

#Binary对象传递字节数组，非可读，通过value获取
#user={"name":"walker","password":"ppp","address":[addr],"blob":protocol.Binary("中华人民共和国")}
#proxy.setUser(user)
#print proxy.getUser().blob.value

