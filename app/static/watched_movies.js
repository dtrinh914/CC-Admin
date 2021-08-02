const tableParams = {
    id: 'watched_movies-table',
    className: 'admin-table',
    columnNames: ['watched_id', 'date_created', 'movie_title', 'username'],
    title: 'Watched Movies',
    route: '/watched_movies/'
}

const formParams = {
    title:'Watched Movie',
    id:'watched_id',
    route: '/watched_movies/',
    inputs: [{attr:{
                    type:'select', name:'movie_id', value: 1, required:'required', label:'movie_title'
                   },
              route:'/movies',
              id: 'movie_id',
              fieldname:'title'
             }, 
             {attr:{
                    type:'select', name:'user_id', value: 1, required:'required', label: 'username'
                   },
              route:'/users',
              id: 'user_id',
              fieldname:'username'
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