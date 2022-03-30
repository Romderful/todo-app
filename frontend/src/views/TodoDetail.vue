<template>
    <div class="container">
        <h3 class="mb-5">{{ todoDetail.title }}</h3>
        <p>{{ todoDetail.description }}</p>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: 'TodoDetail',
    props: ["id"],
    data() {
        return {
            todoUrl: `http://127.0.0.1:8000/api-v1/todos/${this.id}/`,
            todoDetail: [],
        }
    },

    methods: {
        async getTodoDetail() {
            const response = await axios.get(this.todoUrl)
            this.todoDetail = response.data;
        },
    },

    created() {
        this.getTodoDetail();
    }
}
</script>
