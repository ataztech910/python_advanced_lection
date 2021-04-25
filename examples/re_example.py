import re
text = """100 ИНФ  Информатика
213 МАТ  Математика  
156 АНГ  Английский"""
print(re.split('\s+', text))

regex_num = re.compile('\d+')
print(regex_num.findall(text))