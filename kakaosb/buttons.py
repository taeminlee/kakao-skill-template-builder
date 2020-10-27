from typing import Dict, Any
from .templates import Button

class MessageButton(Button):
    """사용자의 발화로 messageText를 실행합니다. (바로가기 응답의 메세지 연결 기능과 동일)
    """
    def __init__(self, label: str, messageText: str = None, extra: Dict[str, Any] = None):
        """메시지 응답 버튼 템플릿

        messageText가 있다면, 해당 messageText가 사용자의 발화로 나가게 됩니다.
        messageText가 없다면, button의 label이 사용자의 발화로 나가게 됩니다.

        Args:
            label (str): 버튼에 적히는 문구입니다. 버튼 14자(가로 배열 2개 8자)
            messageText (str, optional): 사용자의 발화로 messageText를 내보냅니다. (바로가기 응답의 메세지 연결 기능과 동일) Defaults to None.
        """
        self.action = 'message'
        self.__dict__.update(locals())


class WeblinkButton(Button):
    """웹 브라우저를 열고 webLinkUrl 의 주소로 이동합니다.
    """
    def __init__(self, label: str, webLinkUrl: str, extra: Dict[str, Any] = None):
        """웹링크 응답 버튼 템플릿

        Args:
            label (str): 버튼에 적히는 문구입니다. 버튼 14자(가로 배열 2개 8자)
            webLinkUrl (str): 웹 브라우저를 열고 webLinkUrl 의 주소로 이동합니다. URL
            extra (Dict[str, Any], optional): block이나 message action으로 블록 호출시, 스킬 서버에 추가적으로 제공하는 정보. Defaults to None.
        """
        self.action = 'webLink'
        self.__dict__.update(locals())


class PhoneButton(Button):
    """phoneNumber에 있는 번호로 전화를 겁니다.
    """
    def __init__(self, label: str, phoneNumber: str, extra: Dict[str, Any] = None):
        """폰 버튼 생성

        Args:
            label (str): 버튼에 적히는 문구입니다. 버튼 14자(가로 배열 2개 8자)
            phoneNumber (str): phoneNumber에 있는 번호로 전화를 겁니다.	전화번호.
            extra (Dict[str, Any], optional): block이나 message action으로 블록 호출시, 스킬 서버에 추가적으로 제공하는 정보. Defaults to None.
        """
        self.action = 'phone'
        self.__dict__.update(locals())


class BlockButton(Button):
    """blockId를 갖는 블록을 호출합니다. (바로가기 응답의 블록 연결 기능과 동일)
    """
    def __init__(self, label, blockId, messageText: str = None, extra: Dict[str, Any] = None):
        """블록 버튼 생성

        Args:
            label (str): 버튼에 적히는 문구입니다. 버튼 14자(가로 배열 2개 8자)
            blockId ([type]): blockId를 갖는 블록을 호출합니다. (바로가기 응답의 블록 연결 기능과 동일). 존재하는 블록 id.
            messageText (str, optional): 블록 연결시 사용자의 발화로 노출됩니다.. Defaults to None.
            extra (Dict[str, Any], optional): block이나 message action으로 블록 호출시, 스킬 서버에 추가적으로 제공하는 정보. Defaults to None.
        """
        self.action = 'block'
        self.__dict__.update(locals())

class ShareButton(Button):
    """말풍선을 다른 유저에게 공유합니다. share action은 특히 케로셀을 공유해야 하는 경우 유용합니다.
    """
    def __init__(self, label, extra: Dict[str, Any] = None):
        """공유 버튼

        Args:
            piplabel (str): 버튼에 적히는 문구입니다. 버튼 14자(가로 배열 2개 8자)
            extra (Dict[str, Any], optional): block이나 message action으로 블록 호출시, 스킬 서버에 추가적으로 제공하는 정보. Defaults to None.
        """
        self.action = 'share'
        self.__dict__.update(locals())
