<script setup>

import { ref, computed } from 'vue'

// defineProps(['title', 'content', 'subtitle'])
defineProps({
    title:{
        type: String,
        required: true
    },
    content:{
        type: String,
        default: 'Valor padrão da minha caixa...'
    },
    qty:{
        type: Number,
        default: 10
    }
})

const showBox = ref(false)

const textoBotao = computed(() => 
    showBox.value ? 'Esconder' : 'Mostrar'
)

</script>

<template>

    <div>

        <button @click="showBox = !showBox">{{ textoBotao }}</button>

        <div v-if="showBox" class="expand-box">

            <h1>{{ title }}</h1>
            <p>{{ content }}</p>
            <p>Quantidade: {{ qty }}</p>

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


</style>