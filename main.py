import os
import csv
import re
from pathlib import Path
import esprima

# 入力CSVのパース
def parse_input_csv(csv_path):
    rpc_list = []
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rpc_list.append({'rpc_name': row['rpc_name'], 'rpc_class': row['rpc_class']})
    return rpc_list

# 指定ディレクトリ以下の全JSファイルを再帰的に取得
def find_js_files(target_dir):
    js_files = []
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith('.js'):
                js_files.append(os.path.join(root, file))
    return js_files

# JSファイルからクラス名を抽出
def extract_js_classes(js_code):
    classes = []
    try:
        tree = esprima.parseScript(js_code, tolerant=True)
        for node in tree.body:
            if node.type == 'ClassDeclaration':
                classes.append(node.id.name)
    except Exception as e:
        pass
    return classes

# JSファイル内でrpc_nameが使われているか判定（変数経由も考慮）
def search_rpc_usage(js_code, rpc_name):
    # 直接記述
    if rpc_name in js_code:
        return True
    # 変数経由（簡易: const/let/var 変数 = 'rpc_name'）
    pattern = re.compile(r"(const|let|var)\\s+(\\w+)\\s*=\\s*['\"]" + re.escape(rpc_name) + r"['\"]")
    if pattern.search(js_code):
        return True
    return False

# メイン処理
def main(js_dir, input_csv, output_csv):
    rpc_list = parse_input_csv(input_csv)
    js_files = find_js_files(js_dir)
    result = []
    for rpc in rpc_list:
        for js_file in js_files:
            with open(js_file, encoding='utf-8') as f:
                js_code = f.read()
            if search_rpc_usage(js_code, rpc['rpc_name']):
                classes = extract_js_classes(js_code)
                for cls in classes:
                    result.append({'rpc_name': rpc['rpc_name'], 'js_class': cls})
    # CSV出力
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['rpc_name', 'js_class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in result:
            writer.writerow(row)

if __name__ == '__main__':
    # 例: main('js_folder', 'input.csv', 'output.csv')
    pass
