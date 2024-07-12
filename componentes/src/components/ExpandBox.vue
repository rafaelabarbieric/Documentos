<script setup>

import { ref, computed } from 'vue'

const props = defineProps(['title', 'content', 'subtitle'])

const showBox = ref(false)

const textoBotao = computed(() => 
    showBox.value ? 'Esconder' : 'Mostrar'
)

</script>

<template>

    <div>

        <button @click="showBox = !showBox">{{ textoBotao }}</button>

        <div v-if="showBox" class="expand-box">
            <h1>{{ props.title }}</h1>
            <p>{{ props.content }}</p>
            <h2 class="color">{{ props.subtitle }}</h2>
        </div>

    </div>

</template>

<style scoped>
.expand-box{
    height: 100%;
    width: 400px;
    padding: 20px;
    border-radius: 10px;
    border: 1px solid black;
    box-shadow: 3px 3px 2px 2px gray;
}
.color{
    color: red;
}

</style>