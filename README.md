# kakao-skill-template-builder

- [kakao-skill-template-builder](#kakao-skill-template-builder)
  - [특징](#특징)
  - [Installation](#installation)
  - [Example](#example)

kakao i openbuilder skill response template builder ⚒ for python 🐍

파이썬에서 카카오 i 오픈빌더의 응답 타입별 JSON 포맷을 생성하는 도구 입니다.

## 특징

👌 오픈빌더 도움말의 모든 [응답 타입별 JSON 포맷](https://i.kakao.com/docs/skill-response-format#skillpayload)을 만들 수 있습니다. 모두 다 테스트 해봤어요! 😊 `tests/test_builder.py`를 참고!

⚒ `SkillResponseBuilder` 를 이용해서 원하는대로 이것저것 섞인 대답을 만들 수 있습니다!

🐍 파이썬의 local 변수를 이용해서 코드가 엄청 짧아요! 고치기 쉽다는 뜻이죠.

## Installation

```bash
$ pip install kakaosb
```

## Example

1. SimpleText

```python
from kakaosb import SkillResponseBuilder, SimpleText

sb = SkillResponseBuilder([SimpleText('Hello Kakao!')])
res_dict = sb.to_dict()  # 사전 형식 변환
res_json = sb.to_json(indent=4)  # json 형식 변환
```

2. 베이직 카드

```python
from kakaosb import SkillResponseBuilder, BasicCard, Thumbnail, Profile, Social, MessageButton, WeblinkButton

sb = SkillResponseBuilder()
basicCard = BasicCard(
    thumbnail=Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg'),
    title='보물상자',
    description='보물상자 안에는 뭐가 있을까',
    profile=Profile('보물상자', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM'),
    social=Social(1238, 8, 780),
    buttons=[
        MessageButton('열어보기', '짜잔! 우리가 찾던 보물입니다'),
        WeblinkButton('구경하기', 'https://e.kakao.com/t/hello-ryan')
    ])
sb.append(basicCard)
res_dict = sb.to_dict()  # 사전 형식 변환
res_json = sb.to_json(indent=4)  # json 형식 변환
```

3. mix

```python
from kakaosb import SkillResponseBuilder, SimpleText, SimpleImage

sb = SkillResponseBuilder()
sb.append(SimpleText('Hello Kakao!'))
sb.append(SimpleImage('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg', '보물상자입니다'))
sb.append(SimpleText('Bye Bye 🧤'))
res_dict = sb.to_dict()  # 사전 형식 변환
res_json = sb.to_json(indent=4)  # json 형식 변환
```