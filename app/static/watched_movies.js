const tableParams = {
    id: 'watched_movies-table',
    className: 'admin-table',
    columnNames: ['watched_id', 'date_created', 'movie_title', 'username'],
    route: '/watched_movies/'
}

const formParams = {
    title:'Watched Movie',
    id:'watched_id',
    route: '/watched_movies/',
    inputs: [{attr:{
                    type:'number', name:'movie_id', value: 1, required:'required'
                   }
             }, 
             {attr:{
                    type:'number', name:'user_id', value: 1, required:'required'
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