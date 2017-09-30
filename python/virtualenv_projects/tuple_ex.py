#!/Users/ansuman/Github/Projects/python/virtualenv/bin/python
#
""" Tuple Example. """


class ex_class:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def ex_func(TupleObj):
        print(TupleObj)

    @classmethod
    def init_with_tuple(cls, tupleObj):
        return cls(*tupleObj)

    def __repr__(self):
        return 'ex_class({}, {}, {}, {})'.format(self.a, self.b, self.c, self.d)

    # def __str__(self):
    #    pass


def main():
    ex_classObj_1 = ex_class.init_with_tuple((1, 2, 3, 4))
    print(ex_classObj_1)

    ex_classObj_2 = ex_class()
    print(ex_classObj_2)


if __name__ == '__main__':
    main()
