from typing import List, Dict, Union, Iterable

# 템플릿 #


class Template:
    """템플릿 클래스
    """
    output_header = None

    def __init__(self, **kwargs):
        """ 모든 키워드 인자를 내부 변수에 저장한다. """
        self.__dict__.update(kwargs)

    def locals_to_dict(self):
        """ 내부 변수들을 가공하여 json 변환 가능한 딕셔너리 형태로 변환한다.
        
        **가공 규칙**
        
        1. key가 self인 경우 제외한다.
        2. value가 None인 경우 제외한다.
        3. Template object인 경우 to_dict()를 호출하여 json 변환 가능하게 한다.
        4. List object인 경우 element마다 to_dict()를 호출하여 json 변환 가능하게 한다.
        """
        def unpack(v):
            if(issubclass(type(v), Template)):  # 규칙 3
                return v.to_dict()
            if type(v) is list:  # 규칙 4
                return [obj.to_dict() if issubclass(type(obj), Template) else obj for obj in v]
            return v

        return {k: unpack(v)
                for k, v in self.__dict__.items()
                if k != 'self' and v is not None}  # 규칙 1, 2

    def to_dict(self):
        """ json 변환 가능한 딕셔너리 형태로 변환한다. """
        # print(self.locals_to_dict())
        if self.output_header is None:
            return self.locals_to_dict()
        else:
            return {self.output_header: self.locals_to_dict()}
    
    def set_forwardable(self, forwardable: bool = None):
        """forwardable

        전달하기 아이콘을 스킬을 통해 출력하기 위해서는 말풍선이 단일형이면서 버튼이 포함되지 않은 경우에만 설정 가능합니다.

        Args:
            forwardable (bool, optional): 말풍선에 전달하기 아이콘을 노출합니다. default to None.
        """
        self.forwardable = forwardable


class Button(Template):
    """ 버튼 템플릿. 단독으로 사용하지 않고, PhoneButton 혹은 BlockButton 등을 이용해야 한다. """
    def __init__(self):
        pass


class Card(Template):
    """카드 템플릿. 단독으로 사용하지 않고, BasicCard 혹은 ComerceCard를 이용해야 한다. """
    def __init__(self):
        pass


# 퀵 리플라이 #


class QuickReply(Template):
    """QuickReply 템플릿

    https://i.kakao.com/docs/skill-response-format#quickreplies
    """
    def __init__(self, label='레이블', messageText='발화', action='message', blockId=None, extra=None):
        self.__dict__.update(locals())


# 컨텍스트 컨트롤 #


class ContextValue(Template):
    """컨텍스트 밸류

    https://i.kakao.com/docs/skill-response-format#contextvalue-%EC%83%81%EC%84%B8-%ED%95%84%EB%93%9C
    """
    def __init__(self, name: str, lifeSpan: int, params: Dict[str, str] = None):
        """[summary]

        Args:
            name (str): 수정하려는 output 컨텍스트의 이름.
            lifeSpan (int): 수정하려는 ouptut 컨텍스트의 lifeSpan.
            params (Dict[str, str], optional): output 컨텍스트에 저장하는 추가 데이터. Defaults to None.
        """
        self.__dict__.update(locals())


class ContextControl(Template):
    """context control 필드는 블록에서 생성한 outputContext의 lifeSpan, params 등을 제어할 수 있습니다.

    https://i.kakao.com/docs/skill-response-format#contextcontrol
    """
    output_header = 'context'

    def __init__(self, values: List[ContextValue]):
        self.__dict__.update(locals())


# 데이터 #

class Data(Template):
    def __init__(self, data: Dict[str, object]):
        self.__dict__.update(locals())
