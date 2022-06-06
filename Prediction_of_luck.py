import time
import datetime
'''
十二地支={子 、 丑 、 寅 、 卯 、 辰 、 巳 、 午 、 未 、 申 、 酉 、 戌 、 亥 }
         1     2    3    4    5    6     7    8    9    10    11   12
一天有24个小时，从上一日23时开始为子，以此类推    23+2//2%12   22+2/2
算时间卦方法：
举例：2016年7月15日13：30分
     丙申年7月15日  未时
       9->7.15 -->8
1.上卦
＝年地支数+月+日相加，/8，找对应卦象[（9+7+15）／８＝３……7]
“7”　对应　艮卦　　
2.下卦
＝年地支数+月+日+时数，再除以8－＞[（9+7+15＋８）／８＝４……7]
“7”　对应　艮卦
3.变爻
（首先爻是从下向上排列的，最下面为初爻，最上面为六爻／上爻）
＝年地支数+月+日+时数，再除以6－＞[（9+7+15＋８）／6＝6……3]
于是在下文，我们就把从下向上数第三个杠由阳转阴，由阴转阳

4.输出结果，（分别代表开始，过程，和结束）
主卦：由上卦下卦组合得主卦。
互卦：由五、四、三爻作为互卦的上卦；二、三、四爻作为互卦的下卦。
变卦：将主卦变爻得到变卦。
'''


def CheckAllTime():#这个函数，可以查看所有时间格式的引用方式
    i = datetime.datetime.now()
    print ("当前的日期和时间是 %s" % i)
    print ("ISO格式的日期和时间是 %s" % i.isoformat() )
    print ("当前的年份是 %s" %i.year)
    print ("当前的月份是 %s" %i.month)
    print ("当前的日期是  %s" %i.day)
    print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
    print ("当前小时是 %s" %i.hour)
    print ("当前分钟是 %s" %i.minute)
    print ("当前秒是  %s" %i.second)

'''def Show(lists):
    print("展示列表：")
    for(listItem in lists):
        print("\t",listItem)'''

def TimeNow():#按照当前的 [年，月，日，时] 并构造列表
    i = datetime.datetime.now()
    year=i.year ; month=i.month
    day=i.day   ;  hour=i.hour
    TimeFormat=[year , month , day , hour]
    return TimeFormat

def SuanTimeGua(timelist):  #最终输出一个包含上卦，下卦，变爻的列表
    year= (timelist[0] - 3) %12 #年地支数
    month = timelist[1]
    day = timelist[2]
    if(timelist[3]==23):
        hour=1
    elif(timelist[3]!=23):
        hour= (timelist[3]+2)//2
    ShangGua_number = (year+month+day)%8
    XiaGua_number = (year+month+day+hour)%8
    BianYao_number = (year+month+day+hour)%6
    print("mumber(上卦，下卦，变爻):",ShangGua_number,XiaGua_number,BianYao_number)
    #BaGua = {1:"乾 111",2:"坤 000",3:"坎 101",4:"離 010",5:"震 110",6:"巽 001",7:"艮 011",0:"兌 100"}
    ShangGua = BaGua[ShangGua_number]
    XiaGua = BaGua[XiaGua_number]
    BianYao = BianYao_number
    return [ShangGua_number,XiaGua_number,BianYao_number],[ShangGua, XiaGua, BianYao]

def BianYao(GuaXiang):#卦象[]包括：上卦(文)，下卦(文)，和变爻(数)
    i=GuaXiang[0]#上卦(文)
    j=GuaXiang[1]#下卦(文)
    k=GuaXiang[2]#变爻(数)
    BenGua = GuaTu[i] + GuaTu[j]
    print("BenGua:",BenGua)
    print("BenGua[-k]:", BenGua[-k])
    BianGua = BenGua
    if(BenGua[-k] == '0'):
        print("阴变阳->：本卦:",BenGua)
        if (k == 1):#当k=1时，-k+1=0，出现bug,特此修正
            BianGua = BenGua[:-k] + '1'
        else :
            BianGua = BenGua[:-k] + '1' + BenGua[-k+1: ]
        print("\t\t 变卦:",BianGua)
    elif (BenGua[-k] == '1'):
        print("阳变阴->：本卦:",BenGua)
        if(k==1):#当k=1时，-k+1=0，出现bug，特此修正
            BianGua = BenGua[:-k] + '0'
        else:
            BianGua = BenGua[:-k] + '0' + BenGua[-k+1: ]
        print(BianGua[-k])
        print("\t\t 变卦:",BianGua)
    return [BenGua,BianGua,k]


