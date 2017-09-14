web: gunicorn tvitapp.wsgi --log-file -
worker: celery -A tvitapp worker -events -loglevel info 
beat: celery -A tvitapp beat 