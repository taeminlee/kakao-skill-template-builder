from kakaosb import SkillResponseBuilder
from kakaosb import SimpleText, SimpleImage, BasicCard, CommerceCard, ListCard, Carousel
from kakaosb import QuickReply, Data, ContextValue, ContextControl
from kakaosb import Thumbnail, Link, Profile, Social, ListItem, CarouselHeader
from kakaosb import MessageButton, WeblinkButton, PhoneButton, ShareButton

import pytest

def test_simpletext():
	# 간단 텍스트 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-4
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"simpleText": {
						"text": "간단한 텍스트 요소입니다."
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	sb.append(SimpleText('간단한 텍스트 요소입니다.'))
	assert(trueDict == sb.to_dict())

def test_simpleimage():
	# 간단 이미지 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-5
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"simpleImage": {
						"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
						"altText": "보물상자입니다"
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	sb.append(SimpleImage('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg', '보물상자입니다'))
	assert(trueDict == sb.to_dict())

def test_basiccard():
	# 베이직 카드 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-6
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
			{
				"basicCard": {
					"title": "보물상자",
					"description": "보물상자 안에는 뭐가 있을까",
					"thumbnail": {
						"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
					},
					"profile": {
						"imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
						"nickname": "보물상자"
					},
					"social": {
						"like": 1238,
						"comment": 8,
						"share": 780
					},
					"buttons": [
						{
							"action": "message",
							"label": "열어보기",
							"messageText": "짜잔! 우리가 찾던 보물입니다"
						},
						{
							"action":  "webLink",
							"label": "구경하기",
							"webLinkUrl": "https://e.kakao.com/t/hello-ryan"
						}
					]
				}
			}
			]
		}
	}
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
	assert(trueDict == sb.to_dict())

