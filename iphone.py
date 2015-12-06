#coding=utf-8

def compute(month=24, total=6792):
    mon = 0
    tot_income = 0
    per = total/month
    for x in xrange(0,month):
        mon +=1
        current =  total - per*mon
        income = current*0.12/365.0*30
        tot_income += income
        if mon == 1:
            print u'月份',u'当月还款', u'剩余总额', u'当月收益', u'总收益'
        print(mon, per, current, income, tot_income)
        
compute()
    