from .templates import Template

class SimpleText(Template):
    """간단한 텍스트형 출력 요소입니다.

    https://i.kakao.com/docs/skill-response-format#simpletext
    """
    output_header = 'simpleText'

    def __init__(self, text: str):
        """SimpleText 생성

        Args:
            text (str): 전달하고자 하는 텍스트입니다. 제한 : 1000자
        """
        self.__dict__.update(locals())


class SimpleImage(Template):
    """간단한 이미지형 출력 요소입니다. 이미지 링크 주소를 포함하면 이를 스크랩하여 사용자에게 전달합니다.
       이미지 링크 주소가 유효하지 않을 수 있기 때문에, 대체 텍스트를 꼭 포함해야 합니다.

    https://i.kakao.com/docs/skill-response-format#simpleimage
    """
    output_header = 'simpleImage'

    def __init__(self, imageUrl: str, altText: str):
        """SimpleImage 생성

        Args:
            imageUrl (str): 전달하고자 하는 이미지의 url입니다.
            altText (str): url이 유효하지 않은 경우, 전달되는 텍스트입니다.
        """
        self.__dict__.update(locals())
