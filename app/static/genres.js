const tableParams = {
    id: 'genres-table',
    className: 'admin-table',
    columnNames: ['genre_id', 'genre_name'],
    route: '/genres/'
}

const formParams = {
    title:'Genre',
    id:'genre_id',
    route: '/genres/',
    inputs: [{attr:{
                    type:'text', name:'genre_name', value: '', required:'required'
                   }
             },
             {attr:{
                    type:'submit', value:'Add', class: 'btn-outline'
                   }
             }
            ]
}

const tableRoot = document.querySelector('#table-root');
const formRoot = document.querySelector('#form-root');
createDBTable(tableRoot, tableParams, formRoot, formParams);