# 어려웠던 일들

## 모델 설정

모델을 만들었는데 TMDB에서 제공하는 JSON이랑 달라서 loaddata할 수 없었다

그리하여 적절히 모델을 수정하고, 또 TMDB의 JSON을 일부 편집하였으며, Genre도 따로 JSON으로 받아서 DB로 로드하여 처리하였다.

## 시리얼라이저와 다대다

시리얼라이저를 사용하려니 다대다 관계를 처리하는 방법을 몰라 어려웠다.

다대다를 처리하기 위해 우선 장르를 먼저 시리얼라이즈하고 이후 그 시리얼라이즈된 데이터를 genre_ids에 덮어씌워서 Movie를 시리어라이즈하자 해결되었다.


## axios를 로컬끼리 통신하려니 cors에러가 난다

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

CORS_ALLOW_ALL_ORIGINS = True

```