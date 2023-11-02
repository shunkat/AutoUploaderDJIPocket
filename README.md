# 最初に
これは、dji pocket2で撮影した動画を、編集せずに繋げてyoutubeにアップロードするためのプログラムです。
他のカメラでも使えるかもしれませんが、動作確認はしていません。
またmacでしか動作確認していません、windowsで使いたい場合は適宜pathの変更をしてください。

# 事前準備
pythonのバージョンは3.12.0です。


インストール済みのライブラリは以下です。
```
cachetools               5.3.2
certifi                  2023.7.22
charset-normalizer       3.3.2
google-api-core          2.12.0
google-api-python-client 2.106.0
google-auth              2.23.4
google-auth-httplib2     0.1.1
googleapis-common-protos 1.61.0
httplib2                 0.22.0
idna                     3.4
oauth2client             4.1.3
pip                      23.3.1
protobuf                 4.24.4
pyasn1                   0.5.0
pyasn1-modules           0.3.0
pyparsing                3.1.1
requests                 2.31.0
rsa                      4.9
six                      1.16.0
uritemplate              4.1.1
urllib3                  2.0.7
```

GCPのプロジェクトを作成して、Youtube API V3を有効にしてください。（もし認証画面を作成していなければ作成もしてください。）

その後、認証情報をダウンロードして、client_secret.jsonという名前でこのプロジェクトのルートディレクトリに配置してください。

# 使い方
1. dji pocket2から取り出したsdカードをPCに接続してください。
2. ```python integrate.py "アップロードした動画のタイトル"```を実行してください。
3. 初回はgoogleからの警告が出てきますが、承認してあげればそれ以降は承認しなくて大丈夫です。
4. もし、アップロードする動画のその他の情報を変更したければupload.pyの118行目あたりを変更してください。