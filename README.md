# js_rpc_mapper

指定フォルダ以下の全JSファイルから、指定されたrpc_nameが使われているファイルとそのクラス名をマッピングし、CSVで出力するツールです。

## 機能
- 指定フォルダ以下のJSファイルを再帰的に探索
- 入力CSVからrpc_name, rpc_classを取得
- JSファイル内でrpc_nameの利用有無を判定（変数経由やimport経由も対応）
- JSファイル内のクラス名抽出
- マッピング結果をCSV出力

## 使い方
1. requirements.txtで依存パッケージをインストール
2. main.pyを実行
3. 入力CSVとJSフォルダパスを指定

## 出力
- rpc_name, js_classの2カラムを持つCSV
