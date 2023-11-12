from flask import Flask, request, render_template
from stories import story


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', story=story.prompts)

@app.route('/story')
def get_story():
    # print(f'results:{request.args}')
    story_string = story.generate(request.args)
    return render_template('story.html', story_string = story_string)

if __name__ == "__main__":
    app.run(debug=True)