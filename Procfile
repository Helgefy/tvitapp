web: gunicorn tvitapp.wsgi --log-file -
worker: celery -A tvitapp worker -events -l info 
beat: celery -A tvitapp beat 