from .templates import Template

class Link(Template):
    """링크

    Information. 링크 우선순위 링크는 다음과 같은 우선순위를 갖습니다.

    pc: pc < web
    모바일: mobile < web
    예를 들면, pc에 대하여 링크 값이 webURL, pcURL를 가지면 위 규칙에 따라 webURL이 노출됩니다.
    모바일 기기에 대하여 Link의 값이 webURL, mobileURL를 가지면 위 규칙에 따라 webURL이 노출됩니다.
    """
    def __init__(self, pc: str = None, mobile: str = None, web: str = None):
        """링크 생성

        Args:
            pc (str, optional): pc의 웹을 실행하는 link입니다. Defaults to None.
            mobile (str, optional): mobile의 웹을 실행하는 link입니다. Defaults to None.
            web (str, optional): 모든 기기에서 웹을 실행하는 link입니다. Defaults to None.
        """
        self.__dict__.update(locals())


class Thumbnail(Template):
    """썸네일 템플릿
    """
    def __init__(self, imageUrl: str, link: Link = None, fixedRatio: bool = None, width: int = None, height: int = None):
        """썸네일 생성

        Args:
            imageUrl (str): 이미지의 url입니다.
            link (Link, optional): 이미지 클릭시 작동하는 link입니다. Defaults to None.
            fixedRatio (bool, optional): true: 이미지 영역을 1:1 비율로 두고 이미지의 원본 비율을 유지합니다. 이미지가 없는 영역은 흰색으로 노출합니다.
                                         false: 이미지 영역을 2:1 비율로 두고 이미지의 가운데를 크롭하여 노출합니다.
                                         Defaults to None. if None act False
            width (int, optional): fixedRatio를 true로 설정할 경우 필요한 값입니다. 실제 이미지 사이즈와 다른 값일 경우 원본이미지와 다르게 표현될 수 있습니다. Defaults to None.
            height (int, optional): fixedRatio를 true로 설정할 경우 필요한 값입니다. 실제 이미지 사이즈와 다른 값일 경우 원본이미지와 다르게 표현될 수 있습니다. Defaults to None.
        """
        self.__dict__.update(locals())


class ListItem(Template):
    """리스트 아이템
    """
    def __init__(self, title: str, description: str = None, imageUrl: str = None, link: Link = None):
        """리스트 아이템 생성

        Args:
            title (str): header에 들어가는 경우, listCard의 제목이 됩니다. items에 들어가는 경우, 해당 항목의 제목이 됩니다.
            description (str, optional): header에 들어가는 경우, 아무런 작동을 하지 않습니다.
                                         items에 들어가는 경우, 해당 항목의 설명이 됩니다. Defaults to None.
            imageUrl (str, optional): items에 들어가는 경우, 해당 항목의 우측 안내 사진이 됩니다. Defaults to None.
            link (Link, optional): 클릭시 작동하는 링크입니다. Defaults to None.
        """
        self.__dict__.update(locals())


class CarouselHeader(Template):
    """캐러셀 헤더
    """
    def __init__(self, title: str, description: str, thumbnail: Thumbnail):
        """캐러셀 헤더 생성

        Args:
            title (str): 케로셀 헤드 제목. 최대 2줄 (한 줄에 들어갈 수 있는 글자 수는 기기에 따라 달라집니다.)
            description (str): 케로셀 헤드 설명. 최대 3줄 (한 줄에 들어갈 수 있는 글자 수는 기기에 따라 달라집니다.)
            thumbnail (Thumbnail): 케로셀 헤드 배경 이미지. 현재 imageUrl 값만 지원합니다.
        """
        self.__dict__.update(locals())


class Profile(Template):
    """프로파일 (kakao i 미지원)
    """
    def __init__(self, nickname: str, imageUrl: str = None):
        """프로파일 생성

        Args:
            nickname (str): 프로필 이름	
            imageUrl (str, optional): 프로필 이미지. Defaults to None.
        """
        self.__dict__.update(locals())


class Social(Template):
    """소셜 (kakao i 미지원)
    """
    def __init__(self, like: int, comment: int, share: int):
        """소셜 생성

        Args:
            like (int): 좋아요
            comment (int): 댓글
            share (int): 공유
        """
        self.__dict__.update(locals())
