# simplified_atm

簡易的なATMを作成

機能
- 口座開設
- 入金
- 出金

## 起動方法
※ docker環境が立ち上がることが前提となっております

1. コンテナイメージをビルドし、起動まで行う。
```
make up_container
```

2. フロント画面をビルドしてサーバーで読み込めるようにする
```
make build_front
```

3. サーバーの起動を行う
```
make up_server
```

4. ブラウザで`localhost:5000`へアクセス


## 停止方法
```
make down
```