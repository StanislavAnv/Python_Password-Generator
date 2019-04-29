#!/usr/bin/env python
# coding: utf-8
'''
	© Copyright 2019 Stanislav https://blog.antvmail.com
	Secure Password Genearator

	The license notices

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import random
import os
import datetime

nowY = datetime.datetime.now().year
print('Secure Password Genearator v1.\n© Copyright 2014 -',nowY,'\nAuthor: Stanislav https://blog.antvmail.com\n')
file_dir = os.path.dirname(os.path.realpath(__file__))

# Starter dictionary
lc='abcdefghijklmnopqrstuvwxyz'
uc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num='1234567890'
sc_sas='!&*-./:=?_' # http://support.sas.com/kb/33/782.html
sc_oracle='@+/!$?:.()-_.' # https://docs.oracle.com/cd/E11223_01/doc.910/e11197/app_special_char.htm#MCMAD416
sc_mc='!@$&*_-+=():;,.?/' # https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements
sc_sap='()!$:;=&><?*+-_.,'# https://help.sap.com/saphelp_nw70/helpdata/en/22/41c43ac23cef2fe10000000a114084/frameset.htm
sc_db='!$*( )_-+=,.;?:'
sc_safe='!*-.=?_'


# Detect password type for special characters
print('___For what type of software password will be used?___\nSAS (1) \nOracle (2)\nMicrosoft services (3) \nSAP (4)\nPostgreSQL/MongoDB/MySQL (5) \nSafe special character list [6]\n')
pwd_type = int(input('Make a choice [6] :') or '6')
while pwd_type > 6 or pwd_type < 1:
        try:
                pwd_type = int(input('"Make a choice" supports only numbers from from 1 to 6 [6] :') or '6')
        except ValueError:
                print('Value "Make a choice" supports only numbers from 1 to 6')
                continue


# Generating password length
print('\n\n___Password length___\n')
pwd_len_lc = int(input('Lower case letter? [4] ') or '4')
while pwd_len_lc<0:
    try:
        pwd_len_lc = int(input('Lower case letters? [4] ') or '4')
    except ValueError:
        print('Value "Lower case letter" supports only numbers!')
        continue

pwd_len_uc = int(input('Upper case letters? [4] ') or '4')
while pwd_len_uc<0:
    try:
        pwd_len_uc = int(input('Upper case letters? [4] ') or '4')
    except ValueError:
        print('Value "Upper case letters" supports only numbers!')
        continue

pwd_len_num = int(input('Numbers? [2] ') or '2')
while pwd_len_num<0:
    try:
        pwd_len_num = int(input('Numbers? [2] ') or '2')
    except ValueError:
        print('Value "Numbers" supports only numbers!')
        continue

pwd_len_sc = int(input('Special characters? [2] ') or '2')
while pwd_len_sc<0:
    try:
        pwd_len_sc = int(input('Special characters? [2] ') or '2')
    except ValueError:
        print('Value "Special characters" supports only numbers!')
        continue

pwd_count = int(input('How much passwords do u need? [1] ') or '1')
while pwd_count<0:
    try:
        pwd_count = int(input('How much passwords do u need? [1] ') or '1')
    except ValueError:
        print('Value "Passwords count" supports only numbers!')
        continue

# Password Generator Core
def password_generator(pwd_type,pwd_len_lc,pwd_len_uc,pwd_len_num,pwd_len_sc,pwd_count):
    orig_file = 'generated_pwd_.txt'
    now = datetime.datetime.today().strftime('%m-%d-%Y_%H-%M-%S')
    filename, file_extension = os.path.splitext(orig_file)
    output_file = filename + now + file_extension
    output_file_path = os.path.join(file_dir, output_file)
    output_file_open = open(output_file_path,"w+")
    output_file_open.write('Created by secure password genearator\n© Copyright 2019 Stanislav https://blog.antvmail.com\n')
    while pwd_count > 0:
        lc_gen = ''.join(random.sample(lc,pwd_len_lc))
        uc_gen = ''.join(random.sample(uc,pwd_len_uc))
        num_gen = ''.join(random.sample(num,pwd_len_num))
        if pwd_type == 1:
            x5_sc_gen = ''.join(random.sample(sc_sas,pwd_len_sc))
        elif pwd_type == 2:
            x5_sc_gen = ''.join(random.sample(sc_oracle,pwd_len_sc))
        elif pwd_type == 3:
            x5_sc_gen = ''.join(random.sample(sc_mc,pwd_len_sc))
        elif pwd_type == 4:
            x5_sc_gen = ''.join(random.sample(sc_sap,pwd_len_sc))
        elif pwd_type == 5:
            x5_sc_gen = ''.join(random.sample(sc_db,pwd_len_sc))
        else:
            x5_sc_gen = ''.join(random.sample(sc_safe,pwd_len_sc))
        pass_length = pwd_len_lc+pwd_len_uc+pwd_len_num+pwd_len_sc
        password = ''.join(random.sample(lc_gen+uc_gen+num_gen+x5_sc_gen,pass_length))
        output_file_open.write(password + "\n")
        pwd_count -= 1
    output_file_open.close()
    done = (input('All passwords saved into a file '  + output_file +  ' in the folder '  + file_dir))
password_generator(pwd_type,pwd_len_lc,pwd_len_uc,pwd_len_num,pwd_len_sc,pwd_count)
