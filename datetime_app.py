from flask import Flask, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def show_datetime():
    now = datetime.now()
    timezone = os.getenv('TZ', 'UTC')
    
    return render_template('datetime.html',
                         current_time=now.strftime("%H:%M:%S"),
                         current_date=now.strftime("%Y-%m-%d"),
                         timezone=timezone)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))