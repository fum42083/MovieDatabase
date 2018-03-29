import signal
import sys
import subprocess

p1=None
p2=None

def signal_handler(signal, frame):
	print("\n---Stopping services---")
	p2.terminate()
	print("uwsgi django upstream stopped")
	p1.terminate()
	print("celery worker (=multithread service) stopped")
	subprocess.call('service rabbitmq-server stop', shell=True)
	print("rabbitmq-server (=Messagequeue) stopped")
	subprocess.call('/etc/init.d/nginx stop', shell=True)
	print("Nginx (=Webserver) stopped")

	sys.exit(0)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	print("--Starting services---\n")
	subprocess.call('service rabbitmq-server restart', shell=True)
	print("rabbitmq-server (=Messagequeue) started")
	subprocess.call('/etc/init.d/nginx restart', shell=True)
	print("Nginx (=Webserver) started")
	p1 = subprocess.Popen('cd MovieDatabase && ../bin/celery worker --app MovieDatabase --loglevel=INFO', shell=True)
	print("celery worker (=multithread service) started")
	p2 = subprocess.Popen('bin/uwsgi --chdir /root/uwsgi-tutorial/MovieDatabase --socket MovieDatabase.sock --module MovieDatabase.wsgi --chmod-socket=666', shell=True)
	print("uwsgi django upstream started")
	print("Website can be visited now via '127.0.0.1:8000/searchmovie'")
	print("Press CTRL + C to stop Services")
	signal.pause()	



