for i in range(1,101):
    #i%7==0表示能被7整除的就跳过打印；
    #i%10==7表示两位数取余数个位带7的跳过打印；
    #i//10==7表示十位带7的跳过打印。
	if(i%7==0 or i%10==7 or i//10==7):
		continue
	print(i)
