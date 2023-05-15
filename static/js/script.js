const app = Vue.createApp({
  data() {
    return {
      tasks: []
    }
  },
  mounted() {
    axios.get('/tasks')
      .then(response => {
        this.tasks = response.data;
        console.log(this.tasks);
      })
      .catch(error => {
        console.log(error);
      });
  },
  methods: {
    addNewTask() {
      axios.post('/new_task', {
        newTaskTitle: this.newTaskTitle,
        newTaskDescription: this.newTaskDescription,
        newTaskDueDate: this.newTaskDueDate,
          completed: 0,
        }, { headers: { 'Content-Type': 'application/json' } })
        .then(response => {
          const newTask = response.data;
          this.tasks.push(newTask);
          this.newTaskTitle = '';
          this.newTaskDescription = '';
          this.newTaskDueDate = '';
          console.log(this.tasks);
        })
        .catch(error => {
          console.log(error);
        });
    },
  
    deleteTask(event) {
      const taskId = event.target.dataset.taskId.replace('data-task-id-', '');
      const task_to_delete = `http://localhost:5000/tasks/${taskId}`;
      axios.delete(task_to_delete)
      .then(response => {
        this.tasks = this.tasks.filter(task => task.id !== taskId);
      })
      .catch(error => {
        console.error("DELETE TASK ERROR", taskId);
      });
    },
    
  
    
    

    updateTask(task) {
      axios.patch(`/update_task/${task.id}`, {completed: task.completed})
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },
  }
});

app.mount('#app');
