import os
import csv
from main import main

def setup_test_env():
    os.makedirs('test_js', exist_ok=True)
    with open('test_js/test1.js', 'w', encoding='utf-8') as f:
        f.write('class TestClass1 { constructor() { this.rpc = "test_ri"; } }')
    with open('test_js/test2.js', 'w', encoding='utf-8') as f:
        f.write('const rpcName = "test_ri"; class TestClass2 {}')
    with open('input.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['rpc_name', 'rpc_class'])
        writer.writerow(['test_ri', 'TestClass1'])
        writer.writerow(['test_ri', 'TestClass2'])

def test_main():
    setup_test_env()
    main('test_js', 'input.csv', 'output.csv')
    with open('output.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        assert any(row['rpc_name'] == 'test_ri' and row['js_class'] == 'TestClass1' for row in rows)
        assert any(row['rpc_name'] == 'test_ri' and row['js_class'] == 'TestClass2' for row in rows)
    print('テスト成功')

if __name__ == '__main__':
    test_main()
