<template>
  <div v-for="todo in todoList" :key="todo.id" class="container">
    <div class="card mb-3">
      <div class="card-header">{{ todo.title }}</div>
      <div class="card-body">
        <p class="card-text">{{ todo.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'TodoList',
  data() {
    return {
      todoList: [],
    }
  },

  methods: {
    async getTodoList() {
      const response = await axios.get("http://127.0.0.1:8000/api-v1/todos/");
      this.todoList = response.data;
    },
  },

  created() {
    this.getTodoList();
  }

}
</script>
