# -*-coding:utf-8-*-
'''''
根据包名从豌豆荚批量下载样本。文件存放于E盘test目录下。
http://www.wandoujia.com/apps/com.cleanmaster.mguard_cn/binding?source=web_inner_referral_binded
'''
import urllib2
import time
import os


def Main():
    f1 = open('package.txt', 'r')  # 打开当前目录下存放包名（每行一个包名）的txt
    packageName = f1.readline().strip()
    while packageName != '':
        print packageName + ' is downloading~'
        downloadUrl = 'http://www.wandoujia.com/apps/%s/download' % packageName
        try:
            if not os.path.exists('apk/%s.apk' % packageName):
                result = urllib2.urlopen(downloadUrl)
                data = result.read()
                with open('apk/%s.apk' % packageName, 'wb') as f:
                    f.write(data)
                    print packageName + ' download over~'
        except Exception, e:
            print packageName + ' has no this package!' + str(e)
        packageName = f1.readline().strip()
        time.sleep(1)
    f1.close()


if __name__ == '__main__':
    Main()