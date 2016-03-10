CONFIG = {                                                                      
    'mode': 'wsgi',                                                           
    'working_dir': '/home/box/web',                                           
    'python': '/usr/bin/python',                                              
    'args': (                                                                   
        '--bind=127.0.0.1:8000',                                              
        '--workers=16',                                                         
        '--timeout=60',                                                         
        'app.module',                                                           
    ),                                                                          
} 
