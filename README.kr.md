# Data Extract-Load-Transform

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

데이터레이크에 있는 값을 파싱해서 메모리에 올려둔 다음, 데이터 레이블러가 실행될 수 있도록 한다. 레이블링이 완료된 데이터를 feature store 로 집어넣는 일을 한다. autosink-data-elt 에는 데이터레이크에 저장되는 형식인 json 파일을 잘 읽고 쓰기 위한 유틸 클래스들, 데이터타입이 정의되어 있다. 라즈베리파이에서 Extract 된 데이터가 데이터레이크에 저장되었다고 할 때, 데이터를 Load 하고 레이블링하여 Transform 된 형태로 feature store 에 저장하기 때문에 ELT라고 이름을 붙였다.

## 기능

- [ ] 데이터레이크에 있는 값을 파싱해서 메모리에 올려둔 다음, 데이터 레이블러가 읽어가기 편한 형태로 정리한다.
- [ ] 레이블러를 호출한다.
- [ ] 레이블링이 완료된 데이터를 feature store 로 집어넣는 일을 한다.

# 환경

환경은 MacOS, Linux 를 기준으로 합니다.

## `Makefile`

`Makefile`은 다음과 같은 기능들을 가지고 있습니다.

### `make lint`

- `.vscode` 설정을 사용하려면 `pylint` 익스텐션을 설치하세요.
- 린터의 기본 세팅에 `pyproject.toml` 파일에 명시된 옵션을 오버라이딩해 코드를 린팅합니다.

### `make format`

- 포매터는 google의 `yapf`를 사용합니다.
- `yapf` 포매터의 기본 세팅에 `pyproject.toml` 파일에 명시된 옵션을 오버라이딩해 코드를 포매팅합니다.
- `.vscode` 설정을 사용하려면 `yapf` 익스텐션을 설치하세요.

### `make test`

- 테스트는 `unittest`를 사용합니다.
- `test_*.py` 와 `*_test.py` 패턴을 모두 지원합니다.
- 테스트 파일이 존재하는 위치까지 `__init__.py` 로 연결되어 있어야 합니다.

### `make publish`

- `~/.pypirc` 파일을 아래와 같이 작성하세요.
    ```
    [pypi]
    username = __token__
    password = pypi-어쩌고저쩌고 # 개인 API 토큰을 발급받아 작성하세요.
    ```
- 이 명령을 실행하면 `flit` 을 사용하여 PyPI 공개 레지스트리에 패키지를 푸시합니다.
- 앞서 이름으로 지정한 `myproject`(가명)이 업로드되어, 전세계 누구나 `python3 -m pip install myproject`로 패키지를 설치해 사용할 수 있게 됩니다.
