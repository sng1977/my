import string
from typing import Type


class MyCar:
    def __init__(self, model='BMW', color='red', engine_capacity=2.2):
        self.__model = model
        self.__color = color
        self.__engine_capacity = engine_capacity

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def engine_capacity(self):
        return self.__engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value):
        self.__engine_capacity = value

    def move_forward(self):
        print(self.model + " moves forward")

    def move_backward(self):
        print(self.model + " moves backward")


# MyCar = MyCar(model='Mersedes')
# MyCar.engine_capacity = 1.6
# print(MyCar.model)
#
# MyCar.move_forward()
# MyCar.move_backward()

class TextProcessor:
    def __init__(self, text='default', punct=False):
        self.__text = text
        self.__isPunct = punct

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        self.__text = value

    @property
    def punct(self):
        return self.__isPunct

    # @punct.setter
    # def punct(self, value):
    #     self.__isPunct = value

    def get_clean_string(self):
        return self.__text.translate(str.maketrans('', '', string.punctuation))

    def __is_punctuatian(self, strPunct):
        if strPunct in string.punctuation:
            self.__isPunct = True
        else:
            self.__isPunct = False

        return False

    def is_punctuation(self, strPunct):
        return self.__is_punctuatian(strPunct)


# myTP = TextProcessor()
# myTP.text = '!Hi, wh?at is the weat[h]er lik?e'
# # print(myTP.get_clean_string())
#
# myTP.is_punctuation('a')
# # print(myTP.punct)


class TextLoader(TextProcessor):
    def __init__(self, clean_string='',isClearedString = False):
        TextProcessor.__init__(self)
        self.__text_processor = TextProcessor
        self.__cleanString = clean_string
        self.__isClearedString = isClearedString

    @property
    def cleanString(self):
        return self.__cleanString

    @cleanString.setter
    def cleanString(self, value):
        self.__cleanString = value

    @property
    def isClearedString(self):
        return self.__cleanString

    @isClearedString.setter
    def isClearedString(self, value):
        self.__isClearedString = value

    def set_clean_text(self):
        self.text = self.__cleanString
        self.__cleanString = self.get_clean_string()
        self.__isClearedString = True
        return self.__cleanString
        #return self.__isClearedString
        #print('Cleared string will be returned')


    #     IsCleanString
    #
    # @property
    # def IsCleanString(self):
    #     print('There was cleaned text')

# myTL = TextLoader()
# myTL.cleanString = '!Hi, wh?at is the weat[h]er lik?e'
# # print(myTL.text)
# print(myTL.cleanString)
# myTL.set_clean_text()
# print(myTL.cleanString)
#
# myTL = TextLoader()
# print(myTL.TextProcessor)
# myTL.cleanString = '!Hi, wh?at is the weat[h]er lik?e'
# print(myTL.set_clean_text())

class DataInterface(TextLoader):
    def __init__(self):
        TextLoader.__init__(self, clean_string='', isClearedString=False)
        __TL = TextLoader

    def process_texts(self, lst):
        for i in lst:
            self.cleanString = i
            print(self.set_clean_text())
            #__TL.clean_string = i
            #print(i)
            #__TL.set_clean_text(i)




myDL = DataInterface()
lst = ['!Hi, wh?at is the weat[h]er lik?e','Ou, i&t i{s go/od!']
myDL.process_texts(lst)