const tableParams = {
    id: 'subscribed_genres-table',
    className: 'admin-table',
    columnNames: ['subscribed_id', 'username', 'genre_name'],
    title: 'Subscribed Genres',
    route: '/subscribed_genres/'
}

const formParams = {
    title:'Subscribed Genre',
    id:'subscribed_id',
    route: '/subscribed_genres/',
    inputs: [{attr:{
                    type:'select', name:'user_id', value: 1, required:'required', label: 'username'
                   },
              route: '/users',
              id: 'user_id',
              fieldname: 'username'
             },
             {attr:{
                    type:'select', name:'genre_id', value: 1, required:'required', label: 'genre_name'
                   },
              route: '/genres',
              id: 'genre_id',
              fieldname: 'genre_name'
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