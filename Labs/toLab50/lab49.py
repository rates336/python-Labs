class NoDuplicates:

    def __init__(self, obj):
        self.unique_values = {obj: obj}

    def __call__(self, *args):
        for x in args:
            self.unique_values.setdefault(x, x)

    def get_list_objects(self):
        return list(self.unique_values.keys())

    def show_objects_in_list(self):
        print(self.get_list_objects())


my_no_dup_list = NoDuplicates('str')
my_no_dup_list('int')
my_no_dup_list('long', 'short', 'byte')
my_no_dup_list('int')
my_no_dup_list.show_objects_in_list()
