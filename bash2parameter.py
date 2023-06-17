import os


def find_value(dict_parameter, right): #找出${}中间的内容并替换
    after_left_bracket = right.split('{')[1]
    in_bracket, after_right_bracket = after_left_bracket.split('}')
    in_bracket_value = dict_parameter[in_bracket]
    return in_bracket_value + '' + after_right_bracket


f = open("D:\PycharmProject\Bike\cmd.sh", "r")
lines = f.readlines()  # 读取全部内容

parameter_dict = dict()
for line in lines:
    if line != '\n':
        valid_var_assign = line.split('#')[0]
        if len(valid_var_assign) == 0:
            continue
        print(valid_var_assign)
        left, right = valid_var_assign.split('=')
        right = right.replace('\n', '')
        right = right.replace('"', '')
        if '$' in right:
            right = find_value(dict_parameter=parameter_dict, right=right)
        parameter_dict[left] = right

# print(parameter_dict)

template = ''
for i in parameter_dict.keys():
    template = template + ' --' + i + ' ' + parameter_dict[i]
print(template)
