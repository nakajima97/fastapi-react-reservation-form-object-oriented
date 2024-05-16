# fastapi-react-reservation-form
## Clone後に実行するコマンド
`docker compose build`  
`docker compose run --entrypoint "poetry install --no-root" api`  
`docker compose run --entrypoint "yarn install" front`  
`docker compose run --entrypoint "yarn install" management-app`  
`docker compose up`  

マイグレーションの実行  
`docker compose exec api poetry run python -m source.migrate_db`  

# テストコードの実行
## api
`docker compose run --entrypoint "poetry run pytest" api`

# ディレクトリについて
```
.
├── api               API（予約フォーム・予約管理アプリで共通）
├── documents         このプロジェクトのドキュメント
├── front             予約フォーム
├── management-app    予約管理アプリ
└── mysql             APIで利用するDB
```
各ディレクトリ内の構造に関して各ディレクトリ内のREADMEを参照