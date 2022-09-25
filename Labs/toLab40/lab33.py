def pause():
    print('-'*20)


projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

projects_leaders = zip(projects, leaders)

for project, leader in projects_leaders:
    print('The leader of {} is {}'.format(project, leader))
pause()

dates = ['2016-06-23', '2016-08-29', '1994-01-01']
projects_dates_leaders = zip(projects, dates, leaders)

for project, date, leader in projects_dates_leaders:
    print('The leader of {} started {} is {}'.format(project, date, leader))
pause()


enumerated_projects_info = enumerate(projects_dates_leaders)

for x, (project, date, leader) in enumerated_projects_info:
    print('{} The leader of {} started {} is {}'.format(x + 1, project, date, leader))
pause()

enumerated_projects_info = enumerate(zip(projects, dates, leaders))

for x, (project, date, leader) in enumerated_projects_info:
    print('{} The leader of {} started {} is {}'.format(x + 1, project, date, leader))
