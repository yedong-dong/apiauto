import logging.handlers
from config.ENV import BASE_DIR as DIR_NAME


class GetLogger:
    '''
    当已经创建了logger对象的时候，那么之后就不在创建了，也就是只创建一次对象
    '''
    # 把logger对象的初始值设置为None
    logger = None

    # 创建logger，并且返回这个logger
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            ########创建日志器，控制他的创建次数
            cls.logger = logging.getLogger('apiautotest')  # 不是None
            # 设置总的级别，debug/info/warning/error
            # 只有比debug级别高的日志才会被显示出来
            cls.logger.setLevel(logging.DEBUG)
            # 2获取格式器
            # 2.1 要给格式器设置要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            # 2.2创建格式器，并且给他设置样式
            fm = logging.Formatter(fmt)
            # 3.创建处理器 按照时间进行切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename=DIR_NAME +'/logs/requestslog.log',  # 原日志文件
                                                           when='H',  # 间隔多长时间把日志存放到新的文件中
                                                           interval=1,
                                                           backupCount=3,  # 除了原日志文件，还有3个备份
                                                           encoding='utf-8'
                                                           )
            #这是在控制台上打印日志信息
            logging.basicConfig(level=logging.DEBUG,format=fmt)

            # 在处理器中添加格式器
            #格式器可以初始化日志记录的内容格式，结合LogRecord对象提供的属性，可以设置不同的日志格式
            #logging.Formatter(fmt=None, datefmt=None, style='％')
            #fmt：日志格式参数，默认为None，如果不特别指定fmt，则使用’%(message)s’格式
            #datafmt：时间格式参数，默认为None，如果不特别指定datafmt，则使用formatTime()文档中描述的格式
            #style：风格参数，默认为’%’，也支持’$’，’{'格式
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)

            # return cls.logger
        return cls.logger


if __name__ == '__main__':
    logger = GetLogger.get_logger()
    logger.debug('调试')  # 相当print小括号中的信息
    logger.info('信息')
    logger.warning('警告')
    name = 'yaoyao'
    logger.error('这个变量是{}'.format(name))
    logger.critical('致命的')
