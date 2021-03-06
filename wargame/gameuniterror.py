"""
这是一个新的包含自定义异常的模块
"""
class GameUnitError(Exception):
    """Custom exceptions class for the 'AbstractGameUnit' and its subclass"""
    def __init__(self, message=''):
        super().__init__(message)
        self.padding = '~'*50 + '\n'
        self.error_message = " Unspecified Error!"
class HealthMeterException(GameUnitError):
    """Custom exception to report Health meter related problems"""
    def __init__(self, message=''):
        super().__init__(message)
        self.error_message = (self.padding + "ERROR:Health Meter Problem"+
                              '\n' + self.padding)