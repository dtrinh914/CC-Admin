const tableParams = {
    id: 'followings-table',
    className: 'admin-table',
    columnNames: ['following_id', 'date_created', 'follower_name', 'followee_name'],
    title: 'Followings',
    route: '/followings/'
}

const formParams = {
    title:'Following',
    id:'following_id',
    route: '/followings/',
    inputs: [{attr:{
                    type:'select', name:'follower_id', value: 1, required:'required', label:'follower_name'
                   },
              route: '/users',
              id: 'user_id',
              fieldname: 'username'
             }, 
             {attr:{
                    type:'select', name:'followee_id', value: 1, required:'required', label:'followee_name'
                   },
              route: '/users',
              id: 'user_id',
              fieldname: 'username'
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