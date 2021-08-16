# AutoHCS_Web
간편하게 URL 파라미터 형식으로 요청하여 자가진단 설문을 완료할 수 있습니다.

# 2021.08.16 수정
selfcheck 부분에서 학교명을 입력하는데 학교를 검색하고 검색된 학교중 최상단에 있는 학교를 골라서 자가진단을 진행하다보니
일부 학생들은 같은 지역에 같은(비슷한) 이름으로 학교가 2개가 검색되었으나 최상단의 결과가 선택되어서 자가진단에 참여할 수 없는 경우가 있었습니다.
기존 hcs.py 파일 내부의 schoolcode = school_infos["schulList"][0]["orgCode"] 부분에서 index가 0으로 고정되어있던 [0] 부분을 파라미터로 받을 수 있도록 수정하였습니다.
selfcheck(name: str, birth: str, area: str, schoolname: str, level: str, password: str, schoolnum: int = None, customloginname: str = None) 을 사용하면 될 것 같습니다.


### 📚 라이브러리 및 라이센스
GPL v3 [hcskr](https://github.com/331leo/hcskr_python) 라이브러리가 사용되었습니다.

### 📄 사용전
```
이 소스코드는 Apache 를 통해 구동됩니다.
httpd.conf 에서
<Files "*.py">
      Options ExecCGI
      AddHandler cgi-script .py
</Files>
을 디렉토리 최상단에 추가하여 사용할 수 있습니다.
```

### ⚙️ 사용방법
```txt
URL 의 파라미터를 이용하여 자가진단 설문에 참여할 수 있습니다.
http(s)://xxx.xxx/check.py?name=이름&birth=생년월일&region=지역&level=학교급&school=학교명&password=비밀번호(&index=int)
다음 URL을 요청하여 간단하게 완료할 수 있습니다.
index 부분은 넣지 않으면 기본값 0으로 요청됩니다. (정수 타입)
```
