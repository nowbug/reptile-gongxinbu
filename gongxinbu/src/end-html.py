# /usr/bin
# encoding:utf-8
import urllib2
import re
import pandas as pd


def urlget(url):
    url = url

    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    content = response.read().decode('gbk').encode('utf-8')
    # print content
    return content


def guize(content):
    tes1 = ['<th width="250">外廓尺寸长（mm）：</th>(.*?)</tr>', '<th width="250">外廓尺寸宽（mm）：</th>(.*?)</tr>',
            '<th width="250">外廓尺寸高（mm）：</th>(.*?)</tr>', '<th width="250">总质量（kg）：</th>(.*?)</tr>',
            '<th width="250">整备质量（kg）：</th>(.*?)</tr>', '<th width="250">最高车速（km/h）：</th>(.*?)</tr>',
            '<th width="250">续驶里程（km，工况法）：</th>(.*?)</tr>', '<th width="250">续驶里程（km，等速法）：</th>(.*?)</tr>',
            '<th width="250">Ekg单位载质量能量消耗量（Wh/km·kg）：</th>(.*?)</tr>',
            '<th width="250">电池系统能量密度（Wh/kg）：</th>(.*?)</tr>',
            '<th width="250">储能装置种类：</th>(.*?)</tr>', '<th width="250">驱动电机类型：</th>(.*?)</tr>',
            '<th width="250">驱动电机峰值功率/转速/转矩（kW /r/min/N.m）：</th>(.*?)</tr>',
            '<th width="250">储能装置总储电量（kWh）：</th>(.*?)</tr>',
            '<th width="250">工况条件下百公里耗电量（Y）（kWh/100km）：</th>(.*?)</tr>', '<th width="250">燃料种类：</th>(.*?)</tr>',
            '<th width="250">是否允许外接充电：</th>(.*?)</tr>', '<th width="250">纯电动模式下续驶里程（km，等速法）：</th>(.*?)</tr>',
            '<th width="250">纯电动模式下续驶里程（km，工况法）：</th>(.*?)</tr>', '<th width="250">发动机生产企业：</th>(.*?)</tr>',
            '<th width="250">排量/功率（ml/kW）：</th>(.*?)</tr>', '<th width="250">发动机型号：</th>(.*?)</tr>',
            '<th width="250">节油率水平（%）：</th>(.*?)</tr>', '<th width="250">燃料消耗量（L/100km，B状态）：</th>(.*?)</tr>',
            '<th width="250">燃料消耗量（L/100km，电量平衡运行阶段）：</th>(.*?)</tr>', '<th width="250">30分钟最高车速（km/h）：</th>(.*?)</tr>',
            '<th width="250">电池系统总质量占整车整备质量比例（%）：</th>(.*?)</tr>']
    # tes1 = ['<TH width=250>外廓尺寸长（mm）：</TH>(.*?)</TR>', '<TH width=250>外廓尺寸宽（mm）：</TH>(.*?)</TR>',
    #         '<TH width=250>外廓尺寸高（mm）：</TH>(.*?)</TR>', '<TH width=250>总质量（kg）：</TH>(.*?)</TR>',
    #         '<TH width=250>整备质量（kg）：</TH>(.*?)</TR>', '<TH width=250>最高车速（km/h）：</TH>(.*?)</TR>',
    #         '<TH width=250>续驶里程（km，工况法）：</TH>(.*?)</TR>', '<TH width=250>续驶里程（km，等速法）：</TH>(.*?)</TR>',
    #         '<TH width=250>Ekg单位载质量能量消耗量（Wh/km·kg）：</TH>(.*?)</TR>', '<TH width=250>电池系统能量密度（Wh/kg）：</TH>(.*?)</TR>',
    #         '<TH width=250>储能装置种类：</TH>(.*?)</TR>', '<TH width=250>驱动电机类型：</TH>(.*?)</TR>',
    #         '<TH width=250>驱动电机峰值功率/转速/转矩（kW /r/min/N.m）：</TH>(.*?)</TR>', '<TH width=250>储能装置总储电量（kWh）：</TH>(.*?)</TR>',
    #         '<TH width=250>工况条件下百公里耗电量（Y）（kWh/100km）：</TH>(.*?)</TR>', '<TH width=250>燃料种类：</TH>(.*?)</TR>',
    #         '<TH width=250>是否允许外接充电：</TH>(.*?)</TR>', '<TH width=250>纯电动模式下续驶里程（km，等速法）：</TH>(.*?)</TR>',
    #         '<TH width=250>纯电动模式下续驶里程（km，工况法）：</TH>(.*?)</TR>', '<TH width=250>发动机生产企业：</TH>(.*?)</TR>',
    #         '<TH width=250>排量/功率（ml/kW）：</TH>(.*?)</TR>', '<TH width=250>发动机型号：</TH>(.*?)</TR>',
    #         '<TH width=250>节油率水平（%）：</TH>(.*?)</TR>', '<TH width=250>燃料消耗量（L/100km，B状态）：</TH>(.*?)</TR>',
    #         '<TH width=250>燃料消耗量（L/100km，电量平衡运行阶段）：</TH>(.*?)</TR>', '<TH width=250>30分钟最高车速（km/h）：</TH>(.*?)</TR>',
    #         '<TH width=250>电池系统总质量占整车整备质量比例（%）：</TH>(.*?)</TR>']
    oneZz = '<td>(.*?)</td>'
    for q in content:
        chengming = 'style="font-size: 20px;"><strong>(.*?)</strong>'
        zheng1 = '配置ID：&nbsp;(.*?)</strong>'
        chexing = re.findall(zheng1, q, re.S)
        chengming = re.findall(chengming, q, re.S)
        print chengming

        z = 0
        while z < len(chexing):
            temp = []
            if chengming == []:
                chengming = 'NAN'
                temp.append(chengming)
            else:
                temp.append(chengming[0].strip().replace('&nbsp;', ''))

            temp.append(chexing[z].strip())

            for i in tes1:
                if re.findall(i, q, re.S) == []:
                    temp.append('NAN')
                else:
                    # print '1111'
                    # print re.findall(oneZz, str(re.findall(i, q, re.S)[0]), re.S)
                    temp.append(re.findall(oneZz, str(re.findall(i, q, re.S)[0]), re.S)[z].strip())
            x = '+'.join(temp)
            f.write(x)
            f.write('\n')
            z += 1
    return 'ok'


def fenge(request):
    print request
    content_bufen = request.split('/tbody></table>')

    tboby = 0
    listtboby = []
    while tboby < len(content_bufen):
        chexing = re.findall('配置ID：&nbsp;(.*?)</strong>', content_bufen[tboby], re.S)
        if chexing != []:
            listtboby.append(content_bufen[tboby])
        tboby += 1
    print len(listtboby)
    return listtboby


f = open('12.txt', 'w')
content = urlget(url='http://123.127.164.29:18082/CVT/Jsp/zjgl/nerds/201712.html')
content_bufen = fenge(content)
daixieru = guize(content_bufen)
print daixieru
f.close()
# print xieru(daixieru)
