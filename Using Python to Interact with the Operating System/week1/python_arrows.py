import arrow
date = arrow.get('2023-01-09', 'YYYY-MM-DD')
print(date)

new_date = date.shift(weeks=+4).format('MMM DD YYYY')
print(new_date)
