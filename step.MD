# TODOアプリ学習ロードマップ

## 最終目標
FastAPI + SQLModel + Docker を使った本格的なWebAPIの構築


## Lv1：TODOアプリを整える ✅ 完了

### やること
- [] 変数名・スペースを整える（`conn =sqlite3` → `conn = sqlite3`）
- [] `id`という変数名を`todo_id`に変える（予約語と被るため）
- [ ] `while True`でメニューをループさせる
- [ ] `"0"`で終了できるようにする
- [ ] `try/except`でエラーハンドリングを追加する

---

## Lv2：カラムを追加する ✅ 完了

### やること
- [ ] `database.db`を削除してテーブルを作り直す
- [ ] `status`（pending / in_progress / done）を追加する
- [ ] `priority`（low / mid / high）を追加する
- [ ] `due_date`（YYYY-MM-DD形式）を追加する
- [ ] INSERT文を更新して新しいカラムも保存する


## Lv3：ファイルを分割する 🔥 現在地

### やること
- [x] `database.py`にDB接続をまとめる
- [x] `models.py`にSQL操作をまとめる
- [x] インスタンス化を`main.py`でやる
- [x] `input()`を`main.py`に移動する
- [ ] `models.py`内の余分な`db_admin = dbManager()`を削除する
- [ ] `db_admin`をSQLクラスに引数で渡す構造にする
- [ ] インデントを統一する（スペース4つ）
- [ ] エラーハンドリングを追加する

### 完成イメージ
```
main.py    → メニュー表示・input・関数の呼び出し
models.py  → SQL操作の関数をまとめたクラス
database.py → DB接続・テーブル作成
```


## Lv4：カテゴリを追加する

### やること
- [ ] `categories`テーブルを作る
- [ ] `todos`テーブルに`category_id`を追加する
- [ ] カテゴリ一覧・追加をメニューに追加する
- [ ] TODOをカテゴリで絞り込む機能を追加する
- [ ] JOINを使ってカテゴリ名も一緒に表示する

### テーブル構成
```
categories
├── id
└── name

todos
├── id
├── text
├── status
├── priority
├── due_date
└── category_id → categories.id
```

---

## Lv5：FastAPIでWebAPI化

### やること
- [ ] `pip install fastapi uvicorn`をインストールする
- [ ] `routers/`フォルダを作る
- [ ] `main.py`をFastAPI化する（while Trueは削除）
- [ ] `routers/todos.py`にエンドポイントを作る（GET・POST・PATCH・DELETE）
- [ ] `routers/categories.py`にエンドポイントを作る
- [ ] `http://localhost:8000/docs`でSwaggerUIを確認する

### フォルダ構成
```
todo-app/
├── main.py
├── database.py
├── models.py
└── routers/
    ├── __init__.py
    ├── todos.py
    └── categories.py
```

---

## Lv6：Gatewayパターン導入

### やること
- [ ] `db/gateways/`フォルダを作る
- [ ] `TodoGW`クラスを作ってSQL操作を移動する
- [ ] `CategoryGW`クラスを作る
- [ ] RouterからはGWを呼び出すだけにする
- [ ] RouterにSQL文が残っていないか確認する

### フォルダ構成
```
todo-app/
├── main.py
├── db/
│   ├── database.py
│   ├── models.py
│   └── gateways/
│       ├── __init__.py
│       ├── category_gw.py
│       └── todo_gw.py
└── routers/
    ├── __init__.py
    ├── todos.py
    └── categories.py
```

---

## Lv7＋8：SQLModel導入 ＆ サブタスク追加

### やること
- [ ] `pip install sqlmodel`をインストールする
- [ ] `models.py`をSQLModelで書き直す
- [ ] IDをUUIDに変更する
- [ ] `TodoStatus`・`TodoPriority`をEnumで定義する
- [ ] `TableBase`（created_at・updated_at）を作る
- [ ] `Subtask`テーブルを追加する（TodoとRlationship）
- [ ] `is_deleted`を追加して論理削除にする
- [ ] GatewayをSQLModelのSessionで書き直す
- [ ] SubtaskGWを作る

### テーブル構成
```
categories
├── id（UUID）
├── name
├── is_deleted
├── created_at
└── updated_at

todos
├── id（UUID）
├── title
├── status（Enum: pending/in_progress/done/expired）
├── priority（Enum: low/mid/high）
├── due_date
├── category_id → categories.id
├── is_deleted
├── created_at
└── updated_at

subtasks
├── id（UUID）
├── todo_id → todos.id
├── title
├── is_done
├── created_at
└── updated_at
```

---

## Lv9：Docker化

### やること
- [ ] `requirements.txt`を作る（`pip freeze > requirements.txt`）
- [ ] `Dockerfile`を作る
- [ ] `compose.yaml`を作る
- [ ] `docker compose up --build`で起動確認する
- [ ] `http://localhost:8000/docs`でSwaggerUIを確認する

---

## Lv10：ユースケース層を追加する（最終目標）

### やること
- [ ] `use_cases/`フォルダを作る
- [ ] `TodoUseCase`を作る（カテゴリ存在確認・todo_number採番）
- [ ] `CategoryUseCase`を作る
- [ ] `SubtaskUseCase`を作る
- [ ] `commit()`をuse_caseに移動する
- [ ] Routerにビジネスロジックが残っていないか確認する

### 最終フォルダ構成
```
todo-app/
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── main.py
├── db/
│   ├── database.py
│   ├── models.py
│   └── gateways/
│       ├── category_gw.py
│       ├── todo_gw.py
│       └── subtask_gw.py
├── use_cases/
│   ├── category_use_case.py
│   ├── todo_use_case.py
│   └── subtask_use_case.py
└── routers/
    ├── categories.py
    ├── todos.py
    └── subtasks.py
```

### 各レイヤーの役割
```
routers/     → HTTPの入出力だけ
use_cases/   → ビジネスロジック・トランザクション管理
gateways/    → DB操作（flushまで）
models.py    → テーブル定義・スキーマ定義
database.py  → 接続・セッション管理
```

---

## その先（中級以上）

| スキル | 内容 |
|-------|------|
| pytest | テストを書く |
| JWT認証 | ログイン機能を追加する |
| PostgreSQL | 本番DBに移行する |
| GitHub Actions | CI/CDを構築する |
| Alembic | DBマイグレーションを管理する |

---

## 現在のレベル評価

| スキル | レベル |
|-------|-------|
| Python | ⭐⭐⭐☆☆ |
| SQL・DB設計 | ⭐⭐⭐☆☆ |
| FastAPI | 未着手 |
| クリーンアーキテクチャ | ⭐⭐☆☆☆ |
| Docker | 未着手 |