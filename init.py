import re

with open('cloud.conf', encoding='utf-8') as f:
    conf = f.read()

re_project_id = r"PROJECT_ID='(?P<PID>.+?)'"
re_user_name = r"USER_NAME='(?P<UNAME>.+)'"
re_password = r"PASSWORD='(?P<PASSWD>.+)'"

p_id = re.search(re_project_id, conf, re.M).group('PID')
p_user = re.search(re_user_name, conf, re.M).group('UNAME')
p_pass = re.search(re_password, conf, re.M).group('PASSWD')

# print(f"{p_id=}")
# print(f"{p_user=}")
# print(f"{p_pass=}")

with open('provider.tf') as f:
    provider_conf = f.read()

provider_conf = re.sub(r'username = ".+"', f'username = "{p_user}"', provider_conf)
provider_conf = re.sub(r'password = ".+"', f'password = "{p_pass}"', provider_conf)
provider_conf = re.sub(r'project_id = ".+"', f'project_id = "{p_id}"', provider_conf)


with open('provider.tf', 'w') as f:
    f.write(provider_conf)

