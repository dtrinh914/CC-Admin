const tableParams = {
    id: 'users-table',
    className: 'admin-table',
    columnNames: ['user_id', 'date_created', 'username', 'password'],
    title: 'Users',
    route: '/users/',
    filter: {by:'username', filterValue:''}
}

const formParams = {
    id:'user_id',
    title: 'User',
    route: '/users/',
    inputs: [{attr: {type:'text', name:'username', value: '', required:'required'}}, 
             {attr: {type:'text', name:'password', value: '', required:'required'}},
             {attr: {type:'submit', value:'Add', class: 'btn-outline'}}
            ]
}

const tableRoot = document.querySelector('#table-root');
const formRoot = document.querySelector('#form-root');
createDBTable(tableRoot, tableParams, formRoot, formParams);