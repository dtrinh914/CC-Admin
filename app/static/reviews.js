const tableParams = {
    id: 'reviews-table',
    className: 'admin-table',
    columnNames: ['review_id', 'data_created', 'author_name', 'movie_title', 'review_text', 'review_score'],
    title: 'Reviews',
    route: '/reviews/'
}

const formParams = {
    title:'Review',
    id:'review_id',
    route: '/reviews/',
    inputs: [{attr:{
                    type:'select', name:'author_id', value:'', label:'author_name'
                   },
              route: '/users',
              id: 'user_id',
              fieldname:'username'
             }, 
             {attr:{
                    type:'select', name:'movie_id', value:'',required:'required', label:'movie_title',
                   },
              route: '/movies',
              id: 'movie_id',
              fieldname: 'title'
             },
             {attr:{
                    type:'textarea', name:'review_text', value:'',required:'required', maxlength:2000,
                    rows: 5
                   }
             },
             {attr:{
                    type:'number', name:'review_score', value:10, required:'required', min:0, max:10
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