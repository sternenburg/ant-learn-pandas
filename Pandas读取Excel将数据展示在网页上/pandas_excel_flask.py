from flask import Flask
import pandas as pd
import os

working_dir = r'c:\Users\Lei\Documents\GitHub\ant-learn-pandas\Pandas读取Excel将数据展示在网页上'
os.chdir(working_dir)

app = Flask(__name__)

@app.route('/')
def show_excel():
    df = pd.read_excel("./学生信息表.xlsx")
    table_html = df.to_html()
    return f"""
        <html>
            <body>
                <h1>学生信息表</h1>
                <div>{table_html}</div>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0")

#在浏览器中打开 127.0.0.1:5000/

