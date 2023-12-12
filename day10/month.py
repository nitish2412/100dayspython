def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return 1
      else:
        return 0
    else:
      return 1
  else:
    return 0
  
def days_in_month(input_year,input_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if(is_leap(input_year)):
    if input_month==2:
      return 29
  return month_days[input_month-1]
  
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)


