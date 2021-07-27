const tableParams = {
    id: 'users-table',
    className: 'admin-table',
    columnNames: ['user_id', 'date_created', 'username', 'password'],
    route: '/users/'
}

const formParams = {
    id:'user_id',
    route: '/users/',
    inputs: [{type:'text', name:'username', value: ''}, 
             {type:'text', name:'password', value: ''},
             {type:'submit', value:'Add'}
            ]
}

const tableRoot = document.querySelector('#table-root');
const formRoot = document.querySelector('#form-root');
createDBTable(tableRoot, tableParams, formRoot, formParams);