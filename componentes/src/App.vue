<script setup>

import ExpandBox from './components/ExpandBox.vue'
import Card from './components/Card.vue'
import CardFull from './components/CardFull.vue'

const caixas = [
  {id: 1, title: 'Caixa 1', content: 'Conteúdo', qty: 100},
  {id: 2, title: 'Caixa 2', qty: 30},
  {id: 3, title: 'Caixa 3', content: 'Conteúdo 3'},
  {id: 4, title: 'Caixa 4'}
]

</script>

<template>

  <h1>Componentes</h1>
  <hr />

  <div>

    <h2>Props</h2>

    <expand-box v-for="caixa in caixas" :key="caixa.id" v-bind="caixa"/> 

    <!--<ExpandBox title="Caixa 1" content="Conteúdo secreto da caixa 1"/>
    <expand-box title="Caixa 2" qty="50"/>-->

  </div>

  <div>

    <h2>Slot</h2>

    <card title="Titulo do Card">
      <p>Conteúdo do Card</p>
    </card>

    <card title="Card 2"></card>

    <CardFull>

      <h2>Meus Dados</h2>
      <p>Body</p>

      <template #header>
        <h1>Meu nome</h1>
      </template>

      <template #footer>
        <p>Dados do card</p>
      </template>

    </CardFull>

  
    <div class="card">

      <div v-if="$slots.header" class="header">
          <slot name="header"></slot>
      </div>

      <div class="body">
        <slot>
          <p>Conteúdo padrão do card</p>
        </slot>
      </div>

      <div v-if="$slots.footer" class="footer">
        <slot name="footer"></slot>
      </div>
    </div>

  </div>

</template>


<style scoped></style>
