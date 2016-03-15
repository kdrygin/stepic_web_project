CONFIG = {
    'mode': 'wsgi',
    #'working_dir': '/home/box/web',
    'working_dir': '/home/box/web/ask',
    # 'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8000',
        # ver 1'--bind=127.0.0.1:8080',
        #'--bind=127.0.0.1:8000',
        '--daemon',
        '--workers=2',
        '--timeout=60',
        # ver 1 'hello:app',
        'ask.wsgi:application',
    ),
}
