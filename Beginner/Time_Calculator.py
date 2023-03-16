def add_time(start, duration, starting_day=None):
  days_list = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
               'Saturday', 'Sunday')
  which_day = ''

  start_time = start.split()[0]
  start_AM_PM = start.split()[1]
  start_time_hours = start_time.split(':')[0]
  start_time_minutes = start_time.split(':')[1]

  duration_hours = duration.split(':')[0]
  duration_minutes = duration.split(':')[1]

  new_time = ''
  new_time_hours = 0
  new_time_minutes = 0
  new_time_AM_PM = start_AM_PM

  # calculating new hours and minutes
  new_time_hours = int(start_time_hours) + int(duration_hours)
  new_time_minutes = int(start_time_minutes) + int(duration_minutes)

  # updating hours and minutes
  new_time_hours += new_time_minutes // 60
  new_time_minutes = new_time_minutes % 60

  # updating hours and meridian
  number_of_days = new_time_hours // 24
  if number_of_days == 0:
    if starting_day is not None:
      which_day = ', ' + (starting_day.lower()).capitalize()

    if new_time_hours >= 12:
      new_time_AM_PM = 'PM' if start_AM_PM == 'AM' else 'AM'; number_of_days += 1
      if new_time_hours > 12: new_time_hours -= 12
      if number_of_days >= 1 and start_AM_PM == 'PM': which_day = ' (next day)'
  
  else:
    new_time_hours -= 24 * number_of_days
    if new_time_hours >= 12:
      new_time_AM_PM = 'PM' if start_AM_PM == 'AM' else 'AM'; number_of_days += 1
      if new_time_hours > 12: new_time_hours -= 12
        
    which_day = ' (next day)'
    if number_of_days > 1:
      which_day = ' (' + str(number_of_days) + ' days later)'
    
    if starting_day is not None:
      index_starting_day = days_list.index((starting_day.lower()).capitalize())
      which_day = ', ' + days_list[(index_starting_day + number_of_days) %
                                   7] + which_day

  

  new_time = str(
    new_time_hours
  ) + ':' + f'{new_time_minutes:02}' + ' ' + new_time_AM_PM + which_day
  return new_time

