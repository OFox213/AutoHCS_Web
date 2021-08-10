# AutoHCS_Web
간편하게 URL 파라미터 형식으로 요청하여 자가진단 설문을 완료할 수 있습니다.

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
http(s)://xxx.xxx/check.py?name=이름&birth=생년월일&region=지역&level=학교급&school=학교명&password=비밀번호
다음 URL을 요청하여 간단하게 완료할 수 있습니다.
```
