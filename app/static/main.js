/*
Create a table element
Args:
    params - {id:id, className:className, columnNames:[]}
    data - []
    updateFn - function to update table
    editFn - function to open edit form

Returns:
    Table element
*/
const createTable = (params, data, updateFn, editFn) => {
    const table = document.createElement('table');
    table.id = params.id;
    table.className = params.className;

    // create table header
    const thead = document.createElement('thead');
    const rowHeader = document.createElement('tr');
    thead.appendChild(rowHeader);

    params.columnNames.forEach(columnName => {
        const header = document.createElement('th');
        header.textContent = columnName;
        rowHeader.append(header);
    });

    table.appendChild(thead);

    // create table body
    const tbody = document.createElement('tbody');

    // fill each cell with data from data parameter
    data.forEach( item => {
        const row = document.createElement('tr');

        params.columnNames.forEach(columnName => {
            const cell = document.createElement('td');
            cell.textContent = item[columnName];
            row.appendChild(cell);
        });
        
        // add in edit button for each row
        const editCell = document.createElement('td');
        editCell.appendChild(createEditBtn(item, editFn));
        row.append(editCell);

        // add in delete button for each row
        const deleteCell = document.createElement('td');
        deleteCell.appendChild(createDeleteBtn(item[params.columnNames[0]], params.route, updateFn));
        row.append(deleteCell);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);

    return table;
}

/*
Creates an Edit button that opens an edit form

Args:
    item - object containing values for a row
    editFn - function to open form and populate with data from item

Returns:
    An edit button
*/
const createEditBtn = (item, editFn) => {
    const editBtn = document.createElement('button');
    editBtn.textContent = 'Edit';
    editBtn.className = 'btn-outline';
    
    editBtn.addEventListener('click', async () => {
        const form = editFn(item);
        form.scrollIntoView({behavior: 'smooth'});
    });

    return editBtn;
}


/*
Creates an Delete button that deletes a row

Args:
    id - id of item to delete
    route - url delete route
    updateFn - function to update table
Returns:
    A delete button
*/
const createDeleteBtn = (id, route, updateFn) => {
    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';
    delBtn.className = 'btn-primary';

    delBtn.addEventListener('click', async () => {
        response = await fetch(route + id, {method:'delete'});

        if(response.status == 200){
            updateFn();
        }
    });

    return delBtn;
}


/*
Creates an form

Args:
    params - id of item to delete {title, route, method, inputs}
    updateFn - function to update table
Returns:
    A form element
*/
const createForm = (params, updateFn) => {
    // create form element
    const form = document.createElement('form');
    form.setAttribute('action', params.route);
    form.setAttribute('method', params.method);
    form.className = 'table-form';
    
    // add title
    const title = document.createElement('h2');
    title.textContent = params.title;
    form.appendChild(title);

    // create input for each item in params.inputs
    params.inputs.forEach(input => {

        if(input.attr.type !== 'submit'){
            const label = document.createElement('label');
            label.setAttribute('for', input.attr.name);
            const labelName = input.attr.label || input.attr.name
            label.textContent = labelName;
            form.appendChild(label);
        }
        
        form.appendChild(createInput(input));
    });

    // add field for error msgs
    const errorMsg = document.createElement('p');
    form.appendChild(errorMsg);


    // add submit functionality
    form.onsubmit = async (e) => {
        e.preventDefault()
        const response = await fetch(params.route, {method: params.method, body: new FormData(form)})

        if(response.status == 200){
            updateFn()
        } else {
            const errorData = await response.json();
            errorMsg.textContent = errorData.error;
        }
    }

    return form;
}

/*
Creates an input element

Args:
    params: parameters for the input
Returns:
    An input element
*/
const createInput = (params) => {
    let input;

    if(params.attr.type == 'textarea'){
        input = document.createElement('textarea');
        input.textContent = params.attr.value;
    } else if(params.attr.type == 'select'){
        input = createSelect(params);
    } else {
        input = document.createElement('input');
    }

    // set input attribute
    for(const attr in params.attr){
        input.setAttribute(attr, params.attr[attr]);
    }

    if(params.attr.type !== 'submit'){
        input.id = params.attr.name
    }
    
    return input;
}

/*
Creates a select element

Args:
    params: parameters for the select element
Returns:
    An select element
*/
const createSelect = (params) => {
    const select = document.createElement('select');

    (async () => {
        // add extra select options
        if(params.extraOptions){
            params.extraOptions.forEach(extraOption => {
                const option = document.createElement('option');
                option.setAttribute('value', extraOption.value);
                option.textContent = extraOption.text;

                if(params.attr.value == ''){
                    option.selected = true;
                }

                select.appendChild(option);
            });
        }
        
        const response = await fetch(params.route);

        if(response.status == 200){
            const data = await response.json();
            
            // create an option for each item in data
            data.forEach(item => {
                const option = document.createElement('option');
                const id = params.id
                option.setAttribute('value', item[id]);
                option.textContent = item[params.fieldname];

                // if the param value is equal to the item value, set it as selected
                if(item[id] == params.attr.value){
                    option.selected = true;
                }

                select.appendChild(option);
            });
        }
    })();
    
    return select;
}


/*
Creates an add button that opens the add form

Args:
    root: root to pass to createAddForm
    formParams: form parameters to pass to createAddForm
    updateFn: update function to pass to createAddForm
Returns:
    An add button
*/
const createAddBtn = (root, formParams, updateFn) => {
    const addBtn = document.createElement('button');
    addBtn.textContent = 'Open Add Form';
    addBtn.className = 'btn';

    addBtn.addEventListener('click', () => {
        const form = createAddForm(root, formParams, updateFn);
        form.scrollIntoView({behavior: 'smooth'});
    });

    return addBtn;
}


/*
Creates an add form and appends it to the root.

Args:
    root: root element to append form to
    formParams: form parameters 
    updateFn: update function
Returns:
    None
*/
const createAddForm = (root, formParams, updateFn) => {
    const postParams = {...formParams}; 
    postParams.method = 'post';
    postParams.title = 'Add ' + postParams.title;

    // clear values of input, except for submit
    postParams.inputs.forEach(input => {
        input.attr.value = input.attr.type == 'submit' ? 'Add' : '';
    });

    // add additional logic to the update function
    const appendedUpdate = () => {
        updateFn();
        createAddForm(root, formParams, updateFn);
    }

    // create the form
    const userForm = createForm(postParams, appendedUpdate);

    // append the form
    while(formRoot.firstChild){
        formRoot.removeChild(formRoot.firstChild);
    }

    root.appendChild(userForm);

    return userForm;
}


/*
Creates an edit form and appends it to the root.

Args:
    root: root element to append form to
    formParams: form parameters 
    updateFn: update function
    data: to populate the edit form
Returns:
    None
*/
const createEditForm = (root, formParams, updateFn, data) => {
    const editParams = {...formParams};
    editParams.route = editParams.route + data[editParams.id];
    editParams.method = 'put';
    editParams.title = 'Edit ' + editParams.title;

    //populate each input with it's value
    editParams.inputs.forEach(input => {
        input.attr.value = input.attr.type == 'submit' ? 'Save' : data[input.attr.name];
    });

    // add addition logic to the update function
    const appendedUpdate = () => {
        updateFn();
        createAddForm(root, formParams, updateFn);
    }

    // create and append edit form 
    const userEditForm = createForm(editParams, appendedUpdate);
    
    while(formRoot.firstChild){
        formRoot.removeChild(formRoot.firstChild);
    }

    root.appendChild(userEditForm);

    return userEditForm;
}

/*
Creates a filter input.

Args:
    params: filter paramters
Returns:
    A filter input
*/
const createFilter = (params, updateFn) => {
    const form = document.createElement('form');
    form.className = 'filter-form';

    const label = document.createElement('label');
    label.setAttribute('for', 'filter_str');
    label.textContent = `Filter by ${params.by}:`;
    form.appendChild(label);

    // filter input
    const filterInput = createInput({attr:
                                        {type:'text', 
                                         name:'filter_str', 
                                         value:params.filterValue,
                                         class:'filter-input'
                                        }
                                     });
    form.appendChild(filterInput);

    // submit button
    form.appendChild(createInput({attr:{type:'submit', value:'Filter', class:'btn'}}));

    // create clear button
    const clearBtn = document.createElement('button');
    clearBtn.className = 'btn-primary-outline'
    clearBtn.textContent = 'Clear Filter';
    clearBtn.onclick = (e) => {
        e.preventDefault();
        params.filterValue = '';
        updateFn()
    };

    form.appendChild(clearBtn);

    form.onsubmit = (e) => {
        e.preventDefault();
        params.filterValue = filterInput.value;
        updateFn()
    }

    return form
};


/*
Creates an DB table and it's functionality and appends it to the root

Args:
    tableRoot: root element to append table to
    tableParams: table parameters
    formRoot: root element to append form to
    formParams: form parameters 
Returns:
    None
*/
const createDBTable = async (tableRoot, tableParams, formRoot, formParams) => {
    // create update function to update the table
    const updateFn = createDBTable.bind(this,tableRoot, tableParams, formRoot, formParams);

    // remove previous table
    while(tableRoot.firstChild){
        tableRoot.removeChild(tableRoot.firstChild);
    }

    // add in add form if no form is present
    if(formRoot.childElementCount == 0){
        createAddForm(formRoot, formParams, updateFn);
    }

    // add title
    const title = document.createElement('h1');
    title.textContent = `${tableParams.title} Table`;
    tableRoot.append(title);

    let getRoute = tableParams.route;

    if(tableParams.filter){
        const filterForm = createFilter(tableParams.filter, updateFn);
        tableRoot.append(filterForm);
        getRoute = getRoute + `?q=${tableParams.filter.filterValue}`;
    }
    
    // get table data from db
    const response = await fetch(getRoute);

    if(response.status == 200){
        // add in table data if success
        const data = await response.json();

        if(data.length == 0){
            // display no data msg
            const noData = document.createElement('h1');
            noData.textContent = tableParams.filter && tableParams.filter.filterValue ?
                                    'There are no rows that match the filter value.': 
                                    'There is no data in the table.';
            tableRoot.appendChild(noData)
        } else {
            const usersTable = createTable(tableParams, 
                                        data, 
                                        updateFn, 
                                        createEditForm.bind(this, formRoot, formParams, updateFn));
            tableRoot.appendChild(usersTable);
            tableRoot.appendChild(createAddBtn(formRoot, formParams, updateFn));
        }
    } else {
        // display error msg
        const errorNode = document.createElement('h1');
        errorNode.textContent = 'Unable to retrieve data.';
        tableRoot.appendChild(errorNode)
    }
}