def test_commerceCard():
	# 커머스 카드 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-7
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"commerceCard": {
						"description": "따끈따끈한 보물 상자 팝니다",
						"price": 10000,
						"discount": 1000,
						"currency": "won",
						"thumbnails": [
							{
							"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
							"link": {
								"web": "https://store.kakaofriends.com/kr/products/1542"
								}
							}
						],
						"profile": {
							"imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
							"nickname": "보물상자 팝니다"
						},
						"buttons": [
							{
								"label": "구매하기",
								"action": "webLink",
								"webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
							},
							{
								"label": "전화하기",
								"action": "phone",
								"phoneNumber": "354-86-00070"
							},
							{
								"label": "공유하기",
								"action": "share"
							}
						]
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	thumbnails = [Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg',
							Link(web='https://store.kakaofriends.com/kr/products/1542'))]
	profile = Profile('보물상자 팝니다', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM')
	btn1 = WeblinkButton('구매하기', 'https://store.kakaofriends.com/kr/products/1542')
	btn2 = PhoneButton('전화하기', '354-86-00070')
	btn3 = ShareButton('공유하기')
	buttons = [btn1, btn2, btn3]
	commerceCard = CommerceCard('따끈따끈한 보물 상자 팝니다', 10000, 'won', thumbnails, buttons, 1000, profile=profile)
	sb.append(commerceCard)
	assert(trueDict == sb.to_dict())

def test_listCard():
	# 리스트 카드 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-8
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"listCard": {
						"header": {
							"title": "카카오 i 디벨로퍼스를 소개합니다"
						},
						"items": [
							{
								"title": "Kakao i Developers",
								"description": "새로운 AI의 내일과 일상의 변화",
								"imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
								"link": {
									"web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
								}
							},
							{
								"title": "Kakao i Open Builder",
								"description": "카카오톡 채널 챗봇 만들기",
								"imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
								"link": {
									"web": "https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
								}
							},
							{
								"title": "Kakao i Voice Service",
								"description": "보이스봇 / KVS 제휴 신청하기",
								"imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
								"link": {
									"web": "https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98"
								}
							}
						],
						"buttons": [
							{
							"label": "구경가기",
							"action": "webLink",
							"webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
							}
						]
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	item1 = ListItem('Kakao i Developers', '새로운 AI의 내일과 일상의 변화', 'http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg',
			 		 Link(web='https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)'))
	item2 = ListItem('Kakao i Open Builder', '카카오톡 채널 챗봇 만들기', 'http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg',
			 		 Link(web='https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)'))
	item3 = ListItem('Kakao i Voice Service', '보이스봇 / KVS 제휴 신청하기', 'http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg',
			 		 Link(web='https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98'))
	items = [item1, item2, item3]
	buttons = [WeblinkButton('구경가기', 'https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88')]
	listCard = ListCard(ListItem('카카오 i 디벨로퍼스를 소개합니다'), items, buttons)
	sb.append(listCard)
	assert(trueDict == sb.to_dict())

def test_carousel():
	# 케로셀 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C%EC%BD%94%EB%93%9C
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"carousel": {
						"type": "basicCard",
						"items": [
							{
								"title": "보물상자",
								"description": "보물상자 안에는 뭐가 있을까",
								"thumbnail": {
									"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
								},
								"buttons": [
									{
										"action": "message",
										"label": "열어보기",
										"messageText": "짜잔! 우리가 찾던 보물입니다"
									},
									{
										"action":  "webLink",
										"label": "구경하기",
										"webLinkUrl": "https://e.kakao.com/t/hello-ryan"
									}
								]
							},
							{
								"title": "보물상자2",
								"description": "보물상자2 안에는 뭐가 있을까",
								"thumbnail": {
									"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
								},
								"buttons": [
									{
										"action": "message",
										"label": "열어보기",
										"messageText": "짜잔! 우리가 찾던 보물입니다"
									},
									{
										"action":  "webLink",
										"label": "구경하기",
										"webLinkUrl": "https://e.kakao.com/t/hello-ryan"
									}
								]
							},
							{
								"title": "보물상자3",
								"description": "보물상자3 안에는 뭐가 있을까",
								"thumbnail": {
									"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
								},
								"buttons": [
									{
										"action": "message",
										"label": "열어보기",
										"messageText": "짜잔! 우리가 찾던 보물입니다"
									},
									{
										"action":  "webLink",
										"label": "구경하기",
										"webLinkUrl": "https://e.kakao.com/t/hello-ryan"
										}
								]
							}
						]
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	bc1 = BasicCard(thumbnail=Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg'),
			  		title='보물상자',
			  		description='보물상자 안에는 뭐가 있을까',
			  		buttons=[
				  		MessageButton('열어보기', '짜잔! 우리가 찾던 보물입니다'),
				  		WeblinkButton('구경하기', 'https://e.kakao.com/t/hello-ryan')
			  		])
	bc2 = BasicCard(thumbnail=Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg'),
			  		title='보물상자2',
			  		description='보물상자2 안에는 뭐가 있을까',
			  		buttons=[
				  		MessageButton('열어보기', '짜잔! 우리가 찾던 보물입니다'),
				  		WeblinkButton('구경하기', 'https://e.kakao.com/t/hello-ryan')
			  		])
	bc3 = BasicCard(thumbnail=Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg'),
			  		title='보물상자3',
			  		description='보물상자3 안에는 뭐가 있을까',
			  		buttons=[
				  		MessageButton('열어보기', '짜잔! 우리가 찾던 보물입니다'),
				  		WeblinkButton('구경하기', 'https://e.kakao.com/t/hello-ryan')
			  		])
	carousel = Carousel(items=[bc1, bc2, bc3])
	sb.append(carousel)
	assert(trueDict == sb.to_dict())

def test_carouselheader():
	# 케로셀 헤더 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-10
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"carousel": {
						"type": "commerceCard",
						"header": {
							"title": "커머스 카드\n케로셀 헤드 예제",
							"thumbnail": {
							"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
							}
						},
						"items": [
							{
								"description": "따끈따끈한 보물 상자 팝니다",
								"price": 10000,
								"discount": 1000,
								"currency": "won",
								"thumbnails": [
									{
										"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
										"link": {
											"web": "https://store.kakaofriends.com/kr/products/1542"
										}
									}
								],
								"profile": {
									"imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
									"nickname": "보물상자 팝니다"
								},
								"buttons": [
									{
										"label": "구매하기",
										"action": "webLink",
										"webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
									},
									{
										"label": "전화하기",
										"action": "phone",
										"phoneNumber": "354-86-00070"
									},
									{
										"label": "공유하기",
										"action": "share"
									}
								]
							},
							{
								"description": "따끈따끈한 보물 상자 팝니다",
								"price": 10000,
								"discount": 1000,
								"currency": "won",
								"thumbnails": [
									{
										"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
										"link": {
											"web": "https://store.kakaofriends.com/kr/products/1542"
										}
									}
								],
								"profile": {
									"imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
									"nickname": "보물상자 팝니다"
								},
								"buttons": [
									{
										"label": "구매하기",
										"action": "webLink",
										"webLinkUrl": "https://store.kakaofriends.com/kr/products/1542"
									},
									{
										"label": "전화하기",
										"action": "phone",
										"phoneNumber": "354-86-00070"
									},
									{
										"label": "공유하기",
										"action": "share"
									}
								]
							}
						]
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	cc = CommerceCard(description='따끈따끈한 보물 상자 팝니다',
					  price=10000,
					  discount=1000,
					  currency='won',
					  thumbnails=[Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg',
					  			  Link(web='https://store.kakaofriends.com/kr/products/1542'))],
					  profile=Profile('보물상자 팝니다', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM'),
					  buttons=[
						  WeblinkButton('구매하기', 'https://store.kakaofriends.com/kr/products/1542'),
						  PhoneButton('전화하기', '354-86-00070'),
						  ShareButton('공유하기')
					  ])
	ch = CarouselHeader('커머스 카드\n케로셀 헤드 예제', None, thumbnail=Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg'))
	carousel = Carousel(items=[cc, cc], header=ch)
	sb.append(carousel)
	assert(trueDict == sb.to_dict())


def test_data():
	# 데이터 테스트
	# https://i.kakao.com/docs/skill-block#step-1-%EC%8A%A4%ED%82%AC-%EC%84%9C%EB%B2%84%EC%97%90%EC%84%9C-%EC%9D%91%EB%8B%B5%EA%B0%92-%EC%84%A4%EC%A0%95
	# 스킬 서버에서 응답값 설정
	trueDict = {
		"version": "2.0",
		"data": {
			"msg": "HI",
			"name": "Ryan",
			"position": "Senior Managing Director"
		}
	}
	sb = SkillResponseBuilder()
	data = Data({'msg': 'HI', 'name': 'Ryan', 'position': 'Senior Managing Director'})
	sb.append(data)
	assert(trueDict == sb.to_dict())

def test_context():
	# 컨텍스트 컨트롤 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-3
	trueDict = {
		"version": "2.0",
		"context": {
			"values": [
				{
					"name": "abc",
					"lifeSpan": 10,
					"params": {
						"key1": "val1",
						"key2": "val2"
					}
				},
				{
					"name": "def",
					"lifeSpan": 5,
					"params": {
						"key3": "1",
						"key4": "true",
						"key5": "{\"jsonKey\": \"jsonVal\"}"
					}
				},
				{
					"name": "ghi",
					"lifeSpan": 0
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	cv1 = ContextValue('abc', 10, {'key1': 'val1', 'key2': 'val2'})
	cv2 = ContextValue('def', 5, {'key3': '1', 'key4': 'true', 'key5': '{"jsonKey": "jsonVal"}'})
	cv3 = ContextValue('ghi', 0)
	cc = ContextControl([cv1, cv2, cv3])
	sb.append(cc)
	assert(trueDict == sb.to_dict())

def test_forwardable():
	# 전달하기 테스트
	# https://i.kakao.com/docs/skill-response-format#%EC%98%88%EC%A0%9C-%EC%BD%94%EB%93%9C-9
	trueDict = {
		"version": "2.0",
		"template": {
			"outputs": [
				{
					"basicCard": {
					"title": "보물상자",
					"description": "보물상자 안에는 뭐가 있을까",
					"thumbnail": {
						"imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
					},
					"profile": {
						"imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
						"nickname": "보물상자"
					},
					"forwardable": True
					}
				}
			]
		}
	}
	sb = SkillResponseBuilder()
	thumb = Thumbnail('http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg')
	profile = Profile('보물상자', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM')
	card = BasicCard(thumb, '보물상자', '보물상자 안에는 뭐가 있을까', profile=profile)
	card.set_forwardable(True)
	sb.append(card)
	assert(trueDict == sb.to_dict())