#以下为代码正文区------------------------------------------------------------------------------------
'''
1.第一步是获取当前时间，斌且根据当前时间输出上卦下卦，直接拼凑可以得到主卦
2.第二步是得到变卦，变卦涉及到运算，我的建议是建立一个独立字典，字典一 = {0-7：八卦名}，字典一 = {八卦名：图形的二进制表示}
3.将上卦图像+下卦图像=六位数数字（str），变爻是从后往前的方法，刚好10**爻数，或者str[-爻数]索引
4.构建全列表解卦：64卦可以化作一个二维表格，先构建一个111111型的数组，在创建一个卦名称型的数组。
/*今日工作结束，下一步：改正字典的顺序；；并且建立一个大字典，可以通过大字典将二维卦象变成字面意思的卦象*/
最后预想的成品结果：
1.你现在的日期是：/（输入的日期格式）
2.上卦，下卦，变爻是->。可以有文字呈现，但程序识别的是数字
3.变爻后结果->（将变爻标出）
4.最终得到的卦象是：卦象名称和图形->
'''
QuanBaGua = {1:"乾 111",2:"兌 100",3:"離 010",4:"震 110",5:"巽 001",6:"坎 101",7:"艮 011",0:"坤 000"}
BaGua = {1:"乾",2:"兌",3:"離",4:"震",5:"巽",6:"坎",7:"艮",8:"坤"}
#乾一；兑二；离三；震四；巽五；坎六；艮七；坤八
GuaTu = {"乾":'111',"兌":'100',"離":'010',"震":'110',"巽":'001',"坎":'101',"艮":'011',"坤":'000'}
SixtyFourGua_num = {'111111': ["乾卦", "上乾下乾"],  '111100': ["夬卦", "上乾下兑"],  '111010': ["大有卦", "上乾下離"], '111110': ["大壮卦", "上乾下震"],  '111001': ["小畜卦", "上乾下巽"], '111101': ["需卦", "上乾下坎"],  '111011': ["大畜卦", "上乾下艮"], '111000': ["泰卦", "上乾下坤"],
                    '100111': ["履卦", "上兑下乾"],  '100100': ["兑卦", "上兑下兑"],  '100010': ["睽卦", "上兑下離"],   '100110': ["归妹卦", "上兑下震"], '100001': ["中孚卦", "上兑下巽"], '100101': ["节卦", "上兑下坎"],  '100011': ["损卦", "上兑下艮"], '100000': ["临卦", "上兑下坤"],
                    '010111': ["同人卦", "上離下乾"], '010100': ["革卦", "上離下兑"],  '010010': ["离卦", "上離下離"],   '010110': ["丰卦", "上離下震"],  '010001': ["家人卦", "上離下巽"], '010101': ["既济卦", "上離下坎"], '010011': ["贲卦", "上離下艮"], '010000': ["明夷卦", "上離下坤"],
                    '110111': ["无妄卦", "上震下乾"], '110100': ["随卦", "上震下兑"],  '110010': ["噬嗑卦", "上震下離"], '110110': ["震卦", "上震下震"],  '110001': ["益卦", "上震下巽"],   '110101': ["屯卦", "上震下坎"],  '110011': ["颐卦", "上震下艮"], '110000': ["复卦", "上震下坤"],
                    '001111': ["姤卦", "上巽下乾"],  '001100': ["大过卦", "上巽下兑"], '001010': ["鼎卦", "上巽下離"],   '001110': ["恒卦", "上巽下震"],  '001001': ["巽卦", "上巽下巽"],   '001101': ["井卦", "上巽下坎"],  '001011': ["蛊卦", "上巽下艮"], '001000': ["升卦", "上巽下坤"],
                    '101111': ["讼卦", "上坎下乾"],  '101100': ["困卦", "上坎下兑"],  '101010': ["未济卦", "上坎下離"], '101110': ["解卦", "上坎下震"],   '101001': ["涣卦", "上坎下巽"],   '101101': ["坎卦", "上坎下坎"],  '101011': ["蒙卦", "上坎下艮"], '101000': ["师卦", "上坎下坤"],
                    '011111': ["遁卦", "上艮下乾"],  '011100': ["咸卦", "上艮下兑"],  '011010': ["旅卦", "上艮下離"],   '011110': ["小过卦", "上艮下震"], '011001': ["渐卦", "上艮下巽"],   '011101': ["蹇卦", "上艮下坎"],  '011011': ["艮卦", "上艮下艮"], '011000': ["谦卦", "上艮下坤"],
                    '000111': ["否卦", "上坤下乾"],  '000100': ["萃卦", "上坤下兑"],  '000010': ["晋卦", "上坤下離"],   '000110': ["豫卦", "上坤下震"],   '000001': ["观卦", "上坤下巽"],   '000101': ["比卦", "上坤下坎"],  '000011': ["剥卦", "上坤下艮"], '000000': ["坤卦", "上坤下坤"],
                    }
