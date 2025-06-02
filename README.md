# js_rpc_mapper

指定フォルダ以下の全JSファイルから、指定されたrpc_nameが使われているファイルとそのクラス名をマッピングし、CSVで出力するツールです。

## 機能
- 指定フォルダ以下のJSファイルを再帰的に探索
- 入力CSVからrpc_name, rpc_classを取得
- JSファイル内でrpc_nameの利用有無を判定（変数経由やimport経由も対応）
- JSファイル内のクラス名抽出
- マッピング結果をCSV出力

## インストール方法
1. Python 3.7以降が必要です。
2. 必要なパッケージをインストールします。

```sh
pip install -r requirements.txt
```

## 入力ファイル（CSV）
- 1行目はヘッダー（rpc_name, rpc_class）
- 例：

```
rpc_name,rpc_class
getUser,UserService
updateUser,UserService
```

## 使い方
main.pyのmain関数を呼び出して実行します。

```python
from main import main
main('jsフォルダのパス', '入力CSVファイルのパス', '出力CSVファイルのパス')
```

例：
```python
from main import main
main('sample_js', 'input.csv', 'output.csv')
```

### コマンドラインから実行する場合

```sh
python main.py jsフォルダのパス 入力CSVファイルのパス 出力CSVファイルのパス
```

例：
```sh
python main.py sample_js input.csv output.csv
```

## 出力ファイル（CSV）
- 2カラム（rpc_name, js_class）
- 例：
```
rpc_name,js_class
getUser,UserClass
updateUser,UserClass
```

## 注意事項・既知の制限
- JSファイル内のクラス宣言のみ抽出します（関数やオブジェクトは対象外）
- rpc_nameの判定は簡易的な文字列一致・変数代入のみ対応
- 大規模なJSコードや特殊な構文には未対応の場合があります

## ライセンス
MIT License

## 作者
- 作成者: あなたの名前
- お問い合わせ: your.email@example.com
