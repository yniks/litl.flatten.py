class flaten:
    __list=list()
    __cls=None
    def __init__(self,obj,unwrp=list):
        self.__cls=unwrp
        self.__list=obj
        if not hasattr(obj, '__iter__'):raise "Base Object is needs to have a __iter__ method defined."
        elif not type(obj)==unwrp:raise "Base Object should be the instance of Unwrappable class"
    def __iter__(self,sub=None):
        if not sub:sub=self.__list
        for each in sub:
            if type(each)==self.__cls:
                for each in self.__iter__(each):
                    yield each
            else:
                yield each