href_dic={'乾卦':"https://m.zhouyi.cc/zhouyi/yijing64/4103.html" , '夬卦':"https://m.zhouyi.cc/zhouyi/yijing64/4183.html" , '大有卦':"https://m.zhouyi.cc/zhouyi/yijing64/4141" , '大壮卦':"https://m.zhouyi.cc/zhouyi/yijing64/4173.html" , '小畜卦':"https://m.zhouyi.cc/zhouyi/yijing64/4112.html" , '需卦':"https://m.zhouyi.cc/zhouyi/yijing64/4108.html" , '大畜卦':"https://m.zhouyi.cc/zhouyi/yijing64/4159.html" , '泰卦':"https://m.zhouyi.cc/zhouyi/yijing64/4126.html" ,
          '履卦':"https://m.zhouyi.cc/zhouyi/yijing64/4113.html" , '兑卦':"https://m.zhouyi.cc/zhouyi/yijing64/4200.html" , '睽卦':"https://m.zhouyi.cc/zhouyi/yijing64/4177.html" , '归妹卦':"https://m.zhouyi.cc/zhouyi/yijing64/4195.html" , '中孚卦':"https://m.zhouyi.cc/zhouyi/yijing64/4255.html" , '节卦':"https://m.zhouyi.cc/zhouyi/yijing64/4244.html" , '损卦':"https://m.zhouyi.cc/zhouyi/yijing64/4181.html" , '临卦':"https://m.zhouyi.cc/zhouyi/yijing64/4146.html" ,
          '同人卦':"https://m.zhouyi.cc/zhouyi/yijing64/4140.html" , '革卦':"https://m.zhouyi.cc/zhouyi/yijing64/4189.html" , '离卦':"https://m.zhouyi.cc/zhouyi/yijing64/4169.html" , '丰卦':"https://m.zhouyi.cc/zhouyi/yijing64/4196.html" , '家人卦':"https://m.zhouyi.cc/zhouyi/yijing64/4176.html" , '既济卦':"https://m.zhouyi.cc/zhouyi/yijing64/4257.html" , '贲卦':"https://m.zhouyi.cc/zhouyi/yijing64/4149.html" , '明夷卦':"https://m.zhouyi.cc/zhouyi/yijing64/4175.html" ,
          '无妄卦':"https://m.zhouyi.cc/zhouyi/yijing64/4153.html" , '随卦':"https://m.zhouyi.cc/zhouyi/yijing64/4144.html" , '噬嗑卦':"https://m.zhouyi.cc/zhouyi/yijing64/4148.html" , '震卦':"https://m.zhouyi.cc/zhouyi/yijing64/4192.html" , '益卦':"https://m.zhouyi.cc/zhouyi/yijing64/4182.html" , '屯卦':"https://m.zhouyi.cc/zhouyi/yijing64/4106.html" , '颐卦':"https://m.zhouyi.cc/zhouyi/yijing64/4164.html" , '复卦':"https://m.zhouyi.cc/zhouyi/yijing64/4152.html" ,
          '姤卦':"https://m.zhouyi.cc/zhouyi/yijing64/4184.html" , '大过卦':"https://m.zhouyi.cc/zhouyi/yijing64/4167.html" , '鼎卦':"https://m.zhouyi.cc/zhouyi/yijing64/4190.html" , '恒卦':"https://m.zhouyi.cc/zhouyi/yijing64/4171.html" , '巽卦':"https://m.zhouyi.cc/zhouyi/yijing64/4198.html" , '井卦':"https://m.zhouyi.cc/zhouyi/yijing64/4188.html" , '蛊卦':"https://m.zhouyi.cc/zhouyi/yijing64/4145.html" , '升卦':"https://m.zhouyi.cc/zhouyi/yijing64/4186.html" ,
          '讼卦':"https://m.zhouyi.cc/zhouyi/yijing64/4109.html" , '困卦':"https://m.zhouyi.cc/zhouyi/yijing64/4187.html" , '未济卦':"https://m.zhouyi.cc/zhouyi/yijing64/4163.html" , '解卦':"https://m.zhouyi.cc/zhouyi/yijing64/4180.html" , '涣卦':"https://m.zhouyi.cc/zhouyi/yijing64/4212.html" , '坎卦':"https://m.zhouyi.cc/zhouyi/yijing64/4107.html" , '蒙卦':"https://m.zhouyi.cc/zhouyi/yijing64/4107.html" , '师卦':"https://m.zhouyi.cc/zhouyi/yijing64/4110.html" ,
          '遁卦':"https://m.zhouyi.cc/zhouyi/yijing64/4172.html" , '咸卦':"https://m.zhouyi.cc/zhouyi/yijing64/4170.html" , '旅卦':"https://m.zhouyi.cc/zhouyi/yijing64/4197.html" , '小过卦':"https://m.zhouyi.cc/zhouyi/yijing64/4256.html" , '渐卦':"https://m.zhouyi.cc/zhouyi/yijing64/4196.html" , '蹇卦':"https://m.zhouyi.cc/zhouyi/yijing64/4179.html" , '艮卦':"https://m.zhouyi.cc/zhouyi/yijing64/4193.html" , '谦卦':"https://m.zhouyi.cc/zhouyi/yijing64/4142.html" ,
          '否卦':"https://m.zhouyi.cc/zhouyi/yijing64/4127.html" , '萃卦':"https://m.zhouyi.cc/zhouyi/yijing64/4185.html" , '晋卦':"https://m.zhouyi.cc/zhouyi/yijing64/4174.html" , '豫卦':"https://m.zhouyi.cc/zhouyi/yijing64/4143.html" , '观卦':"https://m.zhouyi.cc/zhouyi/yijing64/4147.html" , '比卦':"https://m.zhouyi.cc/zhouyi/yijing64/4111.html" , '剥卦':"https://m.zhouyi.cc/zhouyi/yijing64/4150.html" , '坤卦':"https://m.zhouyi.cc/zhouyi/yijing64/4105.html"
          }

timelist = TimeNow()
print("当前时间 :",timelist)
GuaMumber , GuaXiang = SuanTimeGua(timelist)
print("上卦，下卦，变爻 :",GuaXiang)
result = BianYao(GuaXiang)
print(result)
BenGua=SixtyFourGua_num[result[0]]
print(BenGua)
BenGua_href=href_dic[BenGua[0]]
BianGua=SixtyFourGua_num[result[1]]
BianGua_href=href_dic[BianGua[0]]
YaoBian=result[2]
print("本卦：",BenGua,"\n链接查看本卦：",BenGua_href)
print("变卦：",BianGua,"\n链接查看变卦：",BianGua_href)
print("变爻数（从下往上，最下级为1，最上级为0）：",result[2])

