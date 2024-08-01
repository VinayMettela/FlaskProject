from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {'id':1, 'title':'Data Analyst', 'location':'Bengaluru, India' , 'salary':'Rs. 10,00,000'},
  {'id':2, 'title':'Data Scientist', 'location':'Delhi, India' , 'salary': 'Rs. 15,00,000'},
{'id':3, 'title':'Frontend Engineer', 'location':'Remote'},
{'id':4, 'title':'Backend Engineer', 'location': 'San Francisco, USA' , 'salary': '120,0000'}
]

@app.route("/")
def hello_world():
  return render_template('Home.html',jobs=JOBS,Company_name='Cool')

@app.route("/api/Jobs")
def Jobs_lst():
  return jsonify(JOBS)

print(__name__)

if __name__ == "__main__":
  # print("i am inside the if")
  app.run(host="0.0.0.0", debug=True)
