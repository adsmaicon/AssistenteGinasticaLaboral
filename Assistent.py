from AwsAssistent import AwsAssistent
from GoogleAssistent import GoogleAssistent
from AssitentTypeEnum import AssitentTypeEnum


class Assistent(object):

    @staticmethod
    def factory(type):

        if type == AssitentTypeEnum.AWS : return AwsAssistent()
        if type == AssitentTypeEnum.GOOGLE: return GoogleAssistent()
        assert 0, "Bad shape creation: " + type