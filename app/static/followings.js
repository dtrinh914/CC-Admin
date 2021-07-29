const tableParams = {
    id: 'followings-table',
    className: 'admin-table',
    columnNames: ['following_id', 'date_created', 'follower_id', 'followee_id'],
    route: '/followings/'
}

const formParams = {
    title:'Following',
    id:'following_id',
    route: '/followings/',
    inputs: [{attr:{
                    type:'number', name:'follower_id', value: 1, required:'required'
                   }
             }, 
             {attr:{
                    type:'number', name:'followee_id', value: 1, required:'required'
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