// Create a table element
// Args:
//      params - {id:id, className:className, columnNames:[]}
//      data - []
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

        const editCell = document.createElement('td');
        editCell.appendChild(createEditBtn(item, editFn));
        row.append(editCell);

        const deleteCell = document.createElement('td');
        deleteCell.appendChild(createDeleteBtn(item[params.columnNames[0]], params.route, updateFn));
        row.append(deleteCell);

        tbody.appendChild(row);
    });

    table.appendChild(tbody);

    return table;
}

const createEditBtn = (item, editFn) => {
    const editBtn = document.createElement('button');
    editBtn.textContent = 'Edit';
    
    editBtn.addEventListener('click', async () => {
        editFn(item);
    });

    return editBtn;
}

const createDeleteBtn = (id, route, updateFn) => {
    const delBtn = document.createElement('button');
    delBtn.textContent = 'Delete';

    delBtn.addEventListener('click', async () => {
        response = await fetch(route + id, {method:'delete'});

        if(response.status == 200){
            updateFn();
        }
    });

    return delBtn;
}


// create a form
const createForm = (params, updateFn) => {
    const form = document.createElement('form');
    form.setAttribute('action', params.route);
    form.setAttribute('method', params.method);

    params.inputs.forEach(input => {
        const label = document.createElement('table');
        label.setAttribute('for', input.id);
        label.textContent = input.name;

        form.appendChild(label);
        form.appendChild(createInput(input));
    });

    form.onsubmit = async (e) => {
        e.preventDefault()
        const response = await fetch(params.route, {method: params.method, body: new FormData(form)})

        if(response.status == 200){
            updateFn()
        } else {
            console.log('error');
        }
    }

    return form;
}

// create an input
const createInput = (params) => {
    const input = document.createElement('input');
    input.setAttribute('id', params.name);
    input.setAttribute('type', params.type);
    input.setAttribute('name', params.name);
    input.setAttribute('value', params.value);

    return input;
}

const createAddBtn = (root, formParams, updateFn) => {
    const addBtn = document.createElement('button');
    addBtn.textContent = 'Add';

    addBtn.addEventListener('click', () => {
        createAddForm(root, formParams, updateFn);
    });

    return addBtn;
}

const createAddForm = (root, formParams, updateFn) => {
    const postParams = {...formParams}; 
    postParams.method = 'post';

    postParams.inputs.forEach(input => {
        input.value = input.type == 'submit' ? 'Add' : '';
    });

    const userForm = createForm(postParams, updateFn);

    root.removeChild(root.firstChild);
    root.appendChild(userForm);
}

const createEditForm = (root, formParams, updateFn, data) => {
    const editParams = {...formParams};
    editParams.route = editParams.route + data[editParams.id];
    editParams.method = 'put';

    editParams.inputs.forEach(input => {
        input.value = input.type == 'submit' ? 'Save' : data[input.name];
    });

    const userEditForm = createForm(editParams, updateFn);
    root.removeChild(root.firstChild);
    root.appendChild(userEditForm);
}

const createDBTable = async (tableRoot, tableParams, formRoot, formParams) => {
    const updateFn = createDBTable.bind(this,tableRoot, tableParams, formRoot, formParams);

    while(tableRoot.firstChild){
        tableRoot.removeChild(tableRoot.firstChild);
    }
    
    const response = await fetch(tableParams.route);

    if(response.status == 200){
        const data = await response.json();
        const usersTable = createTable(tableParams, 
                                       data, 
                                       updateFn, 
                                       createEditForm.bind(this, formRoot, formParams, updateFn));
        tableRoot.appendChild(usersTable);
        tableRoot.appendChild(createAddBtn(formRoot, formParams, updateFn));
    } else {
        const errorNode = document.createElement('h1');
        errorNode.textContent = 'Error';
        tableRoot.appendChild(errorNode)
    }
}