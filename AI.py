from aip import AipImageClassify

def plant_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):#参数是路径
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用植物识别 """
    result = client.plantDetect(image)
    return result['result'][0]["name"]

def animal_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用动物识别 """
    result = client.animalDetect(image)

    return result['result'][0]["name"]

def vegetable_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用动物识别 """
    result = client.ingredient(image)

    return result['result'][0]["name"]

def logo_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用动物识别 """
    result = client.logoSearch(image)

    return result['result'][0]["name"]

def car_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用车辆识别 """
    result = client.carDetect(image)

    return result['result'][0]["name"]

def redwine_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用红酒识别 """
    result = client.redwine(image)

    return result['result']["wineNameCn"]

def money_AI(path):
    """ 你的 APPID AK SK """
    APP_ID = '26156304'
    API_KEY = 'w5gv9bGDvXaPMM7BSIRNhchr'
    SECRET_KEY = 'GozVbSoHLFZng61V1hEHAx8GSrcO2nxZ'

    client = AipImageClassify(APP_ID,API_KEY,SECRET_KEY)

    """ 读取图片 """
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(path)

    """ 调用货币识别 """
    result = client.currency(image)

    return result['result']["currencyName"]
