from flask import Flask, render_template, request
from pymongo import MongoClient
from pprint import pprint
import pprintjson


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/signin', methods=['POST'])
def signin():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    _username = request.form.get('username')  # get(attr) returns None if attr is not present
    _password = request.form.get('password')

    # Validate and send response
    if _username == 'kani' and _password == 'Terence04':
        return render_template('signin.html', username=_username)
    else:
        return render_template('notauthorized.html')  # 400 Bad Request


@app.route('/search', methods=['POST'])
def search():
    if request.form['search_button'] == 'Search':
        return render_template('search.html')
    else:
        pass


@app.route('/insert', methods=['POST'])
def insert():
    if request.form['insert_button'] == 'Insert':
        return render_template('insert.html')
    else:
        pass


@app.route('/update', methods=['POST'])
def update():
    if request.form['update_button'] == 'Update':
        return render_template('update.html')
    else:
        pass


@app.route('/delete', methods=['POST'])
def delete():
    if request.form['delete_button'] == 'Delete':
        return render_template('delete.html')
    else:
        pass


@app.route('/searching', methods=['POST'])
def searching():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('searchkey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('searchvalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant
    d = {}
    dlist = []
    mydocs = db.docs.find({mykey1:myvalue1})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("searchoutput.html",mydocs=dlist)


@app.route('/inserting', methods=['POST'])
def inserting():
    # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('insertkey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('insertvalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant
    mydict = {mykey1: myvalue1}
    x = db.docs.insert_one(mydict)

    d = {}
    dlist = []
    mydocs = db.docs.find({mykey1:myvalue1})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("insertoutput.html",mydocs=dlist)

@app.route('/updating', methods=['POST'])
def updating():
        # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('updatekey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('updatevalue')
    mychangekey = request.form.get('newkey')
    mychangevalue = request.form.get('newvalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant
    myquery = {mykey1: myvalue1}
    newvalues = {"$set": {mychangekey: mychangevalue}}

    db.docs.update_many(myquery, newvalues)

    d = {}
    dlist = []
    mydocs = db.docs.find({mychangekey: mychangevalue})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("updateoutput.html", mydocs=dlist)

@app.route('/deleting', methods=['POST'])
def deleting():
        # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
    mykey1 = request.form.get('deletekey')  # get(attr) returns None if attr is not present
    myvalue1 = request.form.get('deletevalue')

    client = MongoClient("mongodb+srv://kani:Terence04@clustermongodb-xwcjz.gcp.mongodb.net/test?retryWrites=true")
    print(client)
    db = client.restaurant

    myquery = {mykey1: myvalue1}
    db.docs.delete_one(myquery)

    d = {}
    dlist = []
    mydocs = db.docs.find({mykey1: myvalue1})
    for x in mydocs:
        print(x)
        d['data'] = x
        dlist.append(d.copy())
    print(dlist)

    if request.method == 'POST':
        return render_template("deleteoutput.html", mydocs=dlist)

if __name__ == '__main__':
    app.run(debug=True)
