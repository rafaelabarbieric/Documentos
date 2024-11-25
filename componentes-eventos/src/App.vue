<script setup>
import { ref } from 'vue'
import ProductList from '@/components/ProductList.vue'

const produtos = ref([
  { id: 1, nome: 'Produto A', preco: 'R$ 20,50' },
  { id: 2, nome: 'Produto B', preco: 'R$ 30,50' },
  { id: 3, nome: 'Produto C', preco: 'R$ 20,50' },
  { id: 4, nome: 'Produto D', preco: 'R$ 20,50' }
])

function excluirProduto(id) {
  const index = produtos.value.findIndex((produto) => produto.id === id)
  produtos.value.splice(index, 1)
}

function excluirTodosProdutos(){
  produtos.value = []
}

</script>

<template>

  <h1>Meus Produtos</h1>

  <product-list
    :produtos="produtos"
    @excluir="excluirProduto"
    @excluirTudo="excluirTodosProdutos"
  />
  
</template>

<style scoped></style>
