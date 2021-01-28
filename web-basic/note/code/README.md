# Python 코드

## 가상환경 만들기 (최초 한 번만)

`pipenv --python 3.8`

## 가상환경으로 들어가기

`pipenv shell`

## linter 설치

**linter은 작성한 코드에 에러가 생길 부분을 미리 감지한다.**

`shift + command + p` --> python : select linter --> flake8 선택&설치

해당 폴더에 .vscode 폴더가 생성된 것을 확인할 수 있다.

## formatter 설치

`pipenv install black --dev --pre`

## 파이선 파일 실행

`pipenv run python myPythonFile.py`

## 라이브러리 설치

`pipenv install <패키지이름>`
