from datetime import datetime

def create_time_spans(symbol):
    function = '''
def time_span(start, end=datetime.now()):
    duration = end - start
    duration_in_s = duration.total_seconds()
    return divmod(duration_in_s, {})[0]
'''
    number = 1
    if symbol == 'm':
        number = 60
    elif symbol == 'h':
        number = 3_600
    elif symbol == 'd':
        number = 86_400

    exec(function.format(number), globals())
    return time_span


time_span_m = create_time_spans('m')
time_span_h = create_time_spans('h')
time_span_d = create_time_spans('d')

start = datetime(2019, 1, 1, 0, 0, 0)
print(time_span_m(start))
print(time_span_d(start))
print(time_span_h(start))

