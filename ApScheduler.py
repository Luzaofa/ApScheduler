# Time    : 1/17/2019 6:49 PM
# Author  : Luzaofa

import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


class Demo(object):

    def __init__(self):
        pass

    def my_job1(self, args):
        print('-' * 10 + 'my_job1' + '-' * 10)
        print('Next Data synchronization: ', (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime(
            "%Y-%m-%d %H:%M:%S"))

    def my_job2(self, args):
        print('-' * 10 + 'my_job2' + '-' * 10)
        print('Next Data synchronization: ', (datetime.datetime.now() + datetime.timedelta(hours=24)).strftime(
            "%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    demo = Demo()
    print('start')

    sched = BlockingScheduler()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(now)

    sched.add_job(demo.my_job1, 'interval', seconds=60, args=['text'], id='my_job')  # 每隔一分钟执行一次
    sched.add_job(demo.my_job2, 'cron', day_of_week='mon-fri', hour=19, minute=48, args=['text'],
                  end_date='2019-01-30')  # 工作日下午7点48运行，2019年1月30日程序停止运行
    sched.start()
