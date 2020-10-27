from typing import List
from .templates import Card, Template, Button
from .commons import Thumbnail, ListItem, CarouselHeader, Profile, Social

class BasicCard(Card):
    """기본 카드형 출력 요소입니다. 기본 카드는 소셜, 썸네일, 프로필 등을 통해서 사진이나 글, 인물 정보 등을 공유할 수 있습니다.
       기본 카드는 제목과 설명 외에 썸네일 그룹, 프로필, 버튼 그룹, 소셜 정보를 추가로 포함합니다.

    https://i.kakao.com/docs/skill-response-format#basiccard

    * social과 profile은 현재 미지원 상태입니다.
    """
    output_header = 'basicCard'

    def __init__(self, thumbnail: Thumbnail, title: str = None, description: str = None, 
                 profile: Profile = None, social: Social = None, buttons: List[Button] = None):
        """BasicCard 생성

        Args:
            thumbnail (Thumbnail): 카드의 상단 이미지입니다.
            title (str, optional): 카드의 제목입니다. 최대 2줄. Defaults to None.
            description (str, optional): 카드에 대한 상세 설명입니다. 최대 230자. Defaults to None.
            profile (Profile, optional): 카드의 프로필 정보입니다. Defaults to None.
            social (Social, optional): 카드의 소셜 정보입니다. Defaults to None.
            buttons (List[Button], optional): 카드의 버튼들을 포함합니다. 최대 3개. Defaults to None.
        """
        self.__dict__.update(locals())


class CommerceCard(Card):
    """커머스 카드형 출력 요소입니다. 커머스 카드는 제품에 대한 소개, 구매 안내 등을 사용자에게 전달할 수 있습니다.
       커머스 카드는 제목과 설명 외에 썸네일 그룹, 프로필, 버튼 그룹, 가격 정보를 추가로 포함합니다.

    https://i.kakao.com/docs/skill-response-format#commercecard
    """
    output_header = 'commerceCard'

    def __init__(self, description: str, price: int, currency: str, thumbnails: List[Thumbnail], buttons: List[Button],
                 discount: int = None, discountRate: int = None, discountedPrice: int = None, profile: Profile = None):
        """CommerceCard 생성

        Args:
            description (str): 제품에 대한 상세 설명입니다.	최대 76자.
            price (int): 제품의 가격입니다.
            currency (str): 제품의 가격에 대한 통화입니다. 현재 won만 가능.
            thumbnails (List[Thumbnail]): 제품에 대한 사진입니다. 현재 1개만 가능.
            buttons (List[Button]): 다양한 액션을 수행할 수 있는 버튼입니다. 1개 이상, 3개 이하.
            discount (int, optional): 제품의 가격에 대한 할인할 금액입니다. Defaults to None.
            discountRate (int, optional): 제품의 가격에 대한 할인율입니다. Defaults to None.
            discountedPrice (int, optional): 제품의 가격에 대한 할인가(할인된 가격)입니다. Defaults to None.
            profile (Profile, optional): 제품을 판매하는 프로필 정보입니다. Defaults to None.

        **Information. price, discount, discountedPrice 의 동작 방식**

            discountedPrice 가 존재하면 price, discount, discountRate 과 관계 없이 무조건 해당 값이 사용자에게 노출됩니다.
            예) price: 10000, discount: 7000, discountedPrice: 2000 인 경우, 3000 (10000 - 7000)이 아닌 2000이 사용자에게 노출
            위의 예에서 discountedPrice가 없는 경우, 3000이 사용자에게 노출
            예) price: 10000, discountRate: 70, discountedPrice: 2000 인 경우, 3000 (10000 * 0.3)이 아닌 2000이 사용자에게 노출
            discountRate은 discountedPrice를 필요로 합니다. discountedPrice가 주어지지 않으면 사용자에게 >discountRate을 노출하지 않습니다.
            discountRate과 discount가 동시에 있는 경우, discountRate을 우선적으로 노출합니다.
        """
        self.__dict__.update(locals())


class ListCard(Template):
    """리스트 카드형 출력 요소입니다. 리스트 카드는 표현하고자 하는 대상이 다수일 때, 이를 효과적으로 전달할 수 있습니다.
       헤더와 아이템을 포함하며, 헤더는 리스트 카드의 상단에 위치합니다. 리스트 상의 아이템은 각각의 구체적인 형태를 보여주며, 제목과 썸네일, 상세 설명을 포함합니다.

    https://i.kakao.com/docs/skill-response-format#listcard
    """
    output_header = 'listCard'

    def __init__(self, header: ListItem, items: List[ListItem], buttons: List[Button] = None):
        """ListCard 생성

        Args:
            header (ListItem): 카드의 상단 항목.
            items (List[ListItem]): 카드의 각각 아이템. 최대 5개
            buttons (List[Button], optional): 최대 2개. Defaults to None.
        """
        self.__dict__.update(locals())


class Carousel(Template):
    """케로셀은 여러 장의 카드를 하나의 메세지에 일렬로 포함하는 타입입니다.

    https://i.kakao.com/docs/skill-response-format#carousel
    """
    output_header = 'carousel'

    def __init__(self, items: List[Card], header: CarouselHeader = None):
        if(len(items) > 0):
            if(type(items[0]) is BasicCard):
                self.type = 'basicCard'
            elif(type(items[0] is CommerceCard)):
                self.type = 'commerceCard'
            else:
                raise NotImplementedError('basicCard 혹은 commerceCard')
        self.__dict__.update(locals())

    def to_dict(self):
        for item in self.__dict__['items']:
            item.output_header = None
        return super().to_dict()
