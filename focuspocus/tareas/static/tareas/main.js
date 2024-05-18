let IdCounter = 0;
const input = document.querySelector('input[type="text"]');

userInput.addEventListener('submit', (event)=>{
    event.preventDefault();
    if(input.value.trim().length != 0){
        addTask();
    }
});

let addTask = ()=>{
    IdCounter++;

    //Recoger Texto
    let newValue = input.value;

    //Agregar tarea
    const newTask = `
        <div class="task-container" id="${IdCounter}">
            <label>
                <input type="checkbox"> 
                ${newValue}
            </label>
            <img src="./images/delete.png" class="closeBtn">
        </div>
    `;
    list.innerHTML += newTask;
    input.value = '';
    updateStats();
}

list.addEventListener('click', (event)=>{
    if(event.srcElement.nodeName == 'INPUT'){
        updateStats();
    }else if(event.srcElement.nodeName == 'IMG'){
        deleteTask(event.srcElement.parentNode.id);
    }
});

let updateStats = () => {
    let totalTasks = document.querySelectorAll('.task-container').length;
    let completedCount = document.querySelectorAll('input[type="checkbox"]:checked').length;
    let pendingCount = totalTasks - completedCount;
    
    stats.innerHTML = `Tareas pendientes: ${pendingCount} Completadas: ${completedCount}`;
};

let deleteTask = (id)=>{
    let taskToDelete = document.getElementById(id);
    list.removeChild(taskToDelete);
    updateStats();
};