{
    'name':   'User Rights for Cancel Journal Entries',
    'author': 'itech resources',
    'company': 'Itech Resources',
    'depends': [
                'base',
                'account',
                'sale',
                'purchase',
                ],
    
    'data': [
        'views/cancel.xml',
        'security/cancel_rights.xml'
        ,
       
    ],
    
    'application': True,
    'price':'15.0',
    'currency': 'EUR',
}
