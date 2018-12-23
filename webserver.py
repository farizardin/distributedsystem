from flask import Flask, render_template, request, redirect
from zatt.client import DistributedDict

app = Flask('__name__')

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        try:
            data = request.form['inputan']
            d = DistributedDict('127.0.0.1',8658)
            d['key'] = data
            x = d['key']
            return render_template('index.html', nilai = x, aksi = "disetor ke", alamat = "127.0.0.1:8658")
        except:
            try:
                data = request.form['inputan']
                d = DistributedDict('127.0.0.1',8659)
                d['key'] = data
                x = d['key']
                return render_template('index.html', nilai = x, aksi = "disetor ke", alamat = "127.0.0.1:8659")
            except:
                try:
                    data = request.form['inputan']
                    d = DistributedDict('127.0.0.1',8660)
                    d['key'] = data
                    x = d['key']
                    return render_template('index.html', nilai = x, aksi = "disetor ke", alamat = "127.0.0.1:8660")
                except:
                    return render_template('errorhandle.html')

@app.route('/getdata', methods = ['GET','POST'])
def get():
    srv1 = 8658
    srv2 = 8659
    srv3 = 8660
    a1 = "Data dari"
    a2 = "adalah"
    if request.method == "GET":
        return render_template('1.html', server1 = srv1, server2 = srv2, server3 = srv3)
    elif request.method == "POST":
        select = request.form.get('field_id')
        if select == "8658":
            ipserver = "127.0.0.1:8658"
            d = DistributedDict('127.0.0.1',8658)
            nilai = d['key']
            return render_template('1.html',serverip = ipserver, server1 = srv1, server2 = srv2, server3 = srv3, test = nilai, act1 = a1, act2 = a2)
        elif select == "8659":
            ipserver = "127.0.0.1:8659"
            d = DistributedDict('127.0.0.1',8659)
            nilai = d['key']
            return render_template('1.html',serverip = ipserver, server1 = srv1, server2 = srv2, server3 = srv3, test = nilai,act1 = a1, act2 = a2)
        elif select == "8660":
            ipserver = "127.0.0.1:8660"
            d = DistributedDict('127.0.0.1',8660)
            nilai = d['key']
            return render_template('1.html',serverip = ipserver, server1 = srv1, server2 = srv2, server3 = srv3, test = nilai,act1 = a1, act2 = a2)
if __name__ == "__main__":
    app.run(debug=True)