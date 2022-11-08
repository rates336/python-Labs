def show_progress(how_many, character='*'):
    print(character * how_many)


show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10, '-')
show_progress(15, '+')


def double(x):
    return 2 * x


def square(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x/2


def generate_values(function_name, values_list):
    result_list = []
    for x in values_list:
        result_list.append(function_name(x))
    return result_list


number = 8
transformations = [double, square, negative, div2, number]
print(transformations)
counter = 0
for y in transformations[:4]:
    transformations.append(y(transformations[-1]))
    for x in transformations[:4]:
        print(x(transformations[-1]))

print(generate_values(double, range(11)))
print(generate_values(square, range(11)))
print(generate_values(negative, range(11)))
print(generate_values(div2, range(11)))

