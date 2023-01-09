import pandas as pd
visitors = [123, 456, 789, 987, 654, 321]
errors = [12, 45, 78, 98, 65, 32]

df = pd.DataFrame({'visitors': visitors, 'errors': errors}, index=[
                  'Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat'])
print(df)
print(df['errors'].mean())
