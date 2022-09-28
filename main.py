# coding: utf-8

import re

msg = 'В розыгрыше победили: id1234563, id4653, id461, id'
re.findall('id\d+', msg)  # буквы "id" и далее какие-то цифры
