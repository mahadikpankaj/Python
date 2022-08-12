import datetime as dt

str_dt1 = '11-08-2022 00:00:00.00000' #'02-12-2021 00:00:00.00000'
#str_dt2 = '23-07-2023 00:00:00.00000'
#str_dt2 = '30-08-2021 00:00:00.00000'
str_dt2 = '07-04-2022 00:00:00.00000'

dt1 = dt.datetime.strptime(str_dt1, "%d-%m-%Y %H:%M:%S.%f")

dt_now = dt.datetime.now()
# days_after = 21 * 6
#days_after = 126 * 2
days_after = 126 * 2 -2

#dt2 = dt.datetime.strptime(str_dt2, "%d-%m-%Y %H:%M:%S.%f")
dt2 = dt1 + dt.timedelta(days=days_after)
#dt2 = dt_now + dt.timedelta(days=days_after)
#dt2 = dt_now

rounded_dt1 = dt1.replace(hour=0, minute=0, second=0, microsecond=0)
rounded_dt2 = dt2.replace(hour=0, minute=0, second=0, microsecond=0)
str_rounded_dt2 = rounded_dt2.strftime("%B %d,%Y");

delta = (rounded_dt2 - rounded_dt1)

diff = round(delta.days)
sign = diff / abs(diff)
diff = abs(diff)

diff_mod_21 = diff%21
diff_mod_18 = diff%18
if (sign < 0):
	diff_mod_21 = 21 - diff_mod_21
	diff_mod_18 = 18 - diff_mod_18


ch_21 = int(diff_mod_21 + 1)
ch_18 = int(diff_mod_18 + 1)

if (ch_21==22):
	ch_21 = 1
		
if (ch_18==19):
	ch_18 = 1

print(f'Date: {str_rounded_dt2}')
print(f'ch_21 = {ch_21}, ch_18 = {ch_18}')
