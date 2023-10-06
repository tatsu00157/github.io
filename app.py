from flask import Flask, render_template

app = Flask(__name__)

# サンプルのポートフォリオデータ
portfolio = [
    {
        'title': 'プロジェクト1',
        'description': 'これはプロジェクト1の詳細です。',
        'url': 'https://example.com/project1',
        'image': 'project1.jpg',
    },
    {
        'title': 'プロジェクト2',
        'description': 'これはプロジェクト2の詳細です。',
         'url': 'https://example.com/project2',
        'image': 'project2.jpg',
    },
    {
        'title': 'プロジェクト3',
        'description': 'これはプロジェクト3の詳細です。',
         'url': 'https://example.com/project3',
        'image': 'project3.jpg',
    },
    # {
    #     'title': 'プロジェクト4',
    #     'description': 'これはプロジェクト4の詳細です。',
    #      'url': 'https://example.com/project3',
    #     'image': 'project3.jpg',
    # },
    # {
    #     'title': 'プロジェクト5',
    #     'description': 'これはプロジェクト5の詳細です。',
    #      'url': 'https://example.com/project3',
    #     'image': 'project3.jpg',
    # },
    # {
    #     'title': 'プロジェクト6',
    #     'description': 'これはプロジェクト6の詳細です。',
    #      'url': 'https://example.com/project3',
    #     'image': 'project3.jpg',
    # },
    # {
    #     'title': 'プロジェクト7',
    #     'description': 'これはプロジェクト7の詳細です。',
    #      'url': 'https://example.com/project3',
    #     'image': 'project3.jpg',
    # },
    # {
    #     'title': 'プロジェクト8',
    #     'description': 'これはプロジェクト8の詳細です。',
    #      'url': 'https://example.com/project3',
    #     'image': 'project3.jpg',
    # },
    # {
    #     'title': 'プロジェクト9',
    #     'description': 'これはプロジェクト9の詳細です。',
    #      'url': 'https://example.com/project3',
    #     'image': 'project3.jpg',
    # }
]

@app.route('/')
@app.route('/portfolio')
def view_portfolio():
    return render_template('portfolio.html', portfolio=portfolio)

if __name__ == '__main__':
    app.run()
