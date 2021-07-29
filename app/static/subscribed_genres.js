const tableParams = {
    id: 'subscribed_genres-table',
    className: 'admin-table',
    columnNames: ['subscribed_id', 'user_id', 'genre_id'],
    route: '/subscribed_genres/'
}

const formParams = {
    title:'Subscribed Genre',
    id:'subscribed_id',
    route: '/subscribed_genres/',
    inputs: [{attr:{
                    type:'number', name:'user_id', value: 1, required:'required'
                   }
             },
             {attr:{
                    type:'number', name:'genre_id', value: 1, required:'required'
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