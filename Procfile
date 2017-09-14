web: gunicorn tvitapp.wsgi --log-file -
orker: celery -A tvitapp worker -events -loglevel info 
beat: celery -A tvitapp beat 