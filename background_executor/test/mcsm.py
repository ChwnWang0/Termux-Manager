import os
import wprint
import re
import threading

import mcsm_api
switch = mcsm_api.mcsm_controller() # 注册控制器

import json

# 数据交换目录
根目录 = 'E:\\项目\\Termux\\Termux-Manager\\background_executor\\test\\data'


def 保存结果(message_data):    
    # 以覆盖方式写入文件，如果没有该文件就创建一个
    with open(根目录 + '\\-1-mcsm_return.json', 'w') as file:
        file.write(json.dumps(message_data))

def 执行(data):
    if data['request_type'] == 'task': # 请求类型 task(任务) check(查看)
        # 执行任务
        if data['data'][0]['switch'] == 'on':
            wprint.wprint('-3-开启操作')
            # 开启
            if switch.state() != 'on':
                switch.switch('on')
        elif data['data'][0]['switch'] == 'off':
            wprint.wprint('-4-关闭操作')
            # 关闭
            # wprint.wprint(switch.state())
            if switch.state() != 'off':
                switch.switch('off')
    elif data['request_type'] == 'check':
        wprint.wprint('-5-查看操作')
        # 初始化参数
        message_data = {
            'name' : 'mcsm_return',
            'request_type' : 'return_data',
            'data' : [{
                'switch' : 'off' # 开关 on开启 off关闭
            }], 
        }

        # 查看状态
        if switch.state() == 'on':
            message_data['data'][0]['switch'] = 'on'
        elif switch.state() == 'off':
            message_data['data'][0]['switch'] = 'off'
        
        # 保存结果
        保存结果(message_data)


# 遍历文件
file_list = os.listdir(根目录)
for file in file_list:
    # wprint.wprint(file)
    if 'mcsm_sw' in file:
        result = re.search(r'-(.*?)-', file)
        if result:
            wprint.wprint(result.group(1))
            with open(file, 'r') as file:
                data = json.loads(file)
            os.remove(根目录 + '\\' + file)
            thread1 = threading.Thread(target=执行, args=(data))
            thread1.start()
            
            
