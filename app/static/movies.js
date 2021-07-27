const tableParams = {
    id: 'movies-table',
    className: 'admin-table',
    columnNames: ['movie_id', 'title', 'avg_review_score'],
    route: '/movies/'
}

const formParams = {
    id:'movie_id',
    route: '/movies/',
    inputs: [{type:'text', name:'title', value: ''}, 
             {type:'number', name:'avg_review_score', value: ''},
             {type:'submit', value:'Add'}
            ]
}

const tableRoot = document.querySelector('#table-root');
const formRoot = document.querySelector('#form-root');
createDBTable(tableRoot, tableParams, formRoot, formParams);