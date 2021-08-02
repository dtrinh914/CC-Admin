const tableParams = {
    id: 'movies-table',
    className: 'admin-table',
    columnNames: ['movie_id', 'title', 'avg_review_score'],
    title: 'Movies',
    route: '/movies/'
}

const formParams = {
    title:'Movie',
    id:'movie_id',
    route: '/movies/',
    inputs: [{attr:{
                    type:'text', name:'title', value: '', required:'required'
                   }
             }, 
             {attr:{
                    type:'number', name:'avg_review_score', value: '', 
                    step:0.1, min:0.0, max:10.0, required:'required'
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