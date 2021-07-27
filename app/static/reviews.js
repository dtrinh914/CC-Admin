const tableParams = {
    id: 'reviews-table',
    className: 'admin-table',
    columnNames: ['review_id', 'data_created', 'author_id', 'movie_id', 'review_text', 'review_score'],
    route: '/reviews/'
}

const formParams = {
    title:'Review',
    id:'review_id',
    route: '/reviews/',
    inputs: [{attr:{
                    type:'number', name:'author_id', value:''
                   }
             }, 
             {attr:{
                    type:'number', name:'movie_id', value:'',required:'required'
                   }
             },
             {attr:{
                    type:'textarea', name:'review_text', value:'',required:'required', maxlength:2000
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