#!/usr/bin/env python3
# coding:utf-8

__author__ = '徐育良'
import logging
import colorlog

# 日志级别类型
levelMap = {'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
            }

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red'
}

# logging.warning('Watch out!')  # 消息会被打印到控制台上
# logging.warning('I told you so')  # 这行不会被打印，因为级别低于默认级别
# logging.basicConfig(filename='example.log',level=logging.INFO)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
logging.basicConfig(  # filename='example.log', filemode='a',
    level